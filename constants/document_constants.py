"""
This module contains xpaths and constants involved in creating a new project
"""

# Xpaths #
from constants.generic_constants import DATA_FOLDER_PATH_MAC

XP_CREATE_BTN = "//app-button[@text='Create']"
XP_DOC_UPLOAD_BTN = "//app-button[@text='UPLOAD']"
XP_DOC_CANCEL_BTN = "//app-button[@text='CANCEL']"
XP_DOCUMENT_DOMAIN_DD = "//*[contains(text(),'Domain')]/../../../*[@role='combobox']"
XP_DOCUMENT_TYPE = "//*[contains(text(),'Type')]/../../../*[@role='combobox']"
XP_DOCUMENT_SUB_TYPE_DD = "//*[contains(text(),'Sub-Type')]/../../../*[@role='combobox']"
XP_META_FIELD = "//*[contains(text(),'{}')]/../../../*[1]"
XP_NEXT_BUTTON = "//app-button[@text='NEXT']"
XP_FILE_UPLOAD = "//div[@class='mr-14']//following-sibling::input"
XP_GSP_FORM_HEALTH_AUTHORITY_DD = "//*[contains(text(),'Health Authority')]/../../../*[@role='combobox']"
XP_GSP_FORM_APPLICATION_TYPE_DD = "//*[contains(text(),'Application Type')]/../../../*[@role='combobox']"
XP_GSP_FORM_APPLICATION_NUMBER = "//mat-label[contains(text(),'Application Number')]"
XP_SGP_FORM_SUBMISSION_NUMBER = "//mat-label[contains(text(),'Submission Number')]"
XP_GSP_PLANNED_SUBMISSION_DATE = "//*[contains(text(),'Planned Submission Date')]/../../../..//*[@aria-label='Open calendar']"
XP_GSP_CONTACT_INFORMATION = "//mat-label[contains(text(),'Contact Info')]"
XP_DOCUMENT_CREATED_LIST = "//div[contains(text(),'{}')]"
XP_DOCUMENT_NAME = "//mat-label[contains(text(),'Document Name*')]"
XP_DOCUMENT_DATE_LOCATOR = "//*[contains(text(),'Document Date')]/../../../..//*[@aria-label='Open calendar']"
XP_GSP_SPONSOR_NAME = "//div[contains(text(),'Sponsor Name')]"
XP_APPLICATION_FORM = "//div[contains(text(),'Application Details')]"
XP_PROPOSED_FIELDS = "//span[contains(text(),'Proposed Participating')]"
XP_GSP_FORM_TITLE = "//*[contains(text(),'Global Submission Plan Form')]"
XP_DOCUMENT_DATE = "//*[@role='gridcell']/*[contains(text(),{})]"
XP_DOWNLOAD_ICON_GSP_PAGE = "//div[@class='mr-2']"
XP_SEND_FILES = "//span[contains(text(),'Send Files')]"
XP_CHECKBOX = "(//input[@type='checkbox']//..)[1]"
XP_GSP_CHECKBOX = "(//input[@type='checkbox']//..)[2]"
XP_LAUNCH_WORKFLOW_TYPE_POPUP = "//div[@class='mat-menu-content ng-tns-c296-183']"
XP_LAUNCH_WORKFLOW_TYPES = "//div[contains(text(),'{}')]"
XP_SEND_FILE_POPUP_TITLE = "//div[contains(text(),'Send Files')]"
XP_SEARCH_RECIPIENTS_BOX = "(//input[@role='combobox'])[2]"
XP_SEARCH_MEMBER_BOX = "//input[@role='combobox']"
XP_SELECT_RECIPIENT = "(//span[@class='mat-option-text'])[3]"
XP_CANCEL_BUTTON_IN_SEND_FILE_POPUP = "//span[contains(text(),'CANCEL')]"
XP_VIEW_BTN = "//span[contains(text(),'View')]"
XP_DOWNLOAD_BTN = "//span[contains(text(),'Download')]"
XP_DELETE_BTN = "//span[contains(text(),'Delete')]"
XP_DOC_NAME = "//div[contains(text(),'Sub Type')]/../../../..//following-sibling::tbody//td[3]"
XP_LAST_MODIFIED = "//div[contains(text(),'Last Modified')]/../../../..//following-sibling::tbody//td[6]"
XP_GSP_TOOL_TIP = "//div[contains(text(),'Add Additional information')]"
XP_GSP_CLOSE_TOOL_TIP = "//mat-icon[contains(text(),'close')]"
XP_HA_ADD_BTN = "//span[contains(text(),'Add')]"
XP_HA_OVERLAY_ADD_BTN = "//*[@class='mat-dialog-actions mat-dialog-action-panel']//*[@text='Add']"
XP_SAVED_SUCCESS_MSG = "//span[contains(text(),'Saved document successfully')]"
XP_ADDITIONAL_INFO_ICON = "(//div[@class='flex cursor']//img)[2]"
XP_ADDITIONAL_DOC_FIELD = "//*[contains(text(),'Document Name')]/../../../*[1]"
XP_ADDITIONAL_INFO_SAVE_BTN = "//span[contains(text(),'Save')]"
XP_FILES_ACTION_BTN = "//mat-icon[contains(text(),'more_vert')]"
XP_ADDITIONAL_DOC_STATUS = "//div[contains(@id,'mat-select-value')]//span//span"
XP_EDIT_HA_PROPOSED_TEXT = "(//div[contains(@class,'table-cell ng-star')])[3]"
XP_EDIT_HA_PROPOSED_FILED = "//*[contains(@id,'#/properties/proposedIndication')]"
XP_EDIT_HA_ICON = "(//*[contains(text(),'edit')])[3]"
XP_EDIT_HA_SAVE_BTN = "(//*[contains(text(),'Save')])[2]"
XP_META_DOMAIN = "//span[contains(text(),'Regulatory Administrative')]"
XP_META_DOC_TYPE = "//span[contains(text(),'Regulatory Document')]"
XP_META_DOC_SUBTYPE = "//span[contains(text(),'Global Submissions')]"
# s4#
XP_ADD_BTN = "//mat-icon[contains(text(),'add')]"
XP_ADD_TEAM_ROLE_DD = "//*[contains(text(),'Role')]/../../../*[@role='combobox']"
XP_ADD_TEAM_DOMAIN_DD = "//*[contains(text(),'Domain')]/../../../*[@role='combobox']"
XP_ADD_TEAM_MEMBERS_DD = "//input[@role='combobox']"
XP_TEAM_MEMBER_ADD_BTN = "//span[contains(text(),'ADD')]"
XP_ADD_TEAM_CANCEL_BTN = "//span[contains(text(),'CANCEL')]"
XP_ADDED_TEAM_NAME = "//tbody/tr//td[1]"

# s5#
XP_SELECT_RECIPIENTS = "(//span[@class='mat-option-text'])[3]"
XP_SELECT_FILE_PLACEHOLDER = "(//input[@role='combobox'])[1]"
XP_SELECT_TOPLINE_DOC = "(//span[@class='mat-option-text'])[3]"
XP_TOPLINE_DOC_REMOVE_BTN = "//*[contains(text(),'Top Line Results')]//mat-icon"
XP_MESSAGE_OPTIONAL = "//mat-label[contains(text(),'Message (Optional)')]//..//..//..//input"
XP_SEND_BTN = "//span[contains(text(),'SEND')]"
XP_SEND_FILES_POPUP_CARD = "//h1[contains(text(),'Send Files?')]"
XP_TASK_CREATION_SNACKBAR = "//div[@class='snackbar-container']"
XP_SELECT_FILES_TOOLTIP = "//div[contains(text(),'Add Files')]"
XP_GSP_SUBMIT_PACKAGE_CARD = "//mat-card-title[contains(text(),'Submit GSP Package')]"
XP_COMPLETE_BUTTON = "//span[contains(text(),'COMPLETE')]"
XP_UNREAD_TASK_COUNT = "//span[@id='mat-badge-content-2']"
XP_TASK_ICON = "//img[@class='ng-tns-c311-3']"
XP_ADDITIONAL_DOC_CANCEL_BTN = "//span[contains(text(),'Cancel')]"
XP_EDIT_POPUP_SAVE_BTN = "(//span[contains(text(),'Save')])[2]"
XP_PREPOPULATED_GSP = "//mat-chip[contains(text(),'Global Submissions')]"
# Constants #
GSP_FORM_TITLE = "Global Submission Plan Form"
SPONSOR_NAME = "Sponsor Name"
SEND_FILE_POPUP_TITLE = "Send Files"
DOCUMENT_UPLOAD_FILE = DATA_FOLDER_PATH_MAC.format("sample.pdf")
META_GSP = {
    "SPONSOR_NAME": "Sponsor Name",
    "DOCUMENT_NAME": "Document Name",
    "PROJECT_NAME": "Project Name",
    "PRODUCT_NAME": "Product Name",
    "INDICATION": "Indication",
    "DOCUMENT_DATE": "Document Date",
    "DOCUMENT_STATUS": "Document Status",
    "DOCUMENT_CREATION_DATE": "Document Creation Date"
}

DOCUMENT_DOMAIN = {
    "REGULATORY_ADMINISTRATIVE": "Regulatory Administrative",
    "SUPPORTING_MATERIAL": "Supporting Materials"
}

DOCUMENT_TYPE = {
    "REGULATORY_DOCUMENT": "Regulatory Document",
    "SUPPORTING_EVIDENCE": "Supporting Evidence"
}

DOCUMENT_SUBTYPE = {
    "GLOBAL_SUBMISSIONS": "Global Submissions",
    "TOPLINE_RESULTS": "Top Line Results"
}

META_UPLOAD_DOC = {
    "DOCUMENT_DOMAIN": "Supporting Materials",
    "DOCUMENT_TYPE": "Supporting Evidence",
    "DOCUMENT_SUBTYPE": "Top Line Results",
    "SPONSOR_NAME": "Sponsor Name",
    "DOCUMENT_NAME": "Document Name",
    "PROJECT_NAME": "Project Name",
    "PRODUCT_NAME": "Product Name",
    "INDICATION": "Indication",
    "CLEARED_FOR_DISTRIBUTION": "Cleared for Distribution",
    "DOCUMENT_DATE": "Document Date",
    "DOCUMENT_STATUS": "Document Status",
    "DOCUMENT_VERSION_NUMBER": "Document Version Number",
    "DOCUMENT_CREATION_DATE": "Document Creation Date"
}

GSP_ELECTRONIC_FORM = {
    "HEALTH_AUTHORITY": "Health Authority",
    "APPLICATION_TYPE": "Application Type",
    "PROPOSED_INDICATION": "Proposed Indication",
    "APPLICATION_NUMBER": "Application Number",
    "SUBMISSION_NUMBER": "Submission Number",
    "PLANNED_SUBMISSION_DATE": "Planned Submission Date",
    "CONTACT_INFORMATION": "Contact Info"
}

DOCUMENT_STATUS = {
    "STATUS_1": "Status1",
    "STATUS_2": "Status2"
}

HEALTH_AUTHORITY = {
    "DEMO": "demo",
    "DEMO_HEALTH_ORGANIZATION": "Demo Health Organization",
    "IMOH": "IMOH - Israeli Ministry of Health"
}

APPLICATION_TYPE = {
    "APP_TYPE_1": "application_type_1",
    "APP_TYPE_2": "application_type_2"
}

GSP_SUBTYPE = {
    "GLOBAL_SUBMISSIONS": "Global Submissions",
    "TOPLINE_RESULTS": "Top Line Results"
}
ADD_TEAM_ROLE = {
    "PROJECT_MANAGER": "ProjectManager",
    "AUTHOR": "Author",
    "REVIEWER": "Reviewer",
    "APPROVER": "Approver"
}
ADD_TEAM_DOMAIN = {
    "REGULATORY_ADMINISTRATIVE": "Regulatory Administrative",
    "PROMOTIONAL_MATERIALS": "Promotional Materials",
    "SUPPORTING_MATERIALS": "Supporting Materials",
    "PROJECT_ADMINISTRATIVE": "Project Administrative"
}
ADD_USERS = {
    "USER1": "vasanth",
    "USER2": "testing",
    "USER3": "Aarav"
}
WORKFLOW_TYPES = {
    "SEND_GSP_PACKAGE": "Send Global Submission Plan Package",
    "SEND_OTHER_WORKFLOW": "Send Other Workflow",
    "SEND_SPONSOR_LETTER": "Send Sponsor Authorization Letter",
    "SEND_AID_DOCUMENT": "Send Assessment Aid Document"
}
