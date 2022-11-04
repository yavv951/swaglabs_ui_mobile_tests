"""
Tests web version swaglabs
"""
import os
import allure
import pytest
from allure_commons.types import AttachmentType
from model import app
from model.pages.auth.model import AuthData
from tests.conftest import open_page
from utils.attachment import take_screenshot, add_video_to_report

URL_MAIN = os.getenv('URL_MAIN')


@pytest.mark.web
@allure.description('Test auth in system')
def test_auth():
    """
    Test open sign up page
    """
    open_page(URL_MAIN)
    data = AuthData()
    app.auth.fill_user_name(data).fill_user_password(data).submit_form()
    take_screenshot(name='Screenshot', type_file=AttachmentType.PNG)
    add_video_to_report()


@pytest.mark.web
@pytest.mark.parametrize("field, attr", [('login', '2233'), ('password', '3387777'), ('login', None), ('password', None)])
@allure.description('Test auth in system with invalid user data')
def test_invalid_auth(field, attr):
    """
    Test auth in system with invalid user data
    """
    open_page(URL_MAIN)
    data = AuthData()
    setattr(data, field, attr)
    app.auth.fill_user_name(data).fill_user_password(data).submit_form()
    app.auth.have_text_input_invalid_name_or_password()
    take_screenshot(name='Screenshot', type_file=AttachmentType.PNG)
    add_video_to_report()


@pytest.mark.web
@allure.description('Test make order in market')
def test_make_order(auth):
    """
    Test make order
    """
    app.main.click_button_add_cart().get_number_of_products_in_carts().click_button_cart().click_button_checkout()
    app.main.fill_first_name().fill_last_name().fill_postal_code().click_button_continue()
    app.main.click_button_finish()
    take_screenshot(name='Screenshot', type_file=AttachmentType.PNG)
    add_video_to_report()


@pytest.mark.web
@allure.description('Test add product in cart')
def test_add_product_in_cart(auth):
    """
    Test add product in cart
    """
    app.main.click_button_add_cart().get_number_of_products_in_carts()
    take_screenshot(name='Screenshot', type_file=AttachmentType.PNG)
    add_video_to_report()

