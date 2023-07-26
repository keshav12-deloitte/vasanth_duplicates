import time

import allure

from base.basePage import BasePage
from constants import generic_constants as GC
from constants import task_invitation_constants as TC
from constants import document_constants as DC
from page.document_page import DocumentPage
from page.genericFunctions import GenericFunctions


class TaskAndInvitationPage(BasePage):
    """
    This class of consists of reusable functions which can be used in task and invitation creation
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.gf = GenericFunctions(self.driver)
        self.dp = DocumentPage(self.driver)

    @allure.step(" view task list in task inbox page")
    def view_task_status(self, task_status):
        """
        This function helps in viewing the list of tasks in task inbox
        :param task_status:
        :return:
        """
        self.wait_for_element(TC.XP_TASK_STATUS)
        status = self.get_text(TC.XP_TASK_STATUS)
        self.gf.check_values(task_status, status)

    @allure.step("view task inbox from side bar")
    def view_task_inbox_from_side_bar(self):
        """
        This function helps to verify view task inbox from side bar
        :return:
        """
        self.wait_until_element_is_clickable(GC.XP_SIDE_NAVIGATION_DRAWER_EXPAND)
        self.click(GC.XP_SIDE_NAVIGATION_DRAWER_EXPAND, msg="navigation drawer")
        self.gf.check_element_is_displayed(TC.XP_TASK_BAR, msg="Task bar from side bar")

    @allure.step("get task count")
    def get_task_count(self):
        """
        This function verify task count
        :return:
        """
        try:
            xyz = self.get_text(TC.XP_UNREAD_TASK_COUNT)
            count = int(xyz)
            return count
        except:
            count = 0
            return count

    @allure.step("navigate to side bar")
    def navigation_through_side_bar(self, sidebar_tab):
        """
        This function helps to verify navigate to side bar
        :param sidebar_tab:
        :return:
        """
        self.wait_until_element_is_clickable(GC.XP_SIDE_NAVIGATION_DRAWER_EXPAND)
        self.click(GC.XP_SIDE_NAVIGATION_DRAWER_EXPAND, msg="hamburger icon")
        self.click(sidebar_tab, msg="side bar")
        self.gf.wait_until_spinner_disappears()
        self.wait_for_element(TC.XP_TASK_PAGE_HEADER, msg="task page header")
        self.wait_until_element_is_clickable(GC.XP_SIDE_NAVIGATION_DRAWER_CLOSE)
        self.click(GC.XP_SIDE_NAVIGATION_DRAWER_CLOSE, msg="close hamburger icon")

    @allure.step("checks visual indicator count is decreased")
    def check_task_count_has_decreased(self):
        initial_count = self.get_task_count()
        time.sleep(2)
        self.dp.click(TC.XP_TASK_LIST, msg="Task list")
        time.sleep(4)
        decreased_count = self.get_task_count()
        self.gf.check_values(initial_count - 1, decreased_count)

    @allure.step("visual indicator is disappeared")
    def visual_indication_disappear(self):
        """
        This function helps in verify that the visual indicator is disappeared
        upon viewing task
        """
        self.js_click(TC.XP_TASK_LIST, msg="Task list")
        self.wait_for_element(TC.XP_CREATE_INVITATION_BTN)
        self.gf.check_element_not_displayed(TC.XP_UNREAD_TASK_COUNT, msg="Unread task count")

    @allure.step("verify default sort for send date")
    def verify_default_sort_for_send_date(self):
        """
        This function helps to verify default sort for send date
        upon viewing task
        """
        self.gf.wait_until_spinner_disappears()
        self.wait_for_element(TC.XP_TASK_PAGE_HEADER, msg="task page header")
        self.gf.check_element_is_displayed(TC.XP_SENT_DATE_SORTED, msg="send date sorted")

    @allure.step("verify task details fields are displayed")
    def verify_the_fields_in_task_detail_popup(self):
        """
        This function verify the fields in task detail pop-up
        :return:
        """
        self.wait_for_element(TC.XP_TASK_DETAILS_PROJECT_NAME, msg="Task detail project name")
        self.gf.check_element_is_displayed(TC.XP_TASK_DETAILS_PROJECT_NAME, msg="project name")
        self.gf.check_element_is_displayed(TC.XP_TASK_DETAILS_WORKFLOW, msg="Work flow")
        self.gf.check_element_is_displayed(TC.XP_TASK_DETAILS_MESSAGE, msg="optional message ")
        msg = self.get_text(TC.XP_TASK_DETAILS_MESSAGE)
        self.gf.check_values(msg, TC.OPTIONAL_MSG)
        self.gf.check_element_is_displayed(TC.XP_TASK_DETAILS_SENT_DATE, msg="sent date")
        self.gf.check_element_is_displayed(TC.XP_TASK_DETAILS_ATTACHMENTS, msg="Attachments")
        self.gf.check_element_is_displayed(TC.XP_CREATE_INVITATION_BTN, msg="create invitation button")
        self.gf.check_element_is_displayed(TC.XP_DECLINE_GSP_BTN, msg="decline GSP button")

    @allure.step("click on task list")
    def click_on_task_list(self):
        """
        This function  click on task list
        :return:
        """
        self.gf.wait_until_spinner_disappears()
        self.wait_for_element(TC.XP_TASK_PAGE_HEADER, msg="task page header")
        self.wait_until_element_is_clickable(TC.XP_TASK_LIST)
        self.dp.click(TC.XP_TASK_LIST, msg="task list")

    @allure.step("verify sent invitation form is displayed")
    def verify_sent_invitation_form_is_displayed(self):
        """
        This function verify that the sent invitation form is displayed
        :return:
        """
        self.wait_until_element_is_clickable(TC.XP_CREATE_INVITATION_BTN)
        self.dp.click(TC.XP_CREATE_INVITATION_BTN, msg="create invitation button")
        self.gf.wait_until_spinner_disappears()
        self.wait_for_element(TC.XP_SENT_INVITATION_FORM_HEADER, msg="Sent invitation form header")
        self.gf.check_element_is_displayed(TC.XP_SENT_INVITATION_FORM_HEADER, msg="Sent invitation form header")

    @allure.step("verify create invitation from members tab")
    def verify_create_invitation_from_members_tab(self):
        """
        This function verify that the User is able to create the invitation from members tab
        :return:
        """
        self.wait_until_element_is_clickable(TC.XP_MEMBERS_BAR)
        self.dp.click(TC.XP_MEMBERS_BAR, msg="Members bar")
        self.dp.wait_until_element_is_clickable(TC.XP_CREATE_INVITATION_BTN)
        self.dp.click(TC.XP_CREATE_INVITATION_BTN, msg="Create invitation button")
        self.fill_send_invitation_form()

    @allure.step("fill send invitation form")
    def fill_send_invitation_form(self):
        """
        This function fill the send invitation form
        :return:
        """
        time.sleep(2)
        self.dp.click(TC.XP_HA_RECIPIENT_BOX, msg="HA Recipient")
        self.wait_until_element_is_clickable(TC.XP_SELECT_HA_RECIPIENTS)
        self.dp.click(TC.XP_SELECT_HA_RECIPIENTS, msg="Select HA recipient")
        self.dp.wait_until_element_is_clickable(TC.XP_SENT_INVITATION_FORM_HEADER)
        self.dp.click(TC.XP_SENT_INVITATION_FORM_HEADER, msg="Invitation Header")
        # self.dp.click(TC.XP_SIDEBAR_CLOSE_BTN, msg="Side bar close button")
        self.wait_until_element_is_clickable(TC.XP_RESPONSE_DUE_DATE)
        self.click(TC.XP_RESPONSE_DUE_DATE, msg="Response due date")
        self.gf.date_function()
        self.dp.send_keys(TC.XP_OPTIONAL_MSG, "test", msg="Optional message")
        self.gf.check_element_is_displayed(TC.XP_SENT_INVITATION_FORM_HEADER, msg="Invitation Header")
        time.sleep(2)

    @allure.step("click send invitation button")
    def verify_click_send_invitation_button(self):
        """
        This function to verify click send invitation button
        :return:
        """
        self.wait_until_element_is_clickable(TC.XP_SEND_INVITATION_SEND_BTN)
        self.click(TC.XP_SEND_INVITATION_SEND_BTN, msg="send button")

    @allure.step("send invitation confirmation popup")
    def verify_confirmation_popup_is_displayed_in_send_invitation_page(self):
        """
        This function verify confirmation popup is displayed in
        send invitation page
        :return:
        """
        self.verify_click_send_invitation_button()
        self.gf.check_element_is_displayed(TC.XP_SEND_INVITATION_CONFIRMATION_POPUP)

    @allure.step("send invitation confirmation msg is displayed")
    def verify_confirmation_msg_is_displayed_onclick_send_button(self):
        """
        This function will verify confirmation snack bar is displayed
        :return:
        """
        self.verify_confirmation_popup_is_displayed_in_send_invitation_page()
        self.click(DC.XP_SEND_BTN, msg="send button")
        self.gf.check_element_is_displayed(TC.XP_SEND_INVITATION_SNACK_BAR_MSG)

    @allure.step("click on save in send invitation")
    def click_save_in_send_invitation_screen(self):
        """
        This function click on save button in send invitation screen
        :return:
        """
        time.sleep(2)
        self.wait_until_element_is_clickable(TC.XP_SEND_INVITATION_SAVE_BTN)
        self.click(TC.XP_SEND_INVITATION_SAVE_BTN, msg="save button")
        self.gf.wait_until_spinner_disappears()

    @allure.step("verify user able to edit the invitation")
    def verify_user_can_continue_to_edit_the_invitation(self):
        """
        This function verify user can continue to edit the invitation
        :return:
        """
        self.wait_until_element_is_clickable(TC.XP_CONTINUE_EDITING_BTN)
        self.click(TC.XP_CONTINUE_EDITING_BTN, msg="continue editing")
        self.gf.wait_until_spinner_disappears()
        self.gf.check_element_is_displayed(TC.OPTIONAL_MSG, msg="Optional message")

    def verify_decline_button_is_disabled(self, sidebar_tab):
        """
        This function verify decline button is disabled after accepting
        the task
        :return:
        """
        self.navigation_through_side_bar(sidebar_tab)
        self.click_on_task_list()
        self.gf.check_element_is_disabled(TC.XP_DECLINE_GSP_BTN)

    @allure.step("verify create invitation page pre populated fields")
    def verify_ha_pre_populated_from_gsp(self):
        """
        This function Verify Recipient Health Authorities is pre populated from GSP
        :return:
        """
        time.sleep(3)
        self.gf.check_element_is_displayed(TC.XP_PREPOPULATED_HA, msg="HA prepopulated")
        self.gf.check_element_is_displayed(TC.XP_SPONSOR_NAME, msg="Sponsor name")
        self.gf.check_element_is_displayed(TC.XP_ATTACHMENTS, msg="Attachments")
        self.gf.check_element_is_displayed(TC.XP_SEND_BTN, msg="Send button")

    @allure.step("decline task verify error message")
    def decline_gsp_task_error_msg(self):
        """
        This function verify error msg is displayed onclick submit button
        in decline gsp without giving a reason
        :return:
        """
        self.dp.wait_for_element(TC.XP_DECLINE_GSP_BTN)
        self.click(TC.XP_DECLINE_GSP_BTN, msg="decline btn")
        self.wait_until_element_is_clickable(TC.XP_DECLINE_GSP_SUBMIT_BTN)
        self.dp.click(TC.XP_DECLINE_GSP_SUBMIT_BTN, msg="decline GSP submit button")
        self.gf.check_element_is_displayed(TC.XP_DECLINE_GSP_ERROR_MSG, msg="decline gsp error")

    @allure.step("decline task by HA")
    def decline_gsp_task(self):
        """
        This function verify task declined by host HA
        :return:
        """
        self.dp.wait_for_element(TC.XP_DECLINE_GSP_BTN)
        self.click(TC.XP_DECLINE_GSP_BTN, msg="decline button")
        self.wait_until_element_is_clickable(TC.XP_DECLINE_GSP_SUBMIT_BTN)
        self.dp.click(TC.XP_DECLINE_GSP_SUBMIT_BTN, msg="decline reason submit button")
        self.send_keys(TC.XP_DECLINE_REASON_FIELD, "NA", msg="decline gsp reason")
        self.click(TC.XP_DECLINE_GSP_SUBMIT_BTN, msg="decline reason submit button")

    @allure.step("verify task is accepted by HA")
    def verify_task_status(self, task_status):
        """
        This function verify the task status
        :param task_status:
        :return:
        """
        time.sleep(2)
        self.navigation_through_side_bar(TC.XP_TASK_TAB)
        self.view_task_status(task_status)

    @allure.step("verify fields in files tab post gsp submission")
    def verify_fields_in_files_page_post_gsp_submission(self):
        """
        This function verify fields in files tab post gsp submission
        :return:
        """
        time.sleep(2)
        self.gf.check_element_is_disabled(DC.XP_CHECKBOX, msg="Check box")
        self.click(DC.XP_FILES_ACTION_BTN, msg="Action button")
        self.gf.check_element_is_disabled(DC.XP_DELETE_BTN, msg="Delete button")
        self.dp.click(DC.XP_DOWNLOAD_BTN)
        self.gf.verify_document_confirmation()

    @allure.step("verify fields in gsp view page post gsp submission")
    def verify_fields_in_gsp_view_page_post_gsp_submission(self):
        """
        This function to verify fields in gsp view page post gsp submission
        :return:
        """
        self.wait_until_element_is_clickable(DC.XP_ADDITIONAL_INFO_ICON)
        self.click(DC.XP_ADDITIONAL_INFO_ICON, msg="Additional info icon")
        self.gf.check_element_is_disabled(DC.XP_ADDITIONAL_INFO_SAVE_BTN, msg="Additional info save button")

    @allure.step("verify save invitation overlay is displayed upon clicking on cancel button")
    def verify_sava_invitation_overlay_displayed_upon_cancel(self):
        """
        This function to verify save invitation overlay is displayed upon clicking on cancel button
        :return:
        """
        self.verify_click_cancel_button_in_create_invitation_screen()
        self.gf.check_element_is_displayed(TC.XP_YES_BTN, msg="Yes button")
        self.gf.check_element_is_displayed(TC.XP_NO_BTN, msg="No button")

    @allure.step("verify user navigates to members tab upon clicking dont save button in save invitation overlay")
    def verify_navigate_to_members_tab_upon_clicking_do_not_save_button(self):
        """
        This function to verify user navigates to members tab upon clicking dont save button in save invitation overlay
        :return:
        """
        self.verify_click_cancel_button_in_create_invitation_screen()
        self.wait_until_element_is_clickable(TC.XP_YES_BTN)
        self.click(TC.XP_YES_BTN, msg="Do not save button")
        self.gf.wait_until_spinner_disappears()
        self.gf.check_element_is_displayed(TC.XP_CREATE_INVITATION_BTN, msg="Creation button")

    @allure.step("verify user navigates to create invitation page on clicking save button in save invitation overlay")
    def verify_navigate_to_create_invitation_page_on_clicking_save_button(self):
        """
        This function to verify user navigates to create invitation page on clicking save button in save
        invitation overlay
        :return:
        """
        self.wait_until_element_is_clickable(TC.XP_NO_BTN)
        self.click(TC.XP_NO_BTN, msg="save button")
        self.gf.check_element_is_displayed(TC.XP_SENT_INVITATION_FORM_HEADER, msg="invitation page header")

    @allure.step("Verify that user is redirected to create invitation page by clicking Send invitation shortcut card.")
    def verify_user_access_link_sent_after_team_member_being_added(self):
        """
        This function fill the send invitation form
        :return:
        """
        self.dp.click(TC.XP_CREATE_INVITATION_BTN_ON_SHORTCUT, msg="Create button on shortcut card")

    @allure.step("Verify send invitation.")
    def verify_send_invitation(self):
        """
        This function to verify send invitation
        :return:
        """
        self.verify_click_send_invitation_button()
        self.dp.click(DC.XP_SEND_BTN, msg="Send button in confirmation page")
        self.dp.verify_task_creation()
        time.sleep(2)

    @allure.step("Verify save invitation form")
    def verify_save_invitation(self):
        """
        This function to verify save invitation form
        :return:
        """
        self.dp.wait_until_element_is_clickable(DC.XP_ADDITIONAL_INFO_SAVE_BTN)
        self.dp.click(DC.XP_ADDITIONAL_INFO_SAVE_BTN, msg="save button in invitation screen")
        self.dp.verify_task_creation()
        self.gf.check_element_is_displayed(TC.XP_CONTINUE_EDITING_BTN, msg="continue editing button")

    @allure.step("Verify edit invitation form")
    def verify_edit_draft_invitation_form(self):
        """
        This function to verify edit invitation form
        :return:
        """
        self.dp.wait_until_element_is_clickable(TC.XP_CONTINUE_EDITING_BTN)
        self.dp.click(TC.XP_CONTINUE_EDITING_BTN, msg="Continue edit button")
        self.dp.wait_until_element_is_clickable(TC.XP_OPTIONAL_MSG)
        self.dp.clear(TC.XP_OPTIONAL_MSG)
        self.dp.send_keys(TC.XP_OPTIONAL_MSG, "Arjun", msg="Optional message")

    @allure.step("Verify cancel send invitation form")
    def verify_cancel_send_invitation_form(self):
        """
        This function to verify cancel send invitation form
        :return:
        """
        self.dp.wait_until_element_is_clickable(DC.XP_CANCEL_BUTTON_IN_SEND_FILE_POPUP)
        self.dp.click(DC.XP_CANCEL_BUTTON_IN_SEND_FILE_POPUP, msg="cancel send button")
        self.gf.check_element_is_displayed(TC.XP_SENT_INVITATION_FORM_HEADER, msg="task page header")

    @allure.step("Verify that browser is not auto filling the login credentials on the accumulus login page")
    def verify_browser_is_not_auto_filling_login_credentials(self):
        """
        This function to verify edit invitation form
        :return:
        """
        text_username = self.get_text(GC.XP_EMAIL)
        text_password = self.get_text(GC.XP_PASSWORD)
        self.gf.check_values(text_username, '')
        self.gf.check_values(text_password, '')

    @allure.step("send invitation confirmation popup")
    def verify_confirmation_popup_is_displayed_in_send_invitation_page(self):
        """
        This function verify confirmation popup is displayed in
        send invitation page
        :return:
        """
        self.wait_until_element_is_clickable(TC.XP_SEND_INVITATION_SEND_BTN)
        self.click(TC.XP_SEND_INVITATION_SEND_BTN, msg="send button")
        self.gf.check_element_is_displayed(TC.XP_SEND_INVITATION_CONFIRMATION_POPUP)

    @allure.step("send invitation confirmation msg is displayed")
    def verify_confirmation_msg_is_displayed_onclick_send_button(self):
        """
        This function will verify confirmation snack bar is displayed
        :return:
        """
        self.verify_confirmation_popup_is_displayed_in_send_invitation_page()
        self.click(DC.XP_SEND_BTN, msg="send button")
        self.gf.check_element_is_displayed(TC.XP_SEND_INVITATION_SNACK_BAR_MSG)

    @allure.step("click cancel button in create invitation screen")
    def verify_click_cancel_button_in_create_invitation_screen(self):
        """
        This function will verify confirmation snack bar is displayed
        :return:
        """
        self.wait_until_element_is_clickable(DC.XP_ADDITIONAL_DOC_CANCEL_BTN)
        self.click(DC.XP_ADDITIONAL_DOC_CANCEL_BTN, msg="Additional info cancel button")
