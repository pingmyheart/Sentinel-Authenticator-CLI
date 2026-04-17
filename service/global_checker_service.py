import logging
import socket
import subprocess
from urllib.parse import urlparse

from configuration.environment import Environment


class GlobalCheckerService:
    def __init__(self, env: Environment):
        self.env = env
        self.log = logging.getLogger(__name__)

    def check_required_none_values(self, dictionary: dict):
        self.log.info("Checking required arguments...")
        for key, value in dictionary.items():
            if value is None:
                raise RuntimeError(f"Required arguments expected: {key}")
        self.log.info("Checking required arguments completed.")

    def check_docker_installed(self):
        self.log.info("Checking docker installation...")
        try:
            result = subprocess.run(['docker', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                self.log.info("Docker is installed.")
                return True
            else:
                self.log.error("Docker is not installed.")
                return False
        except FileNotFoundError:
            self.log.error("Docker command not found. Docker is not installed.")
            return False

    def check_docker_running(self):
        self.log.info("Checking docker execution...")
        try:
            result = subprocess.run(['docker', 'info'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                self.log.info("Docker is running.")
                return True
            else:
                self.log.error("Docker is installed but not running.")
                return False
        except FileNotFoundError:
            self.log.error("Docker command not found. Docker is not installed.")
            return False

    def verify_reachability(self, url: str):
        parsed_url = urlparse(url)
        if parsed_url.scheme:  # If the URL has a scheme like http/https
            return self.__check_url_reachable(url)
        else:
            return self.__check_host_port_reachable(url)

    def __check_host_port_reachable(self, host_port):
        try:
            host, port = host_port.split(':')
            port = int(port)
            with socket.create_connection((host, port), timeout=5):
                self.log.info(f"Host {host} on port {port} is reachable.")
                return True
        except (socket.timeout, ConnectionRefusedError):
            self.log.error(f"Host {host} on port {port} is not reachable.")
            return False
        except ValueError:
            self.log.error(f"Invalid format for host and port: {host_port}. Should be 'host:port'.")
            return False
