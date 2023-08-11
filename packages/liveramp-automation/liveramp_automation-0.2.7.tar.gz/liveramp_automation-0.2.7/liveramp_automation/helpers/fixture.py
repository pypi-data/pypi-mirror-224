import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from liveramp_automation.helpers.login import LoginHepler
from liveramp_automation.helpers.file import FileHelper
from liveramp_automation.utils.log import Logger
from typing import Generator
from playwright.sync_api import Playwright, BrowserContext


@pytest.fixture(scope="module")
def config():
    Logger.info("It is going to import the envChoice.")
    if not os.environ.get('ENVCHOICE'):
        os.environ['ENVCHOICE'] = "prod"
    runEnv = os.environ['ENVCHOICE']
    init_dict = FileHelper.read_init_file('', 'pytest.ini')
    try:
        if init_dict['data']:
            resource_data = init_dict['data']
        if resource_data['resource_path']:
            resource_path = resource_data['resource_path']
        else:
            Logger.error("Please provive resource_data path.")
        if resource_data['resource_prefix']:
            resource_prefix = resource_data['resource_prefix']
        else:
            Logger.error("Please provive resource_prefix.")
    except TypeError:
        Logger.error("Please provive resource_prefix.")

    Logger.info("The testing environment is {} ".format(dict))
    return FileHelper.load_env_yaml(resource_path, resource_prefix, runEnv)


###########################
# API Prefix handle #
##########################


@pytest.fixture(scope="module")
def lrone():
    Logger.info("It is going to import the envChoice.")
    headers = {"lr-org-id": config["lr_org"]}
    Logger.info("It is going to call okta oauth2 token.")
    token = LoginHepler.call_oauth2_get_token(os.environ["APIUSERNAME"], os.environ["APIPASSWORD"])
    Logger.info("We got the okta oauth2 token.Will put it in the headers")
    headers["authorization"] = token
    return headers


################################################
# UI Automation Testing Prefix handle #
###############################################

@pytest.fixture(scope="module")
def driver():
    if not os.environ.get('runEnv'):
        os.environ['runEnv'] = "remote"
    runEnv = os.environ['runEnv']
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    default_directory = os.path.join(os.getcwd(), "resources/download")
    prefs = {"download.default_directory": default_directory}
    chrome_options.add_experimental_option("prefs", prefs)
    Logger.info("The run Env is {}".format(runEnv))
    Logger.info("Run WEBDriver on lang=en ")
    chrome_options.add_argument('--lang=en')

    if runEnv == "remote":
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('window-size=1920x1480')
    else:
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('window-size=1920x1480')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    Logger.info("We are going to open a blank page.")
    driver.get("about:blank")
    driver.implicitly_wait(30)
    Logger.info("We've started a ChromeDriver here.")
    yield driver
    driver.close()
    Logger.info("We've closed the ChromeDriver.Goodbye!")


@pytest.fixture(scope="module")
def page(playwright: Playwright) -> Generator[BrowserContext, None, None]:
    if os.environ['runEnv'] == "remote":
        context = playwright.chromium.launch_persistent_context("", headless=True)
    else:
        context = playwright.chromium.launch_persistent_context("", headless=False, args=['--lang=en'])
    page = context.new_page()
    page.set_default_timeout(60000)
    yield page
    page.close()
    context.close()
