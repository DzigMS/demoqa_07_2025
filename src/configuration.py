import configparser
import os
from pathlib import Path

from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteDriver


class Configuration:

    def __init__(self):
        self._parser = configparser.ConfigParser()
        self._parser.read(Path(os.getenv("CONFIG_PATH", "config.ini")).absolute())


    def get_browser(self):
        """Get selenium instance of driver (chrome, firefox etc.)"""
        browser = self._get_driver()
        wait_time = self._parser.getfloat('browser', 'wait')
        browser.implicitly_wait(wait_time)
        maximize = self._parser.getboolean('browser', 'maximize')
        if maximize:
            browser.maximize_window()

        return browser

    @staticmethod
    def _get_driver():
        driver = os.getenv("BROWSER", "Chrome")
        if driver == "Chrome":
            return ChromeDriver()
        elif driver == "Firefox":
            return FirefoxDriver()
        else:
            return RemoteDriver()

    def get_base_url(self):
        # return self._parser['demoqa'].get('url')
        return self._parser.get('demoqa', 'url')


CONFIG = Configuration()