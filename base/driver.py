import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as ffOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.logs import logger


class WebDriver:
    """
    This class consists of functions that are to be used for creating driver instance
    """

    def get_web_driver(self, browser_name, headless):
        """
        This function gets the web driver instance based on the params passed
        :param browser_name:
        :param headless:
        :return:
        """
        global driver
        try:
            headless_bool = json.loads(headless.lower())
            logger.info(f"the browser is {browser_name}")
            if browser_name == "chrome":
                options = ChromeOptions()
                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                if headless_bool:
                    options.add_argument("headless")
                    options.add_argument("--disable-gpu")
                    options.add_argument("--window-size=1920,1080")
                driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            elif browser_name == "firefox":
                options = ffOptions()
                if headless_bool:
                    options.headless = True
                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
            elif browser_name == "edge":
                driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
            return driver
        except Exception as e:
            logger.error(f"{e} while instantiating the driver")
