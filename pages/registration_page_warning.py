from playwright.sync_api import Page
class RegisterPageWarning:
    def __init__(self,page:Page):
        self.page=Page
        #locators
        self.firstname_war=page.locator("//div[contains(text(),'First Name must be between 1 and 32 characters!')]")
        self.lastname_war=page.locator("//div[contains(text(),'Last Name must be between 1 and 32 characters!')]")
        self.email_war=page.locator("//div[contains(text(),'E-Mail Address does not appear to be valid!')]")
        self.telephone_war=page.locator("//div[contains(text(),'Telephone must be between 3 and 32 characters!')]")
        self.password_war=page.locator("//div[contains(text(),'Password must be between 4 and 20 characters!')]")

        #Action methods
    def firstnametext(self):
            ftext=self.firstname_war.is_visible()
            return ftext

    def lastnametext(self):
        ltext=self.lastname_war.is_visible()
        return ltext
    def emailtext(self):
        etext=self.email_war.is_visible()
        return etext
    def telephonetext(self):
        ttext=self.telephone_war.is_visible()
        return ttext
    def passwordtext(self):
        ptext=self.password_war.is_visible()
        return ptext








