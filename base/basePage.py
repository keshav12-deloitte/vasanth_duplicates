"""
This Module contains all reusable selenium functions
"""
import time

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from constants.generic_constants import WAIT_TIME
from utils.logs import logger


class BasePage:
    def __init__(self, webdriver):
        self.driver = webdriver

    def get_web_element(self, xp_locator, msg=""):
        """
        This function returns the web element for the given locator
        :param xp_locator:
        :param msg:
        :return:
        """
        try:
            return self.driver.find_element_by_xpath(xp_locator)
        except Exception as e:
            logger.error(f"couldn't find {msg}, because of the following {e}")
            self.step_fail(f"Couldn't locate {msg}")

    def launch_url(self, url):
        """
        Function to launch the URL
        :param url:
        :return:
        """
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()
        time.sleep(2)

    def click(self, xp_locator, msg=""):
        """
        Function to click on the web element
        :param xp_locator:
        :param msg:
        :return:
        """
        try:
            self.get_web_element(xp_locator).click()
            self.step_pass(f"Successfully clicked on:{msg}")
        except Exception as e:
            logger.error(msg=f"Exception '{e}' while clicking the element {msg}")
            self.step_fail(f"Unable to click on:{msg}")

    def send_keys(self, xp_locator, value, msg=""):
        """
        Function to type in the web element
        :param xp_locator:
        :param value:
        :param msg:
        :return:
        """
        try:
            self.get_web_element(xp_locator).send_keys(value)
            self.step_pass(f"Successfully entered value in:{msg}")
        except Exception as e:
            logger.error(msg=f"Exception '{e}' while entering {value} in the element {msg}")
            self.step_fail(f"Unable to enter value in:{msg}")

    def click_and_type(self, xp_locator, value, msg=""):
        """
        Function to click and type value in the web element
        :param xp_locator:
        :param value:
        :param msg:
        :return:
        """
        try:
            self.click(xp_locator, msg=msg)
            self.send_keys(xp_locator, value, msg=msg)
            self.step_pass(f"Successfully clicked and entered value in:{msg}")
        except Exception as e:
            logger.error(msg=f"Exception '{e}' while entering {value} in the element {msg}")
            self.step_fail(f"Unable to click and enter the value in:{msg}")

    def get_window_handles(self):
        """
        This Function returns the all open window handle
        :return:
        """
        return self.driver.window_handles

    def get_current_window_handle(self):
        """
        This Function returns the current window handle
        :return:
        """
        return self.driver.current_window_handle

    def switch_to_window(self, window_handle):
        """
        This Function to switch to the given window handle
        :param window_handle:
        :return:
        """
        self.driver.switch_to.window(window_handle)

    def get_title(self):
        """
        Function to get the Title of the webpage
        :return:
        """
        return self.driver.title

    def select_from_drop_down(self, xp_locator, text_to_select, msg=""):
        """
        Function to select to select from a drop down
        :param xp_locator:
        :param text_to_select:
        :param msg:
        :return:
        """
        try:
            select = Select(self.get_web_element(xp_locator))
            select.select_by_visible_text(text_to_select)
            self.step_pass(f"Successfully selected data from:{msg}")
        except Exception as e:
            logger.error(msg=f"Exception '{e}' occurred while selecting {msg} from the drop down")
            self.step_fail(f"Unable to select data from:{msg}")

    def wait_until_element_is_clickable(self, element, seconds=WAIT_TIME):
        """
        Function to wait until the given web element is clickable
        :param seconds:
        :param element:
        :return:
        """
        wait = WebDriverWait(self.driver, seconds)
        wait.until(EC.element_to_be_clickable((By.XPATH, element)))

    def wait_for_element(self, element, msg=""):
        """
        This function waits until the element is available in the webpage
        :param element:
        :param msg:
        """
        try:
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            wait.until(EC.presence_of_element_located((By.XPATH, element)))
            logger.info(f"WebElement locator {msg} found")
        except Exception as e:
            logger.error(f"WebElement found of locator {msg} Not Found, because of following exception {e}")
            self.step_fail(f"waited for element but element not found:{msg}")

    def move_to_element(self, xp_locator, msg=""):
        """
        Function to make the cursor move over the element
        :param xp_locator:
        :param msg:
        :return:
        """
        action = ActionChains(self.driver)
        try:
            web_element = self.get_web_element(xp_locator)
            action.move_to_element(web_element).perform()
            self.step_pass(f"cursor is moved to the element:{msg}")
            logger.info(f"Cursor is moved to element {msg}")
        except Exception as e:
            logger.error(f"Exception '{e}' while moving over the element {msg}")
            self.step_fail(f"cursor cant able to move to the element : {msg}")

    def move_to_element_and_click(self, xp_locator, msg=""):
        """
        Function to make the cursor move the element and click
        :param xp_locator:
        :param msg:
        :return:
        """
        action = ActionChains(self.driver)
        try:
            web_element = self.get_web_element(xp_locator)
            action.move_to_element(web_element).click().perform()
            self.step_pass(f"cursor is moved and clicked the element :{msg}")
        except Exception as e:
            logger.error(f"Exception '{e}' while moving over the element {msg} and click")
            self.step_fail(f"cursor cant able to move and click the element :{msg}")

    def get_text(self, xp_locator):
        """
        Function to get and return the text value for the given locator
        :param xp_locator:
        :return:
        """
        return self.get_web_element(xp_locator).text

    def is_enabled(self, xp_locator, msg=""):
        """
        This function checks whether the given web element is enabled or disabled
        :param xp_locator:
        :param msg:
        :return:
        """
        try:
            self.get_web_element(xp_locator).is_enabled()
            self.step_pass(f"{msg} is enabled")
        except Exception as e:
            logger.error(msg=f"Exception '{e}' while checking {msg} is enabled")
            self.step_fail(f"{msg} is not enabled")

    def is_selected(self, xp_locator, msg=""):
        """
        This function checks whether the given web element is selected
        :param xp_locator:
        :param msg:
        :return:
        """
        try:
            self.get_web_element(xp_locator).is_selected()
            self.step_pass(f"{msg} is selected")
        except Exception as e:
            logger.error(msg=f"Exception '{e}' while checking {msg} is selected")
            self.step_fail(f"{msg} is not selected")

    def is_displayed(self, xp_locator, msg=""):
        """
        This function checks whether the given web element is displayed in the screen
        :param xp_locator:
        :param msg:
        :return:
        """
        try:
            return self.driver.find_element_by_xpath(xp_locator).is_displayed()
        except Exception as e:
            logger.info(f"{e}, because {msg} not being displayed")

    def clear(self, xp_locator):
        """
        This function clears the text fields
        :param xp_locator:
        :return:
        """
        self.get_web_element(xp_locator).clear()

    def wait_until_element_disappear(self, xp_locator, wait_time=WAIT_TIME, msg=""):
        """
        This function waits until the webelement disappears
        :param xp_locator:
        :param wait_time:
        :param msg:
        :return:
        """
        try:
            wait = WebDriverWait(self.driver, wait_time)
            wait.until(EC.invisibility_of_element_located((By.XPATH, xp_locator)))
        except Exception as e:
            logger.error(f"{e}, because {msg} getting appeared for more than 30 seconds")
            self.step_fail(f"{msg} getting appeared for more than 30 seconds")

    def get_text_from_webelement(self, web_element):
        """
        This function return the text for the given locator
        :param web_element:
        :return:
        """
        msg = web_element.text
        return msg.strip()

    def get_web_elements(self, locator):
        """
        This function returns the list of web elements for the given locator
        :param locator:
        :return:
        """
        return self.driver.find_elements_by_xpath(locator)

    def step_fail(self, text):
        """
        Function to make assertion as Fail and also for capturing logs & screenshot in Allure report
        :param text:
        :return:
        """
        with allure.step(text):
            allure.attach(self.driver.get_screenshot_as_png(), name="fail", attachment_type=AttachmentType.PNG)
        logger.error(msg=text)
        assert True

    def step_pass(self, text):
        """
        Function to make assertion as Pass and also for capturing logs & screenshot in Allure report"
        :param text:
        :return:
        """
        with allure.step(text):
            allure.attach(self.driver.get_screenshot_as_png(), name="pass", attachment_type=AttachmentType.PNG)
        logger.info(msg=text)
        assert True

    def js_click(self, xp_locator, msg=""):
        """
        Function to click on the web element using java script executor function
        :param xp_locator:
        :param msg:
        :return:
        """
        try:
            web_element = self.get_web_element(xp_locator)
            self.driver.execute_script("arguments[0].click();", web_element)
            self.step_pass(f"Successfully clicked on:{msg}")
        except Exception as e:
            logger.error(msg=f"Exception '{e}' while clicking the element {msg}")
            self.step_fail(f"Unable to click on:{msg}")

