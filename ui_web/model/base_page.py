from selene import be, have
from selene.support.shared import browser


class BasePage:

    @staticmethod
    def fill_element(locator, text):
        browser.element(locator).clear().type(text)

    @staticmethod
    def click_element(locator):
        browser.element(locator).should(be.clickable).click()

    @staticmethod
    def check_element_have_text(locator, text):
        browser.element(locator).should(have.text(text))

