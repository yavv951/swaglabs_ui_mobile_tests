"""
Application manager
"""
from model.pages.auth.auth import Auth
from model.pages.auth.auth_mobile import MobileAuth
from model.pages.main_page.main import Main
from model.pages.main_page.main_mobile import MobileMain

auth = Auth()
main = Main()
mobile_auth = MobileAuth()
mobile_main = MobileMain()
