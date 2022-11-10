"""
Tests web version swaglabs
"""
import os
import time

import allure
import pytest

from model import app
from model.pages.auth.model import AuthData
from ui_web.tests.conftest import open_page


URL_MAIN = os.getenv('URL_MAIN')


@pytest.mark.web
@allure.tag('UI')
@allure.description('Test auth in system')
def test_auth(setup_browser):
    """
    Test open sign up page
    """
    open_page(URL_MAIN)
    data = AuthData()
    app.auth.fill_user_name(data).fill_user_password(data).submit_form().check_title()
    time.sleep(3)


@pytest.mark.web
@allure.tag('UI')
@pytest.mark.parametrize("field, attr", [('login', '2233'), ('password', '3387777'), ('login', None), ('password', None)])
@allure.description('Test auth in system with invalid user data')
def test_invalid_auth(setup_browser, field, attr):
    """
    Test auth in system with invalid user data
    """
    open_page(URL_MAIN)
    data = AuthData()
    setattr(data, field, attr)
    app.auth.fill_user_name(data).fill_user_password(data).submit_form()
    app.auth.have_text_input_invalid_name_or_password()


@pytest.mark.web
@allure.tag('UI')
@allure.description('Test make order in market')
def test_make_order(setup_browser, auth):
    """
    Test make order
    """
    app.main.click_button_add_cart().get_number_of_products_in_carts().click_button_cart().click_button_checkout()
    app.main.fill_first_name().fill_last_name().fill_postal_code().click_button_continue()
    app.main.click_button_finish()


@pytest.mark.web
@allure.tag('UI')
@allure.description('Test add product in cart')
def test_add_product_in_cart(setup_browser, auth):
    """
    Test add product in cart
    """
    app.main.click_button_add_cart().get_number_of_products_in_carts()

