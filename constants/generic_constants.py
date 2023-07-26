"""
This page consists of Generic and Login page xpaths and constants
"""
from os.path import join, dirname

# Xpaths #
XP_EMAIL = "//input[contains(@id,'#/properties/email')]"
XP_PASSWORD = "//input[contains(@id,'#/properties/pass')]"
XP_SIGN_IN_BTN = "//app-button[@class='custom-button']//following-sibling::span[contains(text(),'Sign In')]"
XP_TEXT = "//*[text()='{}']"
XP_CONTAINS_TEXT = "//*[contains(text(),'{}')]"
XP_DROP_DOWN_OPTION = "//*[@role='option']//*[contains(text(),'{}')]"
XP_CREATE_NEW_PROJECT = "//button[@class='mat-focus-indicator mat-button mat-button-base custom-button customClassName mat-button-primary']//mat-icon"
XP_SPINNER = "//*[@role='progressbar']"
XP_SIDE_NAVIGATION_DRAWER_EXPAND = "//*[contains(@class,'toggle-icon flex flex--self-center flex--row ng-star-inserted')]"
XP_SIDE_NAVIGATION_DRAWER_CLOSE = "//*[contains(@class,'toggle-icon flex--self-center flex--row ng-star-inserted')]"
XP_SIDE_NAVIGATION_ITEM = "//*[@class='mat-list-item-content']//*[contains(text(),'{}')]"
XP_BACK_ICON = "//span[contains(@class,'cursor mt-16 mx-14')]"
XP_USER_ICON = "//span[@class='mat-menu-trigger header-icons']"
XP_LOGOUT_BUTTON = "//span[contains(text(),'logout')]"
XP_DOC_SAVE_SUCCESS_SNACK_BAR = "//*[contains(text(),'successfully')]"
XP_NOTIFICATION_ICON = "//app-header/mat-toolbar[1]/div[1]/span[2]/img[1]"
XP_OTP_TEXT_FIELD = "//*[contains(@id,'#/properties/code')]"

# Constants #
DASHBOARD = "Dashboard"
WELCOME = "Welcome"
CREATE_NEW_PROJECT = "Create New Project"
WAIT_TIME = 100
CANCEL = "Cancel"
SAVE = "Save"
SUBMIT_BTN = "Submit"
AUTHORIZATION_CONSENT = "Authorization Consent"

# Path #
DATA_FOLDER_PATH = join(dirname(dirname(dirname(__file__))), 'web_automation\\test\\Data\\{}')
DOWNLOAD_FOLDER_PATH = join(dirname(dirname(dirname(__file__))), 'web_automation/downloads/{}')
REPORT_FOLDER_PATH = join(dirname(dirname(dirname(__file__))), 'web_automation\\report')
DATA_FOLDER_PATH_MAC = join(dirname(dirname(dirname(__file__))), 'web_automation/test/Data/{}')
REPORT_FOLDER_PATH_MAC = join(dirname(dirname(dirname(__file__))), 'web_automation/report')
