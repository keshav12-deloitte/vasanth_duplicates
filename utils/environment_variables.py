"""This is constant's file which will be used by many other modules. Anything that's static and will not change will be
found here
Also we have variables here which are getting values from ..env file."""

import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
URL = os.environ.get('URL')
BROWSER = os.environ.get('BROWSER')
HEADLESS = os.environ.get('HEADLESS')
EMAIL_ID = os.environ.get("EMAIL_ID")
PASSWORD = os.environ.get("PASSWORD")
HOST_HA_EMAIL = os.environ.get("HOST_HA_EMAIL")
HOST_HA_PASSWORD = os.environ.get("HOST_HA_PASSWORD")
HOST_HA_NAME_1 = os.environ.get("HA_RECIPIENT_NAME_1")
HOST_HA_NAME_2 = os.environ.get("HA_RECIPIENT_NAME_2")
SPONSOR_NAME = os.environ.get("SPONSOR_NAME")
RECIPIENT_ID = os.environ.get("RECIPIENT_ID")
RECIPIENT_URL = os.environ.get("RECIPIENT_URL")
OTP = os.environ.get("OTP")
