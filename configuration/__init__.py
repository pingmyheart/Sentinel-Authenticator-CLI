import logging.config

import colorama

import configuration.environment

# Initialize Colorama
colorama.init(autoreset=True)


# Define color codes
class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': colorama.Fore.LIGHTBLACK_EX,  # Gray
        'INFO': colorama.Fore.BLUE,  # Blue
        'WARNING': colorama.Fore.YELLOW,  # Yellow
        'ERROR': colorama.Fore.RED,  # Red
        'CRITICAL': colorama.Fore.WHITE + colorama.Back.RED,  # White on Red
    }

    def format(self, record):
        # Set the color based on the log level
        color = self.COLORS.get(record.levelname, colorama.Fore.RESET)
        record.msg = color + str(record.msg) + colorama.Fore.RESET
        return super().format(record)


stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(ColoredFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                             datefmt='%Y-%m-%d %H:%M:%S'))
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        stream_handler
    ]
)

environment_impl = environment.Environment()
