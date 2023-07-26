import pytest
from base.basePage import BasePage
from constants import document_constants as DC
from constants import project_constants as PC
from constants import task_invitation_constants as TC
from page.document_page import DocumentPage
from page.genericFunctions import GenericFunctions
from page.project_page import ProjectPage
from page.task_invitation_page import TaskAndInvitationPage
from utils.environment_variables import EMAIL_ID, PASSWORD, HOST_HA_NAME_1, HOST_HA_EMAIL, HOST_HA_PASSWORD, \
    HOST_HA_NAME_2, RECIPIENT_URL, RECIPIENT_ID


@pytest.mark.usefixtures("setup", "before_test", "launch_application")
class TestTaskAndInvitationCreation:

    @pytest.fixture(autouse=True)
    def class_objects(self):
        self.gf = GenericFunctions(self.driver)
        self.pp = ProjectPage(self.driver)
        self.dp = DocumentPage(self.driver)
        self.tp = TaskAndInvitationPage(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.fixture()
    def login(self):
        """
        Function to login to the application
        """
        self.gf.login(EMAIL_ID, PASSWORD)

    @pytest.fixture()
    def create_project(self, login):
        """
        Function create a project
        :param login:
        :return:
        """
        self.pp.create_project(PC.PRODUCT_CODE["PRODUCT_A"], PC.REVIEW_TYPE["PROJECT_ORBIS"],
                               PC.REGULATORY_EVENT_NAME["EVENT_1"])

    def test_view_task_list_in_task_inbox(self, create_project):
        """
        Test case to Verify the task details in post file submission
        AUD - 299
        :param create_project:
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_1,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.view_task_status(TC.STATUS["STATUS1"])

    def test_view_task_inbox_from_side_bar(self, login):
        """
        Test case to Verify the task details in post file submission
        AUD - 300
        :param login:
        :return:
        """
        self.tp.view_task_inbox_from_side_bar()

    def test_verify_sent_date_is_sorted_in_descending_order(self, login):
        """
        This function Verify that by default tasks
        are sorted based on “Sent Date” in descending order.
        AUD-299
        :param login:
        :return:
        """
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.verify_default_sort_for_send_date()

    def test_view_visual_indication_unread_task(self):
        """
        Test case to Verify view visual indication of unread tasks, by creating tasks and validating whether the
        count gets increased
        AUD - 299
        AUD - 300
        :return:
        """
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        initial_count = self.tp.get_task_count()
        self.gf.logout()
        self.gf.login(EMAIL_ID, PASSWORD)
        self.pp.create_project(PC.PRODUCT_CODE["PRODUCT_A"], PC.REVIEW_TYPE["PROJECT_ORBIS"],
                               PC.REGULATORY_EVENT_NAME["EVENT_1"])
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_1,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        increased_count = self.tp.get_task_count()
        self.gf.check_values(initial_count + 1, increased_count)
        self.dp.wait_for_element(TC.XP_UNREAD_TASK_COUNT, msg="Unread tasks")
        self.dp.is_displayed(TC.XP_UNREAD_TASK_COUNT, msg="Unread tasks")

    def test_visual_indication_disappear(self, create_project):
        """
        Test case to Verify visual indicator disappears once the task is viewed
        AUD - 299
        AUD - 300
        :param create_project:
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_1,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.wait_for_element(TC.XP_UNREAD_TASK_COUNT, msg="Unread task count")
        self.tp.check_task_count_has_decreased()

    def test_to_verify_task_details_sidebar_fields(self, create_project):
        """
        This testcase verifies the task details fields in popup
        AUD-301
        :param create_project:
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_1,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.click_on_task_list()
        self.tp.verify_the_fields_in_task_detail_popup()

    @pytest.mark.smoke
    def test_verify_sent_invitation_form_is_displayed(self, create_project):
        """
        This testcase verify sent invitation form is displayed after clicking
        on create invitation button
        AUD-303
        :param create_project:
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_1,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.click_on_task_list()
        self.tp.verify_sent_invitation_form_is_displayed()

    def test_verify_error_msg_is_displayed_in_decline_gsp_popup_without_giving_reason(self, create_project):
        """
        This test case verify error msg is displayed without giving a reason on decline GSP popup
        AUD-816
        :param create_project:
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_1,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.click_on_task_list()
        self.tp.decline_gsp_task_error_msg()

    @pytest.mark.smoke
    def test_verify_decline_gsp_task(self, create_project):
        """
        This test case verify user can decline GSP task
        AUD-816
        :param create_project:
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_1,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.click_on_task_list()
        self.tp.decline_gsp_task()

    @pytest.mark.smoke
    def test_verify_create_invitation_from_members_tab(self, create_project):
        """
        This test case Verify that user is able to invite Health Authorities by filling
        Invitation form with valid details.
        AUD-304
        :param create_project:
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_1,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.click_on_task_list()
        self.tp.verify_sent_invitation_form_is_displayed()
        self.tp.verify_create_invitation_from_members_tab()

    def test_verify_create_invitation(self, create_project):
        """
        This test case verify create invitation form
        AUD-727
        :param create_project:
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_1,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.click_on_task_list()
        self.tp.verify_sent_invitation_form_is_displayed()
        self.tp.fill_send_invitation_form()

    def test_verify_ha_pre_populated_from_gsp(self, create_project):
        """
        This test case Verify that user is able to invite Health Authorities by filling
        Invitation form with valid details and Verify Recipient
        Health Authorities is pre populated from GSP
        AUD-304
        :param create_project:
        :return:
        """
        self.dp.click_shortcut_cards(PC.XP_GSP_CARD, PC.XP_GSP_COMPLETE_BTN)
        self.dp.add_health_authority(health_authority=DC.HEALTH_AUTHORITY.get("DEMO"),
                                     application_type=DC.APPLICATION_TYPE.get("APP_TYPE_1"),
                                     proposed_indication="test",
                                     application_number="001", submission_number="1",
                                     contact_information="7708538922")
        self.gf.click_back_navigation_icon()
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_1,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.refresh()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.click_on_task_list()
        self.tp.verify_sent_invitation_form_is_displayed()
        self.tp.verify_ha_pre_populated_from_gsp()

    @pytest.mark.smoke
    def test_verify_create_invitation_by_accepting_task(self, create_project):
        """
        This test case Verify that the user accepts the task assigned to them
        AUD-727
        :param create_project:
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_1,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.view_task_status(TC.STATUS["STATUS1"])
        self.tp.click_on_task_list()
        self.tp.verify_sent_invitation_form_is_displayed()
        self.tp.verify_task_status(TC.STATUS["STATUS3"])

    # sprint-6
    @pytest.mark.smoke
    def test_verify_fields_in_files_page_post_gsp_submission(self, create_project):
        """
        This function Verify that user is not allowed to add files to another workflow,
        once user send document on a workflow.
        AUD-1111
        :param create_project:
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.send_files_to_recipients(HOST_HA_NAME_2,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.tp.verify_fields_in_files_page_post_gsp_submission()

    @pytest.mark.smoke
    def test_verify_fields_in_gsp_view_page_post_gsp_submission(self, create_project):
        """
        This function Verify that user is not allowed to add files to another workflow,
        once user send document on a workflow.
        AUD-1111
        :param create_project:
        :return:
        """
        self.dp.click_shortcut_cards(PC.XP_GSP_CARD, PC.XP_GSP_COMPLETE_BTN)
        self.dp.add_health_authority(health_authority=DC.HEALTH_AUTHORITY.get("DEMO"),
                                     application_type=DC.APPLICATION_TYPE.get("APP_TYPE_1"),
                                     proposed_indication="test",
                                     application_number="001", submission_number="1",
                                     contact_information="7708538922")
        self.dp.gsp_add_additional_information(doc_name="add_info",
                                               doc_status=DC.DOCUMENT_STATUS.get("STATUS_2"))
        self.gf.click_back_navigation_icon()
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_2,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.dp.document_actions(DC.XP_VIEW_BTN)
        self.tp.verify_fields_in_gsp_view_page_post_gsp_submission()

    def test_verify_navigate_to_members_tab_upon_clicking_do_not_save_button(self, create_project):
        """
        Verify that updates on the invitation are discarded and user is redirected back to Members Tab by
        confirming the cancellation action.
        AUD-999
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.send_files_to_recipients(HOST_HA_NAME_2,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.click_on_task_list()
        self.tp.verify_sent_invitation_form_is_displayed()
        self.tp.fill_send_invitation_form()
        self.tp.verify_sava_invitation_overlay_displayed_upon_cancel()
        self.tp.verify_navigate_to_create_invitation_page_on_clicking_save_button()
        self.tp.verify_navigate_to_members_tab_upon_clicking_do_not_save_button()

    def test_verify_user_navigates_to_create_invitation_page_upon_clicking_shortcut_card(self, create_project):
        """
        Verify that user is able to see the Send invitations shortcut card in Workspace Overview Tab
        Verify that user is redirected to create invitation page by clicking on button displayed in
        Send invitation shortcut card.
        AUD-302
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.send_files_to_recipients(HOST_HA_NAME_2,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.click_on_task_list()
        self.tp.verify_sent_invitation_form_is_displayed()
        self.tp.click(TC.XP_MEMBERS_BAR, msg="Members bar")
        self.dp.check_shortcut_card_displayed(shortcut_card=TC.XP_SEND_INVITATION_SHORTCUT)
        self.dp.click_shortcut_cards(card_name=TC.XP_SEND_INVITATION_SHORTCUT,
                                     card_button=TC.XP_CREATE_INVITATION_BTN_ON_SHORTCUT)
        self.dp.is_displayed(TC.XP_SENT_INVITATION_FORM_HEADER, msg="Sent invitation form header")

    @pytest.mark.smoke
    def test_verify_send_invitation_shortcut_card_disappear_upon_sending_task(self, create_project):
        """
        Verify that "send invitation" shortcut card no longer appears on my Project Workspace Overview
        Tab once after sending invitation successfully.
        AUD-302
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.send_files_to_recipients(HOST_HA_NAME_2,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.click_on_task_list()
        self.tp.verify_sent_invitation_form_is_displayed()
        self.tp.fill_send_invitation_form()
        self.tp.verify_send_invitation()
        self.dp.check_shortcut_card_disappear(shortcut_card=TC.XP_SEND_INVITATION_SHORTCUT)

    @pytest.mark.smoke
    def test_verify_save_invitation(self, create_project):
        """
        Verify that user is able to Save the Invitation to a Health Authority
        AUD-1000
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.send_files_to_recipients(HOST_HA_NAME_2,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.click_on_task_list()
        self.tp.verify_sent_invitation_form_is_displayed()
        self.tp.fill_send_invitation_form()
        self.tp.verify_save_invitation()

    def test_verify_edit_draft_invitation_form(self, create_project):
        """
        Verify that user is able to continue editing an invitation to invite Health Authority, which was saved as Draft
        AUD-806
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.send_files_to_recipients(HOST_HA_NAME_2,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.click_on_task_list()
        self.tp.verify_sent_invitation_form_is_displayed()
        self.tp.fill_send_invitation_form()
        self.tp.verify_save_invitation()
        self.tp.verify_edit_draft_invitation_form()
        self.tp.verify_send_invitation()

    def test_verify_browser_is_not_auto_filling_the_login_credentials(self, login):
        """
        Verify that browser is not auto filling the login credentials on the accumulus login page
        AUD-27
        :return:
        """
        self.gf.logout()
        self.tp.verify_browser_is_not_auto_filling_login_credentials()

    def test_verify_confirmation_popup_in_send_invitation_page(self, create_project, HA_RECIPIENT_NAME_2=None):
        """
        This test case verify confirmation popup is displayed in send invitation screen
        AUD-305
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_2,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.click_on_task_list()
        self.tp.verify_sent_invitation_form_is_displayed()
        self.tp.fill_send_invitation_form()
        self.tp.verify_confirmation_popup_is_displayed_in_send_invitation_page()
        self.tp.verify_cancel_send_invitation_form()

    @pytest.mark.smoke
    def test_verify_after_sending_invitation_confirmation_msg_is_displayed(self, create_project):
        """
        This test case verify confirmation popup is displayed in send
        invitation screen
        AUD-305
        :return:
        """
        self.dp.create_gsp_for_task(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                    DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                    DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                    doc_name="document1",
                                    doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_2,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()
        self.gf.logout()
        self.gf.login(HOST_HA_EMAIL, HOST_HA_PASSWORD)
        self.tp.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.tp.click_on_task_list()
        self.tp.verify_sent_invitation_form_is_displayed()
        self.tp.fill_send_invitation_form()
        self.tp.verify_send_invitation()
