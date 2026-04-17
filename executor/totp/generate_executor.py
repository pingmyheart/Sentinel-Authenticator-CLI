import logging
from urllib.parse import urlparse, parse_qs, unquote

import pyotp

from configuration.environment import Environment
from dto.common.executor import ExecutorResponse
from executor.executor import Executor
from service import global_checker_service_impl


class GenerateExecutor(Executor):
    def __init__(self, env: Environment):
        super().__init__(env)
        self.log = logging.getLogger(__name__)

    def execute(self, **kwargs) -> ExecutorResponse:
        () = self._load_check_args(kwargs)
        self.pre_check_executor()

        totp_list = []

        # Open config file and parse
        with open(self.env.configuration_file, 'r') as file:
            # Read each line
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                try:
                    result = self.__parse_otpauth_full(line)
                    totp = pyotp.TOTP(result['params']['secret']).now()
                    result['totp'] = totp
                    totp_list.append(result)
                except Exception as e:
                    self.log.error(f"Failed to parse line: {line}. Error: {str(e)}")

        totp_list = sorted(totp_list, key=lambda x: x['params']['issuer'])

        for element in totp_list:
            element["params"]["secret"] = "Hidden"

        return ExecutorResponse(response=totp_list)

    def usage(self):
        pass

    def _load_check_args(self, kwargs):
        variables = {
        }
        global_checker_service_impl.check_required_none_values(dictionary=variables)

        return ()

    def pre_check_executor(self, **kwargs):
        pass

    def __parse_otpauth_full(self, url: str) -> dict:
        self.log.debug(f"Parsing OTPAuth URL: {url}")
        parsed = urlparse(url)

        params = parse_qs(parsed.query)
        params = {k: v[0] for k, v in params.items()}

        # Extract type (totp/hotp)
        otp_type = parsed.netloc

        # Extract label (and decode it)
        label = unquote(parsed.path.lstrip("/"))

        return {
            "type": otp_type,
            "label": label,
            "params": params
        }
