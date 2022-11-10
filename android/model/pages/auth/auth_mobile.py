"""
Page object: auth
"""
import allure
from appium.webdriver.common.appiumby import AppiumBy

from model import constants
from model.base_page import BasePage
from model.locators import  MobileAuthPageLocators, MobileMainPageLocators
from model.pages.auth.model import AuthData


class MobileAuth(BasePage):
    """
    Auth in page
    """

    @allure.step('Set username')
    def fill_user_name(self, data: AuthData):
        self.fill_element(locator=(AppiumBy.ID, MobileAuthPageLocators.LOGIN), text=data.login)
        return self

    @allure.step(f"Set user password")
    def fill_user_password(self,  data: AuthData):
        self.fill_element(locator=(AppiumBy.ID, MobileAuthPageLocators.PASSWORD), text=data.password)
        return self

    @allure.step('Submit form')
    def submit_form(self):
        self.click_element(locator=(AppiumBy.ACCESSIBILITY_ID, MobileAuthPageLocators.BUTTON_LOGIN))
        return self

    @allure.step('Check text on page, because user input invalid username or password')
    def have_text_input_invalid_name_or_password(self):
        self.check_element_have_text(locator=(AppiumBy.CLASS_NAME, MobileAuthPageLocators.INVALID_MASSEGE), text=constants.TEXT)
        return self

    @allure.step('Check text on title in main page')
    def check_title(self):
        self.check_element_have_text(locator=MobileMainPageLocators.TITLE, text='Products')
        return self
