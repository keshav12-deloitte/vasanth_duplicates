"""
This Module contains all basic functions required across pages and modules in the application
"""
from datetime import date, timedelta

import allure

from base.basePage import BasePage
from constants import document_constants as DC
from constants import generic_constants as GC
from utils.environment_variables import OTP


# # import ffmpeg
# import requests
# import urllib.request
# # from pydub import AudioSegment
# import os
# import speech_recognition as sr
# import subprocess

class GenericFunctions(BasePage):
    """
    This class consists of reusable functions which can generic and can be used across the modules
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_element_is_displayed(self, element_to_be_checked, msg=""):
        """
        Function to check whether the elements is displayed
        :param element_to_be_checked:
        :param msg:
        :return:
        """
        is_displayed = self.is_displayed(element_to_be_checked)
        if is_displayed:
            self.step_pass(f"{msg} is displaying as Expected")
        else:
            self.step_fail(f"{msg} is not displaying")

    def check_element_not_displayed(self, element_to_be_checked, msg=""):
        """
        Function to check whether the elements is NOT displayed
        :param element_to_be_checked:
        :param msg:
        :return:
        """
        is_displayed = self.is_displayed(element_to_be_checked)
        if not is_displayed:
            self.step_pass(f"{msg} is NOT displaying as expected")
        else:
            self.step_fail(f"{msg} is displaying, which is NOT expected")

    def check_values(self, expected, actual):
        """
        Function to check whether the expected and actual are equal, makes step Pass if equal else not
        :param expected:
        :param actual:
        :return:
        """
        if expected == actual:
            self.step_pass(f"Expected is {expected} and Actual is {actual}, hence step passed")
        else:
            self.step_fail(f"Expected is {expected} and Actual is {actual}, hence step failed")

    def compare_value(self, expected, actual):
        """
        Function to check whether the expected and actual are equal, makes step Pass if equal else not
        :param expected:
        :param actual:
        :return:
        """
        if expected < actual:
            self.step_pass(f"Expected is {expected} and Actual is {actual}, hence step passed")
        else:
            self.step_fail(f"Expected is {expected} and Actual is {actual}, hence step failed")

    def check_element_is_enabled(self, element, msg=""):
        """
        This function verifies whether the given element is enabled
        :param element:
        :param msg:
        :return:
        """
        value = self.is_enabled(element)
        if value:
            self.step_pass(f"Element {msg} is enabled, as expected")
        else:
            self.step_fail(f"Element {msg} is disabled, where as it is expected to enabled")

    def check_element_is_disabled(self, element, msg=""):
        """
        This function verifies whether the given element is disabled
        :param element:
        :param msg:
        :return:
        """
        value = self.is_enabled(element)
        if not value:
            self.step_pass(f"Element {msg} is disabled, as expected")
        else:
            self.step_fail(f"Element {msg} is enabled, where as it is expected to enabled")

    def check_element_is_selected(self, element, msg=""):
        """
        This function verifies whether the given element is selected
        :param element:
        :param msg:
        :return:
        """
        value = self.is_selected(element)
        if value:
            self.step_pass(f"Element {msg} is selected, as expected")
        else:
            self.step_fail(f"Element {msg} is not selected, where as it is expected to selected")

    @allure.step("verify  login")
    def login(self, email_id, password):
        """
        Function to login to the application
        :param email_id:
        :param password:
        :return:
        """
        self.click_and_type(GC.XP_EMAIL, email_id, msg="User name")
        self.click_and_type(GC.XP_PASSWORD, password, msg="Password")
        self.click(GC.XP_SIGN_IN_BTN, msg="Login button")
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="spinner")
        self.accept_auth_consent_form()
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="spinner")
        # self.handle_recaptcha()
        self.enter_otp()

    @allure.step('accepting Authorization Consent form')
    def accept_auth_consent_form(self):
        self.wait_for_element(GC.XP_CONTAINS_TEXT.format(GC.AUTHORIZATION_CONSENT), msg="Authorization Consent form")
        self.click(GC.XP_CONTAINS_TEXT.format("CONTINUE"), msg="CONTINUE button in consent form")

    @allure.step('entering OTP')
    def enter_otp(self):
        self.wait_for_element(GC.XP_OTP_TEXT_FIELD, msg="OTP Entry screen")
        self.send_keys(GC.XP_OTP_TEXT_FIELD, OTP, msg="Entering OTP")
        self.click(GC.XP_CONTAINS_TEXT.format(GC.SUBMIT_BTN), msg="Clicking Submit btn")
        self.wait_for_element(GC.XP_CONTAINS_TEXT.format(GC.DASHBOARD), msg="dashboard")
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="spinner")

    @allure.step("verify select element from drop down")
    def select_element_from_drop_down(self, drop_down_element, element_to_be_selected):
        """
        This function selects elements from the dropdown
        :param drop_down_element:
        :param element_to_be_selected:
        :return:
        """
        self.wait_until_element_is_clickable(drop_down_element)
        self.click(drop_down_element, msg="drop down element")
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="spinner")
        self.click(element_to_be_selected, "drop down element")

    @allure.step("check contain in list")
    def check_contains_in_list(self, list, item_to_be_checked, msg=""):
        """
        Function to check whether the item is present in the given list
        :param list:
        :param item_to_be_checked:
        :param msg:
        :return:
        """
        if item_to_be_checked in list:
            self.step_pass(f"{msg} expected to be present in {list}")
        else:
            self.step_fail(f"{msg} is expected NOT to be present in {list}")

    @allure.step("check not contains in list ")
    def check_not_contains_in_list(self, list, item_to_be_checked, msg=""):
        """
        Function to check whether the item in NOT present in the given list
        :param list:
        :param item_to_be_checked:
        :param msg:
        :return:
        """
        if item_to_be_checked not in list:
            self.step_pass(f"{msg} expected NOT to be present in {list}")
        else:
            self.step_fail(f"{msg} is present in {list}")

    @allure.step("verify navigate to side drawer ")
    def navigate_via_side_drawer(self, page_name):
        """
        Function to navigate to respective page through side navigation drawer
        :param page_name:
        :return:
        """
        self.wait_until_element_is_clickable(GC.XP_SIDE_NAVIGATION_DRAWER_EXPAND)
        self.click(GC.XP_SIDE_NAVIGATION_DRAWER_EXPAND, msg="hamburger icon")
        self.click(GC.XP_SIDE_NAVIGATION_ITEM.format(page_name), msg="tabs")
        self.wait_until_element_is_clickable(GC.XP_SIDE_NAVIGATION_DRAWER_CLOSE)
        self.click(GC.XP_SIDE_NAVIGATION_DRAWER_CLOSE, msg="close hamburger icon")

    @allure.step("verify back navigation button ")
    def click_back_navigation_icon(self):
        """
        This function clicks on the back navigation icon present in the screen
        :return:
        """
        self.wait_until_element_is_clickable(GC.XP_BACK_ICON)
        self.click(GC.XP_BACK_ICON, msg="back icon")
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="spinner")

    @allure.step("verify date function")
    def date_function(self):
        """
        This function helps in selecting the date
        :return:
        """
        doc_date = date.today() + timedelta(days=1)
        document_date = doc_date.strftime('%d')
        k = int(document_date)
        if (document_date.__contains__("0")) and (k < 10):
            current_date = document_date.split("0")[1]
            self.click(DC.XP_DOCUMENT_DATE.format(current_date), msg="current date")
        else:
            self.click(DC.XP_DOCUMENT_DATE.format(document_date), msg="document date")

    @allure.step("logout")
    def logout(self):
        """
        This function to logout from application
        :return:
        """
        self.wait_until_element_is_clickable(GC.XP_USER_ICON)
        self.click(GC.XP_USER_ICON, msg="User icon")
        self.click(GC.XP_LOGOUT_BUTTON, msg="Logout Option")

    @allure.step("verify login by HA")
    def login_by_ha(self, user_name, password):
        """
        This function verify login by HA
        :param user_name:
        :param password:
        :return:
        """
        self.click_and_type(GC.XP_EMAIL, user_name, msg="User name")
        self.click_and_type(GC.XP_PASSWORD, password, msg="Password")
        self.click(GC.XP_SIGN_IN_BTN, msg="Login button")
        self.wait_for_element(GC.XP_CONTAINS_TEXT.format(GC.DASHBOARD), msg="Dashboard")

    @allure.step("verify document saved")
    def verify_document_confirmation(self):
        """
        This function verify document is saved
        :return:
        """
        self.wait_for_element(GC.XP_DOC_SAVE_SUCCESS_SNACK_BAR)
        self.check_element_is_displayed(GC.XP_DOC_SAVE_SUCCESS_SNACK_BAR, msg=" snack bar ")

    def wait_until_spinner_disappears(self):
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="spinner")

    def handle_recaptcha(self):
        time.sleep(5)
        frames = self.driver.find_elements_by_tag_name("iframe")
        self.driver.switch_to.frame(frames[2])
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "//*[@title ='Get an audio challenge' and @id='recaptcha-audio-button' and @tabindex = '1']").click()
        self.driver.switch_to.default_content()
        frames = self.driver.find_elements_by_tag_name("iframe")
        self.driver.switch_to.frame(frames[2])
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "//button[text()='PLAY']").click()
        src = self.driver.find_element_by_id("audio-source").get_attribute("src")
        urllib.request.urlretrieve(src, os.getcwd() + "\\sample.mp3")
        AudioSegment.ffmpeg = r'C:\Users\vyogasekar\Documents\softwares\ffmpeg\bin\ffmpeg.exe'
        AudioSegment.converter = r"C:\Users\vyogasekar\Documents\softwares\ffmpeg\bin\ffmpeg.exe"
        # subprocess.call(['ffmpeg','-i',os.getcwd()+"\\sample.mp3",os.getcwd()+"\\sample.wav"])
        sound = AudioSegment.from_mp3(os.getcwd() + "\\sample.mp3")
        sound.export(os.getcwd() + "\\sample.wav", format="wav")
        sample_audio = sr.AudioFile(os.getcwd() + "\\sample.wav")
        r = sr.Recognizer()
        with sample_audio as source:
            audio = r.record(source)

        key = r.recognize_google(audio)
        self.driver.find_element_by_id("audio-response").send_keys(key.lower())
        self.driver.find_element_by_id("audio-response").send_keys(keys.Keys.ENTER)

