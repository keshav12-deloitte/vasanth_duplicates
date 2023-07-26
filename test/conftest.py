import os
import shutil
import time

import pytest

from base.driver import WebDriver
from constants import generic_constants as GC
from page.genericFunctions import BasePage
from utils.environment_variables import BROWSER, HEADLESS, URL
from utils.logs import logger


def pytest_configure():
    # It deletes the report folder while running the test case
    if os.path.exists(GC.REPORT_FOLDER_PATH):
        shutil.rmtree(GC.REPORT_FOLDER_PATH)


def pytest_addoption(parser):
    """
    Function to get value from the Command line while executing for browser, url and headless option
    :param parser:
    :return:
    """
    parser.addoption("--browser", action="store", default=BROWSER.lower())
    parser.addoption("--url", action="store", default=URL)
    parser.addoption("--headless", action="store", default=HEADLESS)


@pytest.fixture(scope='class')
def setup(request):
    """
    This function sets up the browser for test execution
    :param request:
    :return:
    """
    global driver
    webdriver = WebDriver()
    driver = webdriver.get_web_driver(request.config.getoption("browser"), request.config.getoption("headless"))
    driver.maximize_window()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(2)
    driver.quit()


@pytest.fixture(scope='function')
def launch_application(request):
    """
    Function to launch the url
    :return:
    """
    bp = BasePage(driver)
    bp.launch_url(request.config.getoption("url"))


@pytest.fixture(scope='function', autouse=True)
def test_log(request):
    # Here logging is used, you can use whatever you want to use for logs
    logger.info("STARTED Test '{}'".format(request.node.name))

    def fin():
        logger.info("COMPLETED Test '{}' \n".format(request.node.name))

    request.addfinalizer(fin)


@pytest.fixture(scope="class")
def before_test(request):
    logger.info(f"Test Execution is started with {request.config.getoption('browser')} browser ...")
    yield
    logger.info(f"Test Execution is Stopped")
