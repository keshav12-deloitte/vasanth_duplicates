"""
This module contains xpaths and constants involved in creating a new project
"""

# Xpaths #
XP_CP_OVERLAY_HEADER = "//*[@class='global-text create-new-project-container']//div[contains(text(),'Create New Project')]"
XP_CP_OVERLAY_SUB_HEADER = "//*[@class='global-text create-new-project-container']//*[contains(@class,'global-text--title-sub-header')]"
XP_CANCEL_BTN = "//app-button[@text='CANCEL']"
XP_CP_BTN = "//app-button[@text='CREATE']"
XP_PRODUCT_CODE_DD = "//*[contains(text(),'Product Code')]/../../../*[@role='combobox']"
XP_REGULATORY_EVENT_DD = "//*[contains(text(),'Regulatory Event')]/../../../*[@role='combobox']"
XP_PROJECT_REVIEW_TYPE_DD = "//*[contains(text(),'Project Review Type')]/../../../*[@role='combobox']"
XP_INDICATION_FIELD = "//*[contains(text(),'Indication')]/../../../*[@data-placeholder='Placeholder']"
XP_SNACKBAR_DISMISS_BTN = "//span[contains(text(),'DISMISS')]"
XP_START_GUIDE = "//div[contains(text(),'Priority tasks will appear here')]"
XP_CLOSE_START_GUIDE = "//*[@class='close']"
XP_LOADER_POPUP_TEXTS = "//*[@role='progressbar']/../preceding-sibling::*"
XP_PROJECT_WORKSPACE_TAB = "//*[@class='mat-tab-links']//*[contains(text(),'{}')]"
XP_DD_ITEMS = "//*[@class='mat-option-text']"
XP_GSP_CARD = "//mat-card-title[contains(text(),'Complete Global Submission Plan (GSP) Form')]"
XP_ADD_TEAM_MEMBER_CARD = "//mat-card-title[contains(text(),'Add Team Members')]"
XP_GSP_SUBMIT_PACKAGE_CARD = "//mat-card-title[contains(text(),'Submit GSP Package')]"
XP_SUPPORTING_MATERIAL_CARD = "//mat-card-title[contains(text(),'Add Supporting Materials')]"
XP_GSP_COMPLETE_BTN = "//span[contains(text(),'COMPLETE')]"
XP_ADD_TEAM_MEMBER_START_BTN = "//*[contains(text(),'Add Team Members')]/..//*[contains(text(),'ADD')]"
XP_SUPPORTING_MATERIAL_START_BTN = "//*[contains(text(),'Add Supporting Materials')]/..//*[contains(text(),'Start')]"
XP_ADDITIONAL_INFO_SAVE_BTN = "//span[contains(text(),'Save')]"
XP_PROJECT_NAME = "//span[contains(text(),'Product A-Event 1')]"
XP_LOADER_POPUP_MSG = "//div[contains(text(),'Please wait while your project is being created')]"

# s4#
XP_PRODUCT_NAME = "//div[contains(text(),'Product Name')]/../../../..//following-sibling::tbody//td[1]"
XP_PROJECT_REVIEW_TYPE = "//div[contains(text(),'Review Type')]/../../../..//following-sibling::tbody//td[2]"
# Constants #
CP_OVERLAY_HEADER = "Create New Project"
TXT_PROJECT_REVIEW_TYPE = "Project Review Type"
TXT_REGULATORY_EVENT = "Regulatory Event"
TXT_PRODUCT_NAME = "Product Name"
PRODUCT_NAME_ERROR_MSG = "Product Name cannot be more than 50"
INDICATION_ERROR_MSG = "Indication cannot be more than 56"
LOADER_POP_MSG = "Please wait while your project is being created"
PRIORITY_TASKS = "Priority Tasks"
PRODUCT_CODE = {
    "PRODUCT_A": "Product A",
    "PRODUCT_B": "Product B"
}
REVIEW_TYPE = {
    "PROJECT_ORBIS": "Project Orbis"
}
REGULATORY_EVENT_NAME = {
    "EVENT_1": "Event 1", "EVENT_2": "Event 2"
}
INDICATION = "indication1"

TABS = {
    "OVERVIEW": "OVERVIEW",
    "FILES": "FILES",
    "MEMBERS": "MEMBERS"
}
PROJECT_NAME = {
    "PRODUCT-B": "Product B-Event 1-Jan-2022",
    "PRODUCT-A": "Product A-Event 1-Jan-2022"
}
