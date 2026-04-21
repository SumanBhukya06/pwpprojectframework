import pytest

from pages import registration_page_warning
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utilities.random_data_util import RandomDataUtil
from pages.registration_page_warning import RegisterPageWarning
from playwright.sync_api import expect

@pytest.mark.sanity
@pytest.mark.regression
def test_warning_text(page):
    home_page=HomePage(page)
    registration_page=RegistrationPage(page)
    registration_page_war=RegisterPageWarning(page)



    home_page.click_my_account()
    home_page.click_register()
    registration_page.click_continue()
    registration_page_war.firstnametext()
    registration_page_war.lastnametext()
    registration_page_war.emailtext()
    registration_page_war.telephonetext()
    registration_page_war.passwordtext()








