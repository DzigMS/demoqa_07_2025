import configparser
import os
from pathlib import Path


class Configuration:

    def __init__(self):
        self._parser = configparser.ConfigParser()
        self._parser.read(Path(os.getenv("CONFIG_PATH", "config.ini")).absolute())


    def get_browser(self):
        """Get selenium instance of driver (chrome, firefox etc.)"""
        # TODO DEMO-QA-003 Implement getting selenium driver in config class
        pass

    def get_base_url(self):
        return self._parser['demoqa'].get('url')



CONFIG = Configuration()