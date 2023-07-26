import random
import string
import time
from datetime import datetime

import allure

from base.basePage import BasePage
from constants import generic_constants as GC
from constants import project_constants as PC
from page.genericFunctions import GenericFunctions
from utils.logs import logger


class ProjectPage(BasePage):
    """
    This class of consists of reusable functions which can be used in Project creation flow
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.gf = GenericFunctions(self.driver)

    @allure.step("verify elements in post login ")
    def check_elements_post_login(self):
        """
        This functions checks the elements in landing screen post login
        :return:
        """
        self.gf.check_element_is_displayed(GC.XP_TEXT.format(GC.DASHBOARD), msg="Dashboard")
        time.sleep(2)
        self.gf.check_element_is_displayed(GC.XP_CREATE_NEW_PROJECT, msg="Create new project icon")

    @allure.step("create project overlay")
    def open_create_project_overlay(self):
        """
        This function open the Create Project Overlay
        :return:
        """
        self.wait_until_element_is_clickable(GC.XP_CREATE_NEW_PROJECT)
        self.click(GC.XP_CREATE_NEW_PROJECT, msg="Create new project icon")
        self.wait_for_element(PC.XP_CP_BTN, msg="Create button")
        self.gf.check_element_is_displayed(PC.XP_CP_OVERLAY_HEADER, msg="Overlay header")
        logger.info("Create Project Overlay has been opened")

    @allure.step("click cancel button in create project overlay ")
    def click_cp_overlay_cancel_button(self):
        """
        This function clicks cancel button in Create new Project overlay
        :return:
        """
        self.click(PC.XP_CANCEL_BTN, msg="Cancel button")

    @allure.step("click create button in create project overlay")
    def click_cp_overlay_create_button(self):
        """
        This function clicks Create Project button in Create New Project overlay
        :return:
        """
        self.click(PC.XP_CP_BTN, msg="Create button")

    @allure.step("check elements in create project overlay")
    def check_elements_in_create_project_overlay(self):
        """
        This function checks the presence of all the elements in the Create Project Overlay
        :return:
        """
        self.open_create_project_overlay()
        self.wait_for_element(PC.XP_CP_OVERLAY_HEADER, msg="Overlay header")
        title = self.get_text(PC.XP_CP_OVERLAY_HEADER)
        self.gf.check_values(PC.CP_OVERLAY_HEADER, title)
        self.gf.check_element_is_displayed(PC.XP_PRODUCT_CODE_DD, msg="Product code")
        self.gf.check_element_is_displayed(PC.XP_PROJECT_REVIEW_TYPE_DD, msg="Project review type")
        self.gf.check_element_is_displayed(PC.XP_REGULATORY_EVENT_DD, msg=" Regulatory event")
        self.gf.is_displayed(PC.XP_CANCEL_BTN, msg="cancel button")
        self.wait_for_element(PC.XP_CP_BTN, msg="Create button")

    @allure.step("indication field error message")
    def check_error_msg_indication_field(self):
        """
        This function checks the display of error message when user enters more than 56 char in indication field
        :return:
        """
        self.wait_for_element(PC.XP_INDICATION_FIELD, msg="Indication")
        indication = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(57))
        self.gf.click_and_type(PC.XP_INDICATION_FIELD, indication, msg="Indication")
        self.gf.check_element_is_displayed(GC.XP_TEXT.format(PC.INDICATION_ERROR_MSG), msg="Indication error message")
        self.gf.clear(PC.XP_INDICATION_FIELD)
        self.click(PC.XP_CANCEL_BTN, msg="Cancel button")

    @allure.step("fill indication filed ")
    def fill_indication_field(self):
        indication = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        self.gf.click_and_type(PC.XP_INDICATION_FIELD, indication, msg="Indication field")

    @allure.step("fill create project form")
    def fill_create_project_form(self, product_name, review_type, regulatory):
        """
        This function fills the Create Project form
        :param product_name:
        :param review_type:
        :param regulatory:
        :return:
        """
        self.gf.select_element_from_drop_down(PC.XP_PRODUCT_CODE_DD,
                                              GC.XP_DROP_DOWN_OPTION.format(product_name))
        self.gf.select_element_from_drop_down(PC.XP_PROJECT_REVIEW_TYPE_DD,
                                              GC.XP_DROP_DOWN_OPTION.format(review_type))
        self.gf.select_element_from_drop_down(PC.XP_REGULATORY_EVENT_DD,
                                              GC.XP_DROP_DOWN_OPTION.format(regulatory))
        time.sleep(2)
        self.fill_indication_field()

    @allure.step("creation of project")
    def create_project(self, product_name, review_type, regulatory):
        """
        This function create the project by filling all mandatory fields in create project overlay
        :param product_name:
        :param review_type:
        :param regulatory:
        :return:
        """
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="Spinner")
        self.open_create_project_overlay()
        self.wait_until_element_is_clickable(PC.XP_PRODUCT_CODE_DD)
        self.fill_create_project_form(product_name, review_type, regulatory)
        self.click(PC.XP_CP_BTN, msg="Create button")
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="Spinner")
        self.click(PC.XP_SNACKBAR_DISMISS_BTN)
        self.wait_for_element(PC.XP_GSP_CARD, msg="GSP card")

    @allure.step("check project name")
    def check_project_name(self, product_name, regulatory_event):
        """
        This function checks name of the project based on product_name and regulatory event
        :param product_name:
        :param regulatory_event:
        :return:
        """
        date = datetime.now()
        month = date.strftime("%b")
        year = date.strftime("%Y")
        expected = f"{product_name}-{regulatory_event}-{month}-{year}"
        actual = self.get_text(PC.XP_PROJECT_NAME)
        self.gf.check_values(expected, actual)

    @allure.step("check elements in project workspace")
    def check_elements_in_project_workspace(self, product_name, regulatory_event):
        """
        This function checks the elements in the Project workspace once the project gets created
        :param product_name:
        :param regulatory_event:
        :return:
        """
        self.wait_for_element(PC.XP_GSP_CARD, msg="GSP card")
        self.wait_until_element_is_clickable(PC.XP_CLOSE_START_GUIDE)
        self.gf.check_element_is_displayed(PC.XP_START_GUIDE, msg="Start guide")
        self.gf.click(PC.XP_CLOSE_START_GUIDE, msg="Start guide")
        self.check_project_name(product_name, regulatory_event)

    @allure.step("verify get text from create project popup")
    def get_text_from_creating_project_popup(self, product_name, review_type, regulatory):
        """
        This function gets the array of texts from Creating project loader popup
        :param product_name:
        :param review_type:
        :param regulatory:
        :return:
        """
        text = []
        self.open_create_project_overlay()
        self.fill_create_project_form(product_name, review_type, regulatory)
        self.click(PC.XP_CP_BTN, msg="Create button")
        web_elements = self.get_web_elements(PC.XP_LOADER_POPUP_TEXTS)
        for web_element in web_elements:
            text.append(self.get_text_from_webelement(web_element))
        return text

    @allure.step("check create project loader popup text ")
    def check_creating_project_loader_popup_text(self, product_name, review_type, regulatory):
        """
        This function checks the texts displaying in the creating project loader popup
        :param product_name:
        :param review_type:
        :param regulatory:
        :return:
        """
        self.get_text_from_creating_project_popup(product_name, review_type, regulatory)
        confirmation_msg = self.get_text(PC.XP_LOADER_POPUP_MSG)
        self.gf.check_values(PC.LOADER_POP_MSG, confirmation_msg)

    @allure.step("check created project is displayed in dashboard")
    def check_created_project_is_displayed_in_dashboard(self, project_name, review_type):
        """
        This function checks created project is displayed in dashboard
        :param project_name:
        :param review_type:
        :return:
        """
        self.refresh()
        self.wait_until_element_disappear(GC.XP_SPINNER)
        project1 = self.get_text(PC.XP_PRODUCT_NAME)
        self.gf.check_values(project_name, project1)
        review1 = self.get_text(PC.XP_PROJECT_REVIEW_TYPE)
        self.gf.check_values(review_type, review1)

    @allure.step("verify onclick project navigating to workspace")
    def check_onclick_project_navigating_project_workspace(self):
        """
        This function check onclick on project its navigating to project workspace
        :param:
        :return:
        """
        self.refresh()
        self.wait_until_element_disappear(GC.XP_SPINNER)
        self.click(PC.XP_PRODUCT_NAME, msg="Product name")
