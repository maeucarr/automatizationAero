from Locators.Aeropay_LoginLocators import Aeropay_Login
from Pages.Functions import Functions


class Aeropay_LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.func = Functions(self.driver)
        self.aeropay_login = Aeropay_Login()

    """Display functions for Aeropay Login"""

    def is_email_input_display(self):
        return self.func.is_displayed(self.aeropay_login.email_input)

    def is_password_input_display(self):
        return self.func.is_displayed(self.aeropay_login.password_input)

    def is_signin_button_display(self):
        return self.func.is_displayed(self.aeropay_login.signin_bt)

    def is_reset_button_display(self):
        return self.func.is_displayed(self.aeropay_login.reset_password)

    def is_create_account_button_display(self):
        return self.func.is_displayed(self.aeropay_login.create_account)

    """Click functions for Aeropay Login"""

    def email_input_click(self):
        return self.func.click(self.aeropay_login.email_input)

    def password_input_click(self):
        return self.func.click(self.aeropay_login.password_input)

    def signin_button_click(self):
        return self.func.click(self.aeropay_login.signin_bt)

    def reset_button_click(self):
        return self.func.click(self.aeropay_login.reset_password)

    def create_account_button_click(self):
        return self.func.click(self.aeropay_login.create_account)

    """Enter text functions for Aeropay Login"""

    def enter_email_text(self, text):
        return self.func.enter_text(self.aeropay_login.email_input, text)

    def enter_password_text(self, text):
        return self.func.enter_text(self.aeropay_login.password_input, text)

    """Get text functions for Aeropay Login"""

    def get_error_message_text(self):
        return self.func.get_text(self.aeropay_login.error_message)