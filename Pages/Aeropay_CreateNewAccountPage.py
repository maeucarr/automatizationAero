from Locators.Aeropay_CreateNewAccountLocators import Aeropay_CreateNewAccount
from Pages.Functions import Functions


class Aeropay_CreateNewAccountPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.func = Functions(self.driver)
        self.aeropay_newaccount = Aeropay_CreateNewAccount()

    """Display functions for Aeropay Create New Account"""
    def is_firstname_input_display(self):
        return self.func.is_displayed(self.aeropay_newaccount.first_name_input)

    def is_lastname_input_display(self):
        return self.func.is_displayed(self.aeropay_newaccount.last_name_input)

    def is_email_input_display(self):
        return self.func.is_displayed(self.aeropay_newaccount.email_input)

    def is_cellphone_input_display(self):
        return self.func.is_displayed(self.aeropay_newaccount.cellphone_input)

    def is_new_password_input_display(self):
        return self.func.is_displayed(self.aeropay_newaccount.new_password_input)

    def is_confirm_password_input_display(self):
        return self.func.is_displayed(self.aeropay_newaccount.confirm_password_input)

    def is_accept_terms_bt_display(self):
        return self.func.is_displayed(self.aeropay_newaccount.accept_terms_bt)

    def is_continue_bt_display(self):
        return self.func.is_displayed(self.aeropay_newaccount.continue_bt)

    """Click functions for Aeropay Create New Account"""

    def firstname_input_click(self):
        return self.func.click(self.aeropay_newaccount.first_name_input)

    def lastname_input_click(self):
        return self.func.click(self.aeropay_newaccount.last_name_input)

    def email_input_click(self):
        return self.func.click(self.aeropay_newaccount.email_input)

    def cellphone_input_click(self):
        return self.func.click(self.aeropay_newaccount.cellphone_input)

    def new_password_input_click(self):
        return self.func.click(self.aeropay_newaccount.new_password_input)

    def confirm_password_input_click(self):
        return self.func.click(self.aeropay_newaccount.confirm_password_input)

    def accept_terms_bt_click(self):
        return self.func.click(self.aeropay_newaccount.accept_terms_bt)

    def continue_bt_click(self):
        return self.func.click(self.aeropay_newaccount.continue_bt)

    """Enter text functions for Aeropay Create New Account"""

    def enter_firstname_text(self, text):
        return self.func.enter_text(self.aeropay_newaccount.first_name_input, text)

    def enter_lastname_text(self, text):
        return self.func.enter_text(self.aeropay_newaccount.last_name_input, text)

    def enter_cellphone_text(self, text):
        return self.func.enter_text(self.aeropay_newaccount.cellphone_input, text)

    def enter_email_text(self, text):
        return self.func.enter_text(self.aeropay_newaccount.email_input, text)

    def enter_new_password_text(self, text):
        return self.func.enter_text(self.aeropay_newaccount.new_password_input, text)

    def enter_confirm_password_text(self, text):
        return self.func.enter_text(self.aeropay_newaccount.confirm_password_input, text)

