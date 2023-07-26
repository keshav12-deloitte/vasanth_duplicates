import time

import pytest

from constants import document_constants as DC
from constants import project_constants as PC
from constants import task_invitation_constants as TC
from page.document_page import DocumentPage
from page.genericFunctions import GenericFunctions
from page.project_page import ProjectPage
from utils.environment_variables import EMAIL_ID, PASSWORD, HOST_HA_NAME_1


@pytest.mark.usefixtures("setup", "before_test", "launch_application")
class TestDocumentCreation:

    @pytest.fixture(autouse=True)
    def class_objects(self):
        self.gf = GenericFunctions(self.driver)
        self.pp = ProjectPage(self.driver)
        self.dp = DocumentPage(self.driver)

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

    @pytest.mark.smoke
    def test_create_new_document_save(self, create_project):
        """
        Test case to Verify creating  Global Submission Plan document,
        using "Create" button in Documents screen
        AUD-152 [AC:1,2,3,4,5,6,7]
        :param create_project:
        :return:
        """
        self.dp.create_document(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                doc_name="document1",
                                doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])

    @pytest.mark.smoke
    def test_creation_of_gsp_through_shortcut_on_save(self, create_project):
        """
        Test Case to Verify creating Global Submission Plan document through shortcut (adding HA)
        AUD-43  [AC:1,2,3,4,5,6,7,8,9,10]
        :param create_project:
        :return:
        """
        self.dp.click_shortcut_cards(PC.XP_GSP_CARD, PC.XP_GSP_COMPLETE_BTN)
        self.dp.add_health_authority(health_authority=DC.HEALTH_AUTHORITY.get("DEMO"),
                                     application_type=DC.APPLICATION_TYPE.get("APP_TYPE_1"),
                                     proposed_indication="test", application_number="001",
                                     submission_number="1",
                                     contact_information="7708538922")
        self.gf.click_back_navigation_icon()
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])

    def test_gsp_short_cut_disappear(self, create_project):
        """
        Test case to Verify that the GSP short cut card disappears,
        once GSP document created from shortcut card
        AUD-43
        :param create_project:
        :return:
        """
        self.dp.click_shortcut_cards(PC.XP_GSP_CARD, PC.XP_GSP_COMPLETE_BTN)
        self.gf.click_back_navigation_icon()
        self.dp.check_shortcut_card_disappear(PC.XP_GSP_CARD)

    def test_verify_additional_info_pre_populated_fields(self, create_project):
        """
        Test case to verify additional info  pre populated fields
        :param create_project:
        :return:
        """
        self.dp.fill_gsp_overlay(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                 DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                 DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                 doc_name="document1",
                                 doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_metadata_fields(DC.XP_META_DOMAIN, DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"])
        self.dp.verify_metadata_fields(DC.XP_META_DOC_TYPE, DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"])
        self.dp.verify_metadata_fields(DC.XP_META_DOC_SUBTYPE, DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"])

    def test_cancel_overlay_gsp_from_document_tab(self, create_project):
        """
        Test case to Verify creating GSP document, click cancel button
        in overlay recreated the GSP from create button
        AUD-152
        :param:create_project:
        :return:
        """
        self.dp.create_document_onclick_cancel_btn(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                                   DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                                   DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                                   doc_name="document1",
                                                   doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.check_create_document_button_is_displayed()

    def test_cancel_create_new_files_classification_overlay(self, create_project):
        """
        Verify that Create new pop-up is getting closed when user clicks on "Cancel" button in "Create new file
         Classification" pop-up and no document is created.
        AUD-152
        :param:create_project:
        :return:
        """
        self.dp.cancel_create_new_files_classification_overlay()

    def test_create_gsp_from_document_tab_shortcut_disappear(self, create_project):
        """
        Test case to Verify that the GSP short cut card disappears,
        once GSP document created from documents tab
        AUD-152/AUD-43
        :param:create_project:
        :return:
        """
        self.dp.create_document(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                doc_name="document1",
                                doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.check_shortcut_card_disappear(PC.XP_GSP_CARD)

    @pytest.mark.smoke
    def test_create_gsp_by_adding_health_authority(self, create_project):
        """
        Test case to add health authority for created GSP
        :param create_project:
        :return:
        """
        self.dp.create_document(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                doc_name="document1",
                                doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.document_actions(DC.XP_VIEW_BTN)
        self.dp.add_health_authority(health_authority=DC.HEALTH_AUTHORITY.get("DEMO"),
                                     application_type=DC.APPLICATION_TYPE.get("APP_TYPE_1"),
                                     proposed_indication="test", application_number="001",
                                     submission_number="1",
                                     contact_information="7708538922")
        self.gf.click_back_navigation_icon()
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])

    def test_verify_gsp_data_fields(self, create_project):
        """
        Test case to Verify GSP fields for created document
        AUD-158(1,2,3)
        API : AUD-390
        """
        self.dp.click_shortcut_cards(PC.XP_GSP_CARD, PC.XP_GSP_COMPLETE_BTN)
        self.dp.verify_gsp_data_fields()

    def test_to_add_gsp_additional_info(self, create_project):
        """
        Test case to add GSP additional information to the created GSP
        AUD-156(1,2,3)
        API : AUD-390
        """
        self.dp.click_shortcut_cards(PC.XP_GSP_CARD, PC.XP_GSP_COMPLETE_BTN)
        self.dp.gsp_add_additional_information(doc_name="add_info",
                                               doc_status=DC.DOCUMENT_STATUS.get("STATUS_2"))
        self.dp.click_on_additional_info_save_btn()
        self.gf.click_back_navigation_icon()
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])

    def test_upload_document_from_local_machine(self, create_project):
        """
        Test upload document from local machine
        :param create_project:
        :return:
        """
        self.dp.navigate_to_files_page()
        self.dp.upload_document()

    @pytest.mark.smoke
    def test_upload_document_from_files_page(self, create_project):
        """
        Test case to upload document flow from files tab
        (AUD-56) [AC:1,2,3,4,5]
        :param create_project:
        :return:
        """
        self.dp.upload_document_from_long_cut(DC.DOCUMENT_DOMAIN["SUPPORTING_MATERIAL"],
                                              DC.DOCUMENT_TYPE["SUPPORTING_EVIDENCE"],
                                              DC.DOCUMENT_SUBTYPE["TOPLINE_RESULTS"],
                                              DC.META_UPLOAD_DOC["DOCUMENT_NAME"],
                                              DC.META_UPLOAD_DOC["CLEARED_FOR_DISTRIBUTION"],
                                              DC.DOCUMENT_STATUS["STATUS_1"])
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["TOPLINE_RESULTS"])

    def test_supporting_material_short_cut_disappear(self, create_project):
        """
        Test case to check that the Supporting material
        short cut card disappears upon upload of document
        (AUD-168) [AC:13]
        :param create_project:
        :return:
        """
        self.dp.upload_document_from_long_cut(DC.DOCUMENT_DOMAIN["SUPPORTING_MATERIAL"],
                                              DC.DOCUMENT_TYPE["SUPPORTING_EVIDENCE"],
                                              DC.DOCUMENT_SUBTYPE["TOPLINE_RESULTS"],
                                              DC.META_UPLOAD_DOC["DOCUMENT_NAME"],
                                              DC.META_UPLOAD_DOC["CLEARED_FOR_DISTRIBUTION"],
                                              DC.DOCUMENT_STATUS["STATUS_1"])
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["TOPLINE_RESULTS"])
        self.dp.check_shortcut_card_disappear(PC.XP_SUPPORTING_MATERIAL_CARD)

    def test_add_team_member_from_member_page(self, create_project):
        """
        Test case to Verify delete function in add team member
        (AUD-90)
        :param create_project:
        :return:
        """
        self.dp.navigate_to_member_page()
        self.dp.add_team_member_from_members_page(DC.ADD_TEAM_ROLE["PROJECT_MANAGER"],
                                                  DC.ADD_TEAM_DOMAIN["REGULATORY_ADMINISTRATIVE"])
        self.dp.delete_member_from_list()

    def test_delete_team_member(self, create_project):
        """
        Test case to check team members are added in member tab and verify shortcut card is getting disappeared
        (AUD-90)
        :param create_project:
        :return:
        """
        self.dp.navigate_to_member_page()
        self.dp.add_team_member_from_members_page(DC.ADD_TEAM_ROLE["PROJECT_MANAGER"],
                                                  DC.ADD_TEAM_DOMAIN["REGULATORY_ADMINISTRATIVE"])
        self.dp.click_add_team_member_button()

    def test_add_team_member_and_verify_team_member_is_added(self, create_project):
        """
        This function will add team member and verify it is added
        :param create_project:
        AUD-90
        :return:
        """
        self.dp.navigate_to_member_page()
        self.dp.add_team_member_from_members_page(DC.ADD_TEAM_ROLE["PROJECT_MANAGER"],
                                                  DC.ADD_TEAM_DOMAIN["REGULATORY_ADMINISTRATIVE"])
        self.dp.click_add_team_member_button()
        self.dp.verify_team_member_added_and_displayed(DC.ADD_USERS["USER2"])

    def test_add_team_member_shortcut_disappear(self, create_project):
        """
        This function will check add team member shortcut is disappear
        AUD-90
        :param create_project:
        :return:
        """
        self.dp.navigate_to_member_page()
        self.dp.add_team_member_from_members_page(DC.ADD_TEAM_ROLE["PROJECT_MANAGER"],
                                                  DC.ADD_TEAM_DOMAIN["REGULATORY_ADMINISTRATIVE"])
        self.dp.click_add_team_member_button()
        self.dp.verify_team_member_added_and_displayed(DC.ADD_USERS["USER2"])
        self.dp.check_shortcut_card_disappear(PC.XP_ADD_TEAM_MEMBER_CARD)

    def test_verify_send_document_functionality_in_document_page(self, create_project):
        """
        Test case to Verify send document functionality in document page
        (AUD-45) [AC:1,2,3,4,5]
        :param create_project:
        :return:
        """
        self.dp.create_document(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                doc_name="document1",
                                doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.verify_fields_for_send_document_flow(DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])

    def test_verify_delete_gsp_form(self, create_project):
        """
        Test case to Verify delete gsp form from document page
        (AUD-846)
        :param create_project:
        :return:
        """
        self.dp.click_shortcut_cards(PC.XP_GSP_CARD, PC.XP_GSP_COMPLETE_BTN)
        self.gf.click_back_navigation_icon()
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.document_actions(DC.XP_DELETE_BTN)
        self.gf.verify_document_confirmation()

    def test_verify_view_gsp_form(self, create_project):
        """
        Test case to Verify view gsp form from document page
        (AUD-846)
        :param create_project:
        :return:
        """
        self.dp.click_shortcut_cards(PC.XP_GSP_CARD, PC.XP_GSP_COMPLETE_BTN)
        self.gf.click_back_navigation_icon()
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.document_actions(DC.XP_VIEW_BTN)
        self.dp.verify_gsp_data_fields()

    def test_verify_edit_gsp_form(self, create_project):
        """
        Test case to Verify edit gsp form from document page
        (AUD-846)
        :param create_project:
        :return:
        """
        self.dp.create_document(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                doc_name="document1",
                                doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.document_actions(DC.XP_VIEW_BTN)
        self.dp.add_health_authority(health_authority=DC.HEALTH_AUTHORITY.get("DEMO"),
                                     application_type=DC.APPLICATION_TYPE.get("APP_TYPE_1"),
                                     proposed_indication="test05", application_number="001",
                                     submission_number="1",
                                     contact_information="7708538922")
        self.dp.edit_the_added_health_authority("Edited")
        self.dp.gsp_add_additional_information(doc_name="add_info",
                                               doc_status=DC.DOCUMENT_STATUS.get("STATUS_2"))
        self.dp.click_on_additional_info_save_btn()
        self.gf.click_back_navigation_icon()
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.document_actions(DC.XP_VIEW_BTN)
        self.dp.click_on_health_authority_additional_info_icon()

    def test_verify_edit_gsp_form_click_cancel_button(self, create_project):
        """
        Test case to Verify edit gsp form click on cancel button
        user will be presented with the confirmation popup
        (AUD-846)
        :param create_project:
        :return:
        """
        self.dp.create_document(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                doc_name="document1",
                                doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.document_actions(DC.XP_VIEW_BTN)
        self.dp.gsp_add_additional_info_by_clicking_cancel_btn(doc_name="add_info",
                                                               doc_status=DC.DOCUMENT_STATUS.get("STATUS_2"))
        self.gf.verify_document_confirmation()

    def test_verify_download_gsp_form_from_create_document_tab(self, create_project):
        """
        Test case to Verify download gsp form from document page
        (AUD-846)
        :param create_project:
        :return:
        """
        self.dp.click_shortcut_cards(PC.XP_GSP_CARD, PC.XP_GSP_COMPLETE_BTN)
        self.gf.click_back_navigation_icon()
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.document_actions(DC.XP_DOWNLOAD_BTN)
        self.gf.verify_document_confirmation()

    def test_verify_download_gsp_form_from_metadata_screen(self, create_project):
        """
        Test case to Verify download gsp form from metadata screen
        (AUD-53)
        :param create_project:
        :return:
        """
        self.dp.click_shortcut_cards(PC.XP_GSP_CARD, PC.XP_GSP_COMPLETE_BTN)
        self.dp.add_health_authority(health_authority=DC.HEALTH_AUTHORITY.get("DEMO"),
                                     application_type=DC.APPLICATION_TYPE.get("APP_TYPE_1"),
                                     proposed_indication="test",
                                     application_number="001", submission_number="1",
                                     contact_information="7708538922")
        self.dp.click_on_download_btn_in_ha_form()
        self.gf.verify_document_confirmation()

    def test_add_team_member_from_shortcut(self, create_project):
        """
        Test case to check whether team members can be added via shortcut and verify shortcut gets disappeared
        (AUD-180)
        :param create_project:
        :return:
        """
        self.dp.click_shortcut_cards(PC.XP_ADD_TEAM_MEMBER_CARD, PC.XP_ADD_TEAM_MEMBER_START_BTN)
        self.dp.add_team_member_from_members_page(DC.ADD_TEAM_ROLE["PROJECT_MANAGER"],
                                                  DC.ADD_TEAM_DOMAIN["REGULATORY_ADMINISTRATIVE"])
        self.dp.verify_team_member_added_and_displayed(DC.ADD_USERS["USER2"])
        self.dp.check_shortcut_card_disappear(PC.XP_ADD_TEAM_MEMBER_CARD)

    # sprint 5
    @pytest.mark.smoke
    def test_create_task(self, create_project):
        """
        Test case to send documents to recipients HA and creating a task
        AUD-847
        :param create_project:
        :return:
        """
        self.dp.create_document(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                doc_name="document1",
                                doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.send_files_to_recipients(HOST_HA_NAME_1,
                                         TC.OPTIONAL_MSG,
                                         DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])
        self.dp.verify_task_creation()

    def test_verify_tool_tip_is_displayed_without_selecting_files(self, create_project):
        """
        Test case to verify whether tool-tip is displayed without selecting
        the documents
        AUD-45
        :param create_project:
        :return:
        """
        self.dp.create_document(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                doc_name="document1",
                                doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.check_send_files_tool_tip_is_displayed_without_selecting_files()

    def test_remove_files_from_send_file_popup(self, create_project):
        """
        Test case to add or remove files from the send file pop-up
        AUD-847
        :param create_project:
        :return:
        """
        self.dp.create_document(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                doc_name="document1",
                                doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.upload_document_task_for_ha(DC.DOCUMENT_DOMAIN["SUPPORTING_MATERIAL"],
                                            DC.DOCUMENT_TYPE["SUPPORTING_EVIDENCE"],
                                            DC.DOCUMENT_SUBTYPE["TOPLINE_RESULTS"],
                                            DC.META_UPLOAD_DOC["DOCUMENT_NAME"],
                                            DC.META_UPLOAD_DOC["CLEARED_FOR_DISTRIBUTION"],
                                            DC.DOCUMENT_STATUS["STATUS_1"])
        self.dp.remove_multiple_files_in_send_files(DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"])

    def test_verify_send_files_confirmation_popup_displayed(self, create_project):
        """
        Test case to verify send files confirmation popup is displayed
        AUD-952
        :param create_project:
        :return:
        """
        self.dp.create_document(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                doc_name="document1",
                                doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.verify_send_file_popup_displayed(DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"],
                                                 HOST_HA_NAME_1,
                                                 TC.OPTIONAL_MSG)

    def test_verify_on_click_cancel_btn_in_send_file_popup_navigating_to_send_files(self, create_project):
        """
        Test case to verify on click cancel button in
        send file popup navigating to send files overlay
        AUD-952
        :param create_project:
        :return:
        """
        self.dp.create_document(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                doc_name="document1",
                                doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.click_on_send_file_popup_cancel_button(DC.WORKFLOW_TYPES["SEND_GSP_PACKAGE"],
                                                       HOST_HA_NAME_1,
                                                       TC.OPTIONAL_MSG)

    @pytest.mark.smoke
    def test_gsp_submit_package_short_cut_appear(self, create_project):
        """
        Test case to Verify that the gsp submit package short cut card appears,
        after GSP document and supporting documents are created
        AUD-424
        :param create_project:
        :return:
        """
        self.dp.create_document(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                doc_name="document1",
                                doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.upload_document_task_for_ha(DC.DOCUMENT_DOMAIN["SUPPORTING_MATERIAL"],
                                            DC.DOCUMENT_TYPE["SUPPORTING_EVIDENCE"],
                                            DC.DOCUMENT_SUBTYPE["TOPLINE_RESULTS"],
                                            DC.META_UPLOAD_DOC["DOCUMENT_NAME"],
                                            DC.META_UPLOAD_DOC["CLEARED_FOR_DISTRIBUTION"],
                                            DC.DOCUMENT_STATUS["STATUS_1"])
        self.dp.check_shortcut_card_displayed(PC.XP_GSP_SUBMIT_PACKAGE_CARD)

    def test_navigate_to_send_files_upon_gsp_submit_package_shortcut(self, create_project):
        """
        Test case to Verify that the user navigates to the
        send files screen upon clicking the gsp submit package
        shortcut card
        AUD-424
        :param create_project:
        :return:
        """

        self.dp.create_document(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                doc_name="document1",
                                doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.upload_document_task_for_ha(DC.DOCUMENT_DOMAIN["SUPPORTING_MATERIAL"],
                                            DC.DOCUMENT_TYPE["SUPPORTING_EVIDENCE"],
                                            DC.DOCUMENT_SUBTYPE["TOPLINE_RESULTS"],
                                            DC.META_UPLOAD_DOC["DOCUMENT_NAME"],
                                            DC.META_UPLOAD_DOC["CLEARED_FOR_DISTRIBUTION"],
                                            DC.DOCUMENT_STATUS["STATUS_1"])
        self.dp.check_shortcut_card_displayed(PC.XP_GSP_SUBMIT_PACKAGE_CARD)
        self.dp.click_shortcut_cards(PC.XP_GSP_SUBMIT_PACKAGE_CARD, DC.XP_COMPLETE_BUTTON)
        self.dp.verify_send_recipient_is_displayed()

    @pytest.mark.smoke
    def test_gsp_submit_package_disappear_upon_document_submit(self, create_project):
        """
        Test case to Verify that the gsp submit package short cut card disappears,
        post GSP document and supporting documents are created
        AUD-424
        :param create_project:
        :return:
        """
        self.dp.create_document(DC.DOCUMENT_DOMAIN["REGULATORY_ADMINISTRATIVE"],
                                DC.DOCUMENT_TYPE["REGULATORY_DOCUMENT"],
                                DC.DOCUMENT_SUBTYPE["GLOBAL_SUBMISSIONS"],
                                doc_name="document1",
                                doc_status=DC.DOCUMENT_STATUS.get("STATUS_1"))
        self.dp.verify_document_creation(DC.GSP_SUBTYPE["GLOBAL_SUBMISSIONS"])
        self.dp.upload_document_task_for_ha(DC.DOCUMENT_DOMAIN["SUPPORTING_MATERIAL"],
                                            DC.DOCUMENT_TYPE["SUPPORTING_EVIDENCE"],
                                            DC.DOCUMENT_SUBTYPE["TOPLINE_RESULTS"],
                                            DC.META_UPLOAD_DOC["DOCUMENT_NAME"],
                                            DC.META_UPLOAD_DOC["CLEARED_FOR_DISTRIBUTION"],
                                            DC.DOCUMENT_STATUS["STATUS_1"])
        self.dp.check_shortcut_card_displayed(PC.XP_GSP_SUBMIT_PACKAGE_CARD)
        self.dp.click_shortcut_cards(PC.XP_GSP_SUBMIT_PACKAGE_CARD, DC.XP_COMPLETE_BUTTON)
        self.dp.verify_send_recipient_is_displayed()
        self.dp.send_files(HOST_HA_NAME_1, TC.OPTIONAL_MSG)
        self.dp.verify_task_creation()
        self.dp.check_shortcut_card_disappear(PC.XP_GSP_SUBMIT_PACKAGE_CARD)
