"""
Tests web version swaglabs
"""
import os
import allure
import pytest
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser

from android.model import app
from android.model.pages.auth.model import AuthData

URL_MAIN = os.getenv('URL_MAIN')


@pytest.mark.mobile
@allure.description('Test auth in system')
def test_auth():
    """
    Test open sign up page
    """
    data = AuthData()
    app.mobile_auth.fill_user_name(data).fill_user_password(data).submit_form()


@pytest.mark.mobile
@pytest.mark.parametrize("field, attr", [('login', '2233'), ('password', '3387777'), ('login', None), ('password', None)])
@allure.description('Test auth in system with invalid user data')
def test_invalid_auth(field, attr):
    """
    Test auth in system with invalid user data
    """

    data = AuthData()
    setattr(data, field, attr)
    app.mobile_auth.fill_user_name(data).fill_user_password(data).submit_form()
    app.mobile_auth.have_text_input_invalid_name_or_password()


@pytest.mark.web
@allure.description('Test make order in market')
def test_make_order(auth):
    """
    Test make order
    """
    app.mobile_main.click_button_add_cart().get_number_of_products_in_carts().click_button_cart().click_button_checkout()
    app.mobile_main.fill_first_name().fill_last_name().fill_postal_code().click_button_continue()
    app.mobile_main.click_button_finish()


@pytest.mark.web
@allure.description('Test add product in cart')
def test_add_product_in_cart(auth):
    """
    Test add product in cart
    """
    app.mobile_main.click_button_add_cart().get_number_of_products_in_carts()

