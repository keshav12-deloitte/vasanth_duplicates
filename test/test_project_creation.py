import pytest

from constants import generic_constants as GC
from constants import project_constants as PC
from page.genericFunctions import GenericFunctions
from page.project_page import ProjectPage
from utils.environment_variables import EMAIL_ID, PASSWORD


@pytest.mark.usefixtures("setup", "before_test", "launch_application")
class TestProjectCreation:
    """
    This Test suite consists of Test cases related to the following user stories :
    AUD - 100, 38, 101, 128 and 131
    """

    @pytest.fixture(autouse=True)
    def class_objects(self):
        self.gf = GenericFunctions(self.driver)
        self.pp = ProjectPage(self.driver)

    @pytest.fixture()
    def login(self):
        """
        Function to login to the application
        """
        self.gf.login(EMAIL_ID, PASSWORD)

    @pytest.fixture()
    def create_project(self, login):
        """
        Function to create a new page
        :param login:
        :return:
        Test case to verify creating a new project : AUD-131
        """
        self.pp.create_project(PC.PRODUCT_CODE["PRODUCT_B"], PC.REVIEW_TYPE["PROJECT_ORBIS"],
                               PC.REGULATORY_EVENT_NAME["EVENT_1"])

    def test_default_landing_screen_post_login(self, login):
        """
        Test case to check the default landing screen and Create project button
        AUD-38(1,2)
        AUD-100(1,2)
        :param login:
        """
        self.pp.check_elements_post_login()

    def test_elements_in_create_project_overlay(self, login):
        """
        Test case to check the contents in create project overlay
        AUD - 101(1,2,3,4,5,6,7,8,9,10)
        :param login:
        """
        self.pp.check_elements_in_create_project_overlay()
        self.pp.click_cp_overlay_cancel_button()

    def test_verify_project_overlay_indication_error_msg(self, login):
        """
        Test case to verify indication filed error msg
        :param login:
        :return:
        """
        self.pp.open_create_project_overlay()
        self.pp.check_error_msg_indication_field()

    def test_check_content_in_loader_popup(self, login):
        """
        Test case to check the contents in the Creating Project Loader
        AUD-128(1,2,3,4,5,6,7)
        :param login:
        """
        self.pp.check_creating_project_loader_popup_text(PC.PRODUCT_CODE["PRODUCT_A"],
                                                         PC.REVIEW_TYPE["PROJECT_ORBIS"],
                                                         PC.REGULATORY_EVENT_NAME["EVENT_1"])

    @pytest.mark.smoke
    def test_create_new_project(self, login):
        """
        Test case to verify creating a new project
        AUD-131(1,2,3,4,5,6)
        :param login:
        """
        self.pp.create_project(PC.PRODUCT_CODE["PRODUCT_A"],
                               PC.REVIEW_TYPE["PROJECT_ORBIS"],
                               PC.REGULATORY_EVENT_NAME["EVENT_1"])
        self.pp.check_elements_in_project_workspace(PC.PRODUCT_CODE["PRODUCT_A"],
                                                    PC.REGULATORY_EVENT_NAME["EVENT_1"])

    def test_project_displayed_in_dashboard(self, create_project):
        """
        Test case to check whether the created project is displayed
        AUD-845
        :param create_project:
        :return:
        """
        self.gf.navigate_via_side_drawer(GC.DASHBOARD)
        self.pp.check_created_project_is_displayed_in_dashboard(PC.PROJECT_NAME["PRODUCT-B"],
                                                                PC.REVIEW_TYPE["PROJECT_ORBIS"])

    def test_verify_onclick_projects_navigating_to_project_workspace(self, create_project):
        """
        Test cast to check whether onclick on created project is navigating to project workspace
        AUD-845
        :param create_project:
        :return:
        """
        self.gf.navigate_via_side_drawer(GC.DASHBOARD)
        self.pp.check_onclick_project_navigating_project_workspace()
