import os
import time

import allure
import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from ui_web.model import app
from ui_web.model.pages.auth.model import AuthData
from ui_web.utils import attachment

URL_MAIN = os.getenv('URL_MAIN')


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('selene.base_url', 'https://saucedemo.com/')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.hold_browser_open = (
            os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
    )
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
@allure.description('Test auth in system')
def auth():
    """
    Test open sign up page
    """
    open_page(URL_MAIN)
    data = AuthData()
    app.auth.fill_user_name(data).fill_user_password(data).submit_form()
    yield auth
    browser.close()

@pytest.fixture(scope='function')
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN_SELENOID')
    password = os.getenv('PASSWORD_SELENOID')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver
    yield browser

    attachment.add_html(browser)
    attachment.add_screenshot(browser)
    attachment.add_logs(browser)
    attachment.add_video(browser)
    browser.quit()


@allure.step('Open page')
def open_page(url: str):
    """
    Open(redirect) pages contains testing form
    """
    browser.open(url)
    time.sleep(1)


@allure.step('Close page')
def close_page():
    """
    Close pages contains testing form
    """
    browser.close()
    time.sleep(1)


