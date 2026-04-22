from playwright.sync_api import Page

class NewsletterPage:
    def __init__(self,page:Page):
        self.page=page

        #locators
        self.newsletter_page_radio_yes=page.locator("input[value='1']")
        self.newsletter_page_continue=page.locator("input[value='Continue']")

        #page validation methods
    def get_newsletter_page_radio_yes(self):
        self.newsletter_page_radio_yes.is_checked()

    def clk_newsletter_page_continue(self):
        self.newsletter_page_continue.click()



