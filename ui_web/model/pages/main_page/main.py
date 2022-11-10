"""
Page object: main
"""
import allure
from faker import Faker

from model.base_page import BasePage
from model.locators import MainPageLocators

fake = Faker()

class Main(BasePage):
    """
    Main page
    """

    @allure.step('Click add cart button')
    def click_button_add_cart(self):
        self.click_element(locator=MainPageLocators.ADD_CART)
        return self

    @allure.step('Click button cart container')
    def click_button_cart(self):
        self.click_element(locator=MainPageLocators.BUTTON_CART)
        return self

    @allure.step('Click checkout button')
    def click_button_checkout(self):
        self.click_element(locator=MainPageLocators.BUTTON_CHECKOUT)
        return

    @allure.step('Fill field first name')
    def fill_first_name(self):
        self.fill_element(locator=MainPageLocators.FIELD_FIRST_NAME, text=fake.name())
        return self

    @allure.step('Fill field last name')
    def fill_last_name(self):
        self.fill_element(locator=MainPageLocators.FIELD_LAST_NAME, text=fake.name())
        return self

    @allure.step('Fill field postal code')
    def fill_postal_code(self):
        self.fill_element(locator=MainPageLocators.FIELD_POSTAL_CODE, text=fake.building_number())
        return self

    @allure.step('Click on button continue')
    def click_button_continue(self):
        self.click_element(locator=MainPageLocators.BUTTON_CONTINUE)
        return self

    @allure.step('Click on button finish')
    def click_button_finish(self):
        self.click_element(locator=MainPageLocators.BUTTON_FINISH)
        return self

    def get_number_of_products_in_carts(self):
        self.check_element_have_text(locator=MainPageLocators.NUMBER_OF_PRODUCTS, text='1')
        return self


