import time
from datetime import timedelta, date

import allure

from base.basePage import BasePage
from constants import document_constants as DC
from constants import generic_constants as GC
from constants import project_constants as PC
from page.genericFunctions import GenericFunctions


class DocumentPage(BasePage):
    """
    This class of consists of reusable functions which can be used in Document creation and submission flow
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.gf = GenericFunctions(self.driver)

    @allure.step("Navigate to files page")
    def navigate_to_files_page(self):
        """
        Function to navigate to Document list page
        :return:
        """
        if self.is_displayed(PC.XP_START_GUIDE, msg="tool tip"):
            self.click(PC.XP_CLOSE_START_GUIDE, msg="tool tip close")
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="spinner")
        self.click(PC.XP_PROJECT_WORKSPACE_TAB.format(PC.TABS.get("FILES")), msg="files tab")
        self.wait_until_element_is_clickable(DC.XP_CREATE_BTN)

    @allure.step("Navigate to overview page")
    def navigate_to_overview_page(self):
        """
        Function to navigate to Project Overview page
        :return:
        """
        if self.is_displayed(PC.XP_START_GUIDE, msg="tool tip"):
            self.click(PC.XP_CLOSE_START_GUIDE, msg="tool tip close")
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="spinner")
        self.click(PC.XP_PROJECT_WORKSPACE_TAB.format(PC.TABS.get("OVERVIEW")), msg="overview tab")
        self.wait_for_element(GC.XP_CONTAINS_TEXT.format(PC.PRIORITY_TASKS), msg="priority task")

    @allure.step("Navigate to members page")
    def navigate_to_member_page(self):
        """
        Function to navigate to Member page
        :return:
        """
        if self.is_displayed(PC.XP_START_GUIDE, msg="tool tip"):
            self.click(PC.XP_CLOSE_START_GUIDE, msg="tool tip close")
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="spinner")
        self.click(PC.XP_PROJECT_WORKSPACE_TAB.format(PC.TABS.get("MEMBERS")), msg="members tab")
        self.wait_until_element_is_clickable(DC.XP_ADD_BTN)
        self.click(DC.XP_ADD_BTN, msg="add button")

    @allure.step("check create document button is displayed")
    def check_create_document_button_is_displayed(self):
        """
        This function checks create doc button is
        displayed in files page
        :return:
        """
        self.wait_for_element(DC.XP_CREATE_BTN)
        self.is_displayed(DC.XP_CREATE_BTN)

    @allure.step("check shortcut card disappear")
    def check_shortcut_card_disappear(self, shortcut_card):
        """
        This Function will check shortcut card disappear
        :param shortcut_card:
        :return:
        """
        time.sleep(2)
        self.navigate_to_overview_page()
        self.wait_until_element_disappear(GC.XP_SPINNER)
        self.gf.check_element_not_displayed(shortcut_card)

    @allure.step("check gsp package shortcut card displayed")
    def check_shortcut_card_displayed(self, shortcut_card):
        """
        This Function will check shortcut card displayed
        :param shortcut_card:
        :return:
        """
        time.sleep(2)
        self.navigate_to_overview_page()
        self.wait_until_element_disappear(GC.XP_SPINNER)
        self.gf.check_element_is_displayed(shortcut_card)

    @allure.step("click on shortcut cards ")
    def click_shortcut_cards(self, card_name, card_button):
        """
        This Function will click on shortcut cards
        :param card_name:
        :param card_button:
        :return:
        """
        time.sleep(3)
        self.move_to_element(card_name)
        self.click(card_button, msg="gsp shortcut complete button")
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="spinner")

    @allure.step("fill gsp additional info")
    def fill_gsp_overlay(self, document_domain, document_type, document_subtype, doc_name, doc_status):
        """
        This function will fill the gsp additional info
        :param document_domain:
        :param document_type:
        :param document_subtype:
        :param doc_name:
        :param doc_status:
        :return:
        """
        self.navigate_to_files_page()
        self.click(DC.XP_CREATE_BTN, msg="create button")
        time.sleep(2)
        self.enter_create_document_fields(document_domain, document_type, document_subtype)
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="spinner")
        self.gsp_create_additional_information(doc_name, doc_status)

    @allure.step("verify metadata fields")
    def verify_metadata_fields(self, xpath, actual):
        """
        Function to verify Meta data fields post document upload
        """
        self.wait_for_element(DC.XP_META_DOMAIN)
        metadata_field = self.get_text(xpath)
        self.gf.check_values(metadata_field, actual)

    @allure.step("create document")
    def create_document(self, document_domain, document_type, document_subtype, doc_name, doc_status):
        """
        This function create the Document by filling all mandatory
        fields in create new document overlay
        :param document_domain:
        :param document_type:
        :param document_subtype:
        :param doc_name:
        :param doc_status:
        :return:
        """
        self.fill_gsp_overlay(document_domain, document_type, document_subtype, doc_name, doc_status)
        self.click_on_create_gsp_button()
        self.wait_until_element_is_clickable(PC.XP_SNACKBAR_DISMISS_BTN)
        self.click(PC.XP_SNACKBAR_DISMISS_BTN)

    @allure.step("create document on click cancel button")
    def create_document_onclick_cancel_btn(self, document_domain, document_type, document_subtype, doc_name,
                                           doc_status):
        """
        This function create the Document by filling all mandatory
        fields in create new document overlay and click on cancel button
        :param document_domain:
        :param document_type:
        :param document_subtype:
        :param doc_name:
        :param doc_status:
        :return:
        """
        self.fill_gsp_overlay(document_domain, document_type, document_subtype, doc_name, doc_status)
        self.click(DC.XP_DOC_CANCEL_BTN)

    @allure.step("click on create gsp button in overlay")
    def click_on_create_gsp_button(self):
        """
        This function click on create gsp button in overlay
        :return:
        """
        self.wait_until_element_is_clickable(PC.XP_CP_BTN)
        self.click(PC.XP_CP_BTN, msg="create gsp button")

    @allure.step("Verify cancel create new files classification popup")
    def cancel_create_new_files_classification_overlay(self):
        self.navigate_to_files_page()
        self.click(DC.XP_CREATE_BTN, msg="create button")
        time.sleep(2)
        self.click(DC.XP_ADD_TEAM_CANCEL_BTN)
        self.wait_for_element(DC.XP_CREATE_BTN)
        self.is_displayed(DC.XP_CREATE_BTN)

    @allure.step("Enter create document fields")
    def enter_create_document_fields(self, document_domain, document_type, document_subtype):
        """
        This function fills the Create Document form
        :param document_domain:
        :param document_type:
        :param document_subtype:
        :return:
        """
        self.wait_until_element_is_clickable(DC.XP_DOCUMENT_DOMAIN_DD)
        self.gf.select_element_from_drop_down(DC.XP_DOCUMENT_DOMAIN_DD,
                                              GC.XP_CONTAINS_TEXT.format(document_domain))
        time.sleep(2)
        self.gf.select_element_from_drop_down(DC.XP_DOCUMENT_TYPE,
                                              GC.XP_CONTAINS_TEXT.format(document_type))
        time.sleep(2)
        self.gf.select_element_from_drop_down(DC.XP_DOCUMENT_SUB_TYPE_DD,
                                              GC.XP_CONTAINS_TEXT.format(document_subtype))

    @allure.step("Upload document")
    def upload_document(self):
        """
        This Function will upload the document in the create upload document pop-up
        :return:
        """
        self.send_keys(DC.XP_FILE_UPLOAD, DC.DOCUMENT_UPLOAD_FILE, msg="upload file")

    @allure.step("document action buttons")
    def document_actions(self, action):
        """
        This Function will click on document action buttons
        :return:
        :param action:
        """
        time.sleep(3)
        self.click(DC.XP_FILES_ACTION_BTN, msg="action icon")
        self.click(action, msg="action button")

    @allure.step("fill upload document drop down")
    def fill_upload_document_drop_down(self, document_domain, document_type, document_subtype):
        """
        This Function will fill the drop down while uploading document from document page
        :param document_domain:
        :param document_type:
        :param document_subtype:
        :return:
        """
        time.sleep(2)
        self.js_select_element_from_drop_down(DC.XP_DOCUMENT_DOMAIN_DD,
                                              GC.XP_CONTAINS_TEXT.format(document_domain))
        time.sleep(2)
        self.js_select_element_from_drop_down(DC.XP_DOCUMENT_TYPE,
                                              GC.XP_CONTAINS_TEXT.format(document_type))
        time.sleep(2)
        self.js_select_element_from_drop_down(DC.XP_DOCUMENT_SUB_TYPE_DD,
                                              GC.XP_CONTAINS_TEXT.format(document_subtype))

    @allure.step("upload document from files page")
    def upload_document_from_long_cut(self, domain, domain_type, subtype, doc_name, cfd, status):
        """
        This Function will allow to upload document from files tab
        :param domain:
        :param domain_type:
        :param subtype:
        :param doc_name:
        :param cfd:
        :param status:
        :return:
        """
        self.navigate_to_files_page()
        self.upload_document()
        self.wait_until_element_is_clickable(DC.XP_DOCUMENT_DOMAIN_DD)
        self.fill_upload_document_drop_down(domain, domain_type, subtype)
        self.upload_additional_information(doc_name, cfd, status)
        self.click(DC.XP_DOC_UPLOAD_BTN, msg="upload button")

    @allure.step("upload document from files page for task")
    def upload_document_task_for_ha(self, domain, domain_type, subtype, doc_name, cfd, status):
        """
        This Function will allow to upload document from files tab
        :param domain:
        :param domain_type:
        :param subtype:
        :param doc_name:
        :param cfd:
        :param status:
        :return:
        """
        self.upload_document()
        self.wait_until_element_is_clickable(DC.XP_DOCUMENT_DOMAIN_DD)
        self.fill_upload_document_drop_down(domain, domain_type, subtype)
        self.upload_additional_information(doc_name, cfd, status)
        self.click(DC.XP_DOC_UPLOAD_BTN, msg="upload button")

    @allure.step("move to filed and type")
    def move_to_field_and_type(self, xp_locator, value):
        """
        This Function scrolls to the text field web element, clicks on it  and send keys in the text field
        :param xp_locator:
        :param value:
        :return:
        """
        self.move_to_element(xp_locator)
        self.js_click(xp_locator)
        self.send_keys(xp_locator, value)

    @allure.step("move to field and click")
    def move_to_field_and_click(self, xp_locator):
        """
        This Function scrolls to the web element and clicks on it
        :param xp_locator:
        :return:
        """
        self.move_to_element(xp_locator)
        self.js_click(xp_locator)

    @allure.step("java script select element from drop down")
    def js_select_element_from_drop_down(self, drop_down_element, element_to_be_selected):
        """
        This function selects elements from the dropdown using js executor for clicking the web element
        :param drop_down_element:
        :param element_to_be_selected:
        :return:
        """
        self.wait_until_element_is_clickable(drop_down_element)
        self.js_click(drop_down_element)
        self.wait_until_element_is_clickable(element_to_be_selected)
        self.js_click(element_to_be_selected)

    @allure.step("java script select element from drop down")
    def java_script_select_element_from_drop_down(self, drop_down_element, element_to_be_selected):
        """
        This function selects elements from the dropdown using js executor for clicking the web element
        :param drop_down_element:
        :param element_to_be_selected:
        :return:
        """
        self.wait_until_element_is_clickable(drop_down_element)
        self.js_click(drop_down_element)
        self.js_click(element_to_be_selected)

    @allure.step("move to field and select")
    def move_to_field_and_select(self, xp_locator, element_to_select):
        """
        This function scrolls to the dropdown web element and selects from the list
        :param xp_locator:
        :param element_to_select:
        :return:
        """
        self.move_to_element(xp_locator)
        self.js_select_element_from_drop_down(xp_locator, element_to_select)

    @allure.step("gsp additional information")
    def gsp_create_additional_information(self, doc_name, doc_status):
        """
        This functions fills the additional information in create gsp
        :param doc_name:
        :param doc_status:
        :return:
        """
        self.wait_until_element_is_clickable(DC.XP_DOCUMENT_NAME)
        self.move_to_field_and_type(DC.XP_META_FIELD.format(DC.META_GSP.get("DOCUMENT_NAME")), doc_name)
        self.click(DC.XP_DOCUMENT_DATE_LOCATOR, msg="document date")
        self.gf.date_function()
        self.move_to_field_and_select(DC.XP_META_FIELD.format(DC.META_GSP.get("DOCUMENT_STATUS")),
                                      GC.XP_CONTAINS_TEXT.format(doc_status))

    @allure.step("upload additional information")
    def upload_additional_information(self, doc_name, cfd, doc_status):
        """
        This function fills the Meta data for document upload
        :param doc_name:
        :param doc_status:
        :param cfd:
        :return:
        """
        self.wait_until_element_is_clickable(DC.XP_DOCUMENT_NAME)
        time.sleep(3)
        self.move_to_field_and_type(DC.XP_META_FIELD.format(DC.META_UPLOAD_DOC.get("DOCUMENT_NAME")), doc_name)
        self.move_to_field_and_type(DC.XP_META_FIELD.format(DC.META_UPLOAD_DOC.get("CLEARED_FOR_DISTRIBUTION")), cfd)
        self.select_date_from_calendar()
        self.move_to_field_and_select(DC.XP_META_FIELD.format(DC.META_GSP.get("DOCUMENT_STATUS")),
                                      GC.XP_CONTAINS_TEXT.format(doc_status))
        self.wait_until_element_is_clickable(DC.XP_DOC_UPLOAD_BTN)

    @allure.step("add additional information ")
    def gsp_add_additional_information(self, doc_name, doc_status):
        """
        This function add the additional information in GSP page
        :param doc_name:
        :param doc_status:
        :return:
        """
        self.wait_until_element_is_clickable(DC.XP_ADDITIONAL_INFO_ICON)
        self.click(DC.XP_ADDITIONAL_INFO_ICON, msg="additional info button")
        self.wait_until_element_is_clickable(DC.XP_DOCUMENT_NAME)
        self.clear(DC.XP_ADDITIONAL_DOC_FIELD)
        self.move_to_field_and_type(DC.XP_META_FIELD.format(DC.META_GSP.get("DOCUMENT_NAME")), doc_name)
        self.click(DC.XP_DOCUMENT_DATE_LOCATOR, msg="document date")
        self.gf.date_function()
        self.move_to_field_and_select(DC.XP_META_FIELD.format(DC.META_GSP.get("DOCUMENT_STATUS")),
                                      GC.XP_CONTAINS_TEXT.format(doc_status))

    def gsp_add_additional_info_by_clicking_cancel_btn(self, doc_name, doc_status):
        self.gsp_add_additional_information(doc_name, doc_status)
        self.wait_until_element_is_clickable(DC.XP_ADDITIONAL_DOC_CANCEL_BTN)
        self.click(DC.XP_ADDITIONAL_DOC_CANCEL_BTN, msg="additional info save button")
        self.wait_until_element_is_clickable(DC.XP_EDIT_POPUP_SAVE_BTN)
        self.click(DC.XP_EDIT_POPUP_SAVE_BTN, msg="Save button")

    @allure.step("click on additional info save button")
    def click_on_additional_info_save_btn(self):
        """
        This function click on additional info save button
        in health authority form
        :return:
        """
        self.wait_until_element_is_clickable(DC.XP_ADDITIONAL_INFO_SAVE_BTN)
        self.click(DC.XP_ADDITIONAL_INFO_SAVE_BTN, msg="additional info save button")

    @allure.step("click on download button in health")
    def click_on_download_btn_in_ha_form(self):
        """
        This function click on download button in health
        authority form
        :return:
        """
        self.wait_until_element_is_clickable(DC.XP_DOWNLOAD_ICON_GSP_PAGE)
        self.click(DC.XP_DOWNLOAD_ICON_GSP_PAGE, msg="download icon gsp")

    @allure.step("add health authority")
    def add_health_authority(self, health_authority, application_type, proposed_indication, application_number,
                             submission_number, contact_information):
        """
        Function to add participating health authority
        :param health_authority:
        :param application_type:
        :param proposed_indication:
        :param application_number:
        :param submission_number:
        :param contact_information:
        :return:
        """
        self.wait_for_element(DC.XP_GSP_TOOL_TIP, msg="GSP tool tip")
        self.move_to_element(DC.XP_HA_ADD_BTN, msg="HA add button")
        self.wait_until_element_is_clickable(DC.XP_HA_ADD_BTN)
        self.click(DC.XP_HA_ADD_BTN, msg="add HA button")
        self.move_to_field_and_select(DC.XP_GSP_FORM_HEALTH_AUTHORITY_DD,
                                      GC.XP_CONTAINS_TEXT.format(health_authority))
        self.move_to_field_and_select(DC.XP_GSP_FORM_APPLICATION_TYPE_DD,
                                      GC.XP_CONTAINS_TEXT.format(application_type))
        self.move_to_field_and_type(DC.XP_META_FIELD.format(DC.GSP_ELECTRONIC_FORM.get("PROPOSED_INDICATION")),
                                    proposed_indication)
        self.move_to_field_and_type(DC.XP_META_FIELD.format(DC.GSP_ELECTRONIC_FORM.get("APPLICATION_NUMBER")),
                                    application_number)
        self.move_to_field_and_type(DC.XP_META_FIELD.format(DC.GSP_ELECTRONIC_FORM.get("SUBMISSION_NUMBER")),
                                    submission_number)
        self.gf.move_to_element(DC.XP_GSP_PLANNED_SUBMISSION_DATE)
        doc_date = date.today() + timedelta(days=1)
        document_date = doc_date.strftime('%d')
        self.js_click(DC.XP_GSP_PLANNED_SUBMISSION_DATE, msg="submission plan date")
        self.click(DC.XP_DOCUMENT_DATE.format(document_date), msg="document date")
        time.sleep(2)
        self.move_to_field_and_type(DC.XP_META_FIELD.format(DC.GSP_ELECTRONIC_FORM.get("CONTACT_INFORMATION")),
                                    contact_information)
        self.click(DC.XP_HA_OVERLAY_ADD_BTN, msg="HA popup add button")
        self.wait_for_element(DC.XP_SAVED_SUCCESS_MSG, msg="HA success msg")
        self.is_displayed(DC.XP_SAVED_SUCCESS_MSG, msg="saved success message")
        self.click(PC.XP_SNACKBAR_DISMISS_BTN, msg="Snack bar dismiss button")

    @allure.step("click on health authority additional")
    def click_on_health_authority_additional_info_icon(self):
        """
        This function click on health authority additional
        icon
        :return:
        """
        self.gf.wait_until_element_disappear(GC.XP_SPINNER, msg="Spinner")
        self.wait_until_element_is_clickable(DC.XP_ADDITIONAL_INFO_ICON)
        self.click(DC.XP_ADDITIONAL_INFO_ICON, msg="additional info button")
        value1 = self.gf.get_text(DC.XP_ADDITIONAL_DOC_STATUS)
        self.gf.check_values(value1, DC.DOCUMENT_STATUS["STATUS_2"])

    @allure.step("select date from calendar")
    def select_date_from_calendar(self):
        """
        This function fill the document date fields in the application
        :return:
        """
        doc_date = date.today() + timedelta(days=1)
        document_date = doc_date.strftime('%d')
        self.gf.move_to_element(DC.XP_DOCUMENT_DATE_LOCATOR)
        self.click(DC.XP_DOCUMENT_DATE_LOCATOR, msg="date locator")
        self.click(DC.XP_DOCUMENT_DATE.format(document_date), msg="document date")

    @allure.step("verifies document creation")
    def verify_document_creation(self, document_subtype):
        """
        Function to verify the Name and last Modified
        fields of the newly created GSP document in Document list screen
        :param:document_subtype:
        :return:
        """
        time.sleep(2)
        self.wait_for_element(DC.XP_DOC_NAME)
        document_subtype1 = self.get_text(DC.XP_DOC_NAME)
        self.gf.check_values(document_subtype, document_subtype1)
        modified_date = date.today().strftime("%d-%m-%Y")
        last_modified = self.get_text(DC.XP_LAST_MODIFIED)
        self.gf.check_values(modified_date, last_modified)

    @allure.step("add team from member tab")
    def add_team_member_from_members_page(self, role, domain):
        """
        This function will add team members from members page
        :param role:
        :param domain:
        :return:
        """
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="spinner")
        self.js_select_element_from_drop_down(DC.XP_ADD_TEAM_ROLE_DD,
                                              GC.XP_CONTAINS_TEXT.format(role))
        self.wait_until_element_is_clickable(DC.XP_ADD_TEAM_DOMAIN_DD)
        self.js_select_element_from_drop_down(DC.XP_ADD_TEAM_DOMAIN_DD,
                                              GC.XP_CONTAINS_TEXT.format(domain))
        self.wait_until_element_is_clickable(DC.XP_ADD_TEAM_MEMBERS_DD)
        self.click_and_type(DC.XP_SEARCH_MEMBER_BOX, DC.ADD_USERS["USER3"], msg="search box")
        self.click(DC.XP_SELECT_RECIPIENT, msg="select recipient")

    @allure.step("click on add team from member button")
    def click_add_team_member_button(self):
        """
        Function to click on add team from member button
        :return:
        """
        self.js_click(DC.XP_TEAM_MEMBER_ADD_BTN, msg="team member add button")

    @allure.step("delete member from list")
    def delete_member_from_list(self):
        """
        Function to delete member from list
        :return:
        """
        self.click(DC.XP_GSP_CLOSE_TOOL_TIP, msg="delete team member")

    @allure.step("verify fields for send document")
    def verify_fields_for_send_document_flow(self, workflow_type):
        """
        Function to verify the fields for send document flow
        :param workflow_type
        :return:
        """
        self.click(DC.XP_CHECKBOX, msg="checkbox")
        self.click(DC.XP_SEND_FILES, msg="send file button")
        self.wait_until_element_is_clickable(DC.XP_LAUNCH_WORKFLOW_TYPES.format(workflow_type))
        self.click(DC.XP_LAUNCH_WORKFLOW_TYPES.format(workflow_type), msg="launch workflow 1")
        self.wait_until_element_is_clickable(DC.XP_SEARCH_RECIPIENTS_BOX)
        self.gf.check_element_is_displayed(DC.XP_SEARCH_RECIPIENTS_BOX)
        self.gf.check_element_is_displayed(DC.XP_ADD_TEAM_CANCEL_BTN)
        filename = self.get_text(DC.XP_PREPOPULATED_GSP)
        self.gf.check_values(filename, DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])

    @allure.step("verify gsp data fields ")
    def verify_gsp_data_fields(self):
        """
        Function to verify the gsp data fields
        :return:
        """
        self.wait_for_element(DC.XP_GSP_SPONSOR_NAME, msg="sponsor name")
        self.gf.check_element_is_displayed(DC.XP_GSP_SPONSOR_NAME, msg="sponsor name")
        self.gf.check_element_is_displayed(DC.XP_GSP_FORM_TITLE, msg="form title")
        self.gf.check_element_is_displayed(DC.XP_APPLICATION_FORM, msg="application form")
        self.gf.check_element_is_displayed(DC.XP_PROPOSED_FIELDS, msg="proposed fields")

    @allure.step("verify add team member is displayed")
    def verify_team_member_added_and_displayed(self, name):
        """
        This function will verify the added team members are displayed
        :param name:
        :return:
        """
        self.wait_until_element_disappear(GC.XP_SPINNER)
        self.wait_for_element(DC.XP_ADDED_TEAM_NAME, msg="team member name")
        name1 = self.get_web_elements(DC.XP_ADDED_TEAM_NAME)
        for i in name1:
            text = i.text
            if text == name:
                self.is_displayed(
                    "(//tbody/tr//*[contains(text(),'" + text + "')])[1]//..//..//following-sibling::td[1]",
                    msg="email verify")

    # sprint 5

    @allure.step("fill send files overlay")
    def fill_send_files_overlay(self, ha_name, optional_msg):
        """
        This function fills the send files overlay
        :param ha_name:
        :param optional_msg:
        :return:
        """
        self.wait_until_element_is_clickable(DC.XP_SEARCH_RECIPIENTS_BOX)
        self.click(DC.XP_SEARCH_RECIPIENTS_BOX, msg="search recipients")
        self.send_keys(DC.XP_SEARCH_RECIPIENTS_BOX, ha_name, msg="ha recipient name")
        self.click(DC.XP_SELECT_RECIPIENTS, msg="select recipients")
        self.fill_optional_msg_in_send_files_overlay(optional_msg)
        self.click(DC.XP_SEND_BTN, msg="send button")

    @allure.step("fill send files optional message")
    def fill_optional_msg_in_send_files_overlay(self, optional_msg):
        """
        This function fill the optional message in send files overlay
        :param optional_msg:
        :return:
        """
        self.js_click(DC.XP_SEND_FILE_POPUP_TITLE)
        time.sleep(2)
        self.send_keys(DC.XP_MESSAGE_OPTIONAL, optional_msg, msg="optional message")

    @allure.step("send files to host HA")
    def send_files(self, ha_name, optional_msg):
        """
        This function create a task to recipients
        :param ha_name:
        :param optional_msg:
        :return:
        """
        self.fill_send_files_overlay(ha_name, optional_msg)
        self.wait_for_element(DC.XP_SEND_FILES_POPUP_CARD)
        self.click(DC.XP_SEND_BTN, msg="send button")
        time.sleep(2)

    @allure.step("create gsp for task ")
    def create_gsp_for_task(self, document_domain, document_type, document_subtype, doc_name, doc_status):
        """
        This function to create the gsp for task
        :param document_domain:
        :param document_type:
        :param document_subtype:
        :param doc_name:
        :param doc_status:
        :return:
        """
        self.create_document(document_domain, document_type, document_subtype, doc_name, doc_status)

    @allure.step("send files to HA recipients")
    def send_files_to_recipients(self, ha_name, optional_msg, workflow_type):
        """
        This function to verify send files to HA recipients
        :param ha_name:
        :param optional_msg:
        :param workflow_type:
        :return:
        """
        self.select_documents_and_send_to_ha(DC.XP_LAUNCH_WORKFLOW_TYPES.format(workflow_type))
        self.gf.check_element_is_disabled(DC.XP_SEND_BTN, msg="Send button")
        self.send_files(ha_name, optional_msg)

    @allure.step("select documents to send to HA")
    def select_documents_and_send_to_ha(self, workflow_type):
        """
        This function fill send files popup
        :param workflow_type:
        :return:
        """
        self.wait_until_element_is_clickable(DC.XP_CHECKBOX)
        self.click(DC.XP_CHECKBOX, msg="select all checkbox")
        self.wait_until_element_is_clickable(DC.XP_SEND_FILES)
        self.click(DC.XP_SEND_FILES, msg="send files")
        self.wait_until_element_is_clickable(workflow_type)
        self.click(workflow_type, msg="launch work flow 1")
        self.wait_until_element_disappear(GC.XP_SPINNER, msg="spinner")

    @allure.step("verify send recipient is displayed")
    def verify_send_recipient_is_displayed(self):
        """
        This function checks send recipient is displayed in send file overlay
        :return:
        """
        self.gf.wait_until_element_is_clickable(DC.XP_SEARCH_RECIPIENTS_BOX)
        self.gf.check_element_is_displayed(DC.XP_SEARCH_RECIPIENTS_BOX)

    @allure.step("verify send file popup is displayed")
    def verify_send_file_popup_displayed(self, workflow_type, ha_name, optional_msg):
        """
        This function verify whether send file confirmation popup is displayed
        :param ha_name:
        :param optional_msg:
        :param workflow_type
        :return:
        """
        self.select_documents_and_send_to_ha(DC.XP_LAUNCH_WORKFLOW_TYPES.format(workflow_type))
        self.fill_send_files_overlay(ha_name, optional_msg)
        self.wait_for_element(DC.XP_SEND_FILES_POPUP_CARD, msg="send files popup")
        self.is_displayed(DC.XP_SEND_FILES_POPUP_CARD, msg="send files popup card")

    @allure.step("click on send file popup cancel button")
    def click_on_send_file_popup_cancel_button(self, workflow_type, ha_name, optional_msg):
        """
        This function click on send file popup cancel button
        :param workflow_type:
        :param ha_name:
        :param optional_msg:
        :return:
        """
        self.select_documents_and_send_to_ha(DC.XP_LAUNCH_WORKFLOW_TYPES.format(workflow_type))
        self.fill_send_files_overlay(ha_name, optional_msg)
        self.wait_for_element(DC.XP_SEND_FILES_POPUP_CARD)
        self.click(DC.XP_CANCEL_BUTTON_IN_SEND_FILE_POPUP, msg="cancel button")
        self.is_displayed(DC.XP_SEND_FILE_POPUP_TITLE, msg="send file popup title")

    @allure.step("verify add or remove multiple files")
    def remove_multiple_files_in_send_files(self, workflow_type):
        """
        This functions remove a documents in send files popup
        :param workflow_type
        :return:
        """
        self.gf.verify_document_confirmation()
        time.sleep(2)
        self.select_documents_and_send_to_ha(DC.XP_LAUNCH_WORKFLOW_TYPES.format(workflow_type))
        self.wait_until_element_is_clickable(DC.XP_TOPLINE_DOC_REMOVE_BTN)
        self.click(DC.XP_TOPLINE_DOC_REMOVE_BTN, msg="top_line remove button")
        self.click(DC.XP_CANCEL_BUTTON_IN_SEND_FILE_POPUP, msg="cancel button in send file popup")

    @allure.step("checks   tool tip is displayed")
    def check_send_files_tool_tip_is_displayed_without_selecting_files(self):
        """
        This function verify whether tool tip is displaying on clicking on send files btn
        without selecting documents
        :return:
        """
        self.wait_until_element_is_clickable(DC.XP_SEND_FILES)
        self.click(DC.XP_SEND_FILES, msg="send file button")
        self.gf.check_element_is_displayed(DC.XP_SELECT_FILES_TOOLTIP)

    @allure.step("edit added health authority")
    def edit_the_added_health_authority(self, proposed_indication):
        """
        This function edits the added health authority
        :param:proposed_indication
        :return:
        """
        self.move_to_element(DC.XP_EDIT_HA_PROPOSED_TEXT, msg="HA proposed indication text")
        time.sleep(2)
        self.click(DC.XP_EDIT_HA_ICON, msg="edit ha icon")
        self.clear(DC.XP_EDIT_HA_PROPOSED_FILED)
        self.click_and_type(DC.XP_EDIT_HA_PROPOSED_FILED, proposed_indication, msg="ha edit field")
        self.click(DC.XP_EDIT_HA_SAVE_BTN, msg="HA save button")
        edited_text = self.get_text(DC.XP_EDIT_HA_PROPOSED_TEXT)
        self.gf.check_values(edited_text, "Edited")
        self.gf.verify_document_confirmation()

    @allure.step("verify task creation")
    def verify_task_creation(self):
        """
        This function to verify the success message after file submission
        :return:
        """
        self.wait_for_element(DC.XP_TASK_CREATION_SNACKBAR)
        self.gf.check_element_is_displayed(DC.XP_TASK_CREATION_SNACKBAR)
        self.wait_until_element_disappear(DC.XP_TASK_CREATION_SNACKBAR, msg="Snack bar")
