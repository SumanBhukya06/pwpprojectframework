from playwright.sync_api import expect
import pytest

from pages import registration_page
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.my_account_page import MyAccountPage
from utilities.random_data_util import RandomDataUtil
from pages.newsletter_page import NewsletterPage

@pytest.mark.sanity
@pytest.mark.regression
def yes_option_is_selected_for_newsletter(page):
    home_page=HomePage(page)
    registration_page=RegistrationPage(page)
    my_account_page=MyAccountPage(page)
    newsletter_page=NewsletterPage(page)

    home_page.click_my_account()
    home_page.click_register()

    random_data = RandomDataUtil()
    first_name=random_data.get_first_name()
    last_name=random_data.get_last_name()
    email=random_data.get_email()
    password=random_data.get_password()

    registration_page.set_first_name(first_name)
    registration_page.set_last_name(last_name)
    registration_page.set_email(email)
    registration_page.set_password(password)
    registration_page.set_confirm_password(password)

    #Newsletter
    registration_page.chk_radio_newsletter_yes()
    #policy
    registration_page.set_privacy_policy()
    registration_page.click_continue()
    confirm_msz=registration_page.get_confirmation_msg()
    expect(confirm_msz).to_have_text("Your Account Has Been Created!")

    #newsletter click
    my_account_page.click_newsletter()
    newsletter_page.get_newsletter_page_radio_yes()
    newsletter_page.clk_newsletter_page_continue()
    news_update_text=my_account_page.verify_newsletter_update_msz()
    expect(news_update_text).to_have_text("Success: Your newsletter subscription has been successfully updated!")




    #

