import configparser
import os


class Configuration:

    def __init__(self):
        self._parser = configparser.ConfigParser()
        self._parser.read(os.getenv('CONFIG_PATH', 'config.ini'))


    def get_browser(self):
        """Get selenium instance of driver (chrome, firefox etc.)"""
        # TODO DEMO-QA-003 Implement getting selenium driver in config class
        pass
