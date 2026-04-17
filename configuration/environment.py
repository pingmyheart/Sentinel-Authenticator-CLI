import os


class Environment:
    def __init__(self):
        from dotenv import load_dotenv
        load_dotenv()

        self.configuration_file = os.getenv("CONFIGURATION_FILE", None)
