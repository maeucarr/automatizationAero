import time
import pytest
from Pages.Aeropay_LoginPage import Aeropay_LoginPage
from Pages.Aeropay_CreateNewAccountPage import Aeropay_CreateNewAccountPage
from TestCases.baseTest import BaseTest
from utilities.custom_logger import LogGen
from utilities.utils import utils

# Read data from CSV
data_list2 = utils.read_data_from_csv_create_user()

# Remove the header (first row) if it exists
if data_list2 and data_list2[0] == ['firstname', 'lastname', 'cellphone', 'email', 'password', 'confirmpassword']:
    data_list2 = data_list2[1:]


class Test_Aeropay_Create_Account(BaseTest):

    @pytest.mark.parametrize("data_row", data_list2)
    def test_Aeropay_incorrect_create_user(self, data_row):
        firstname, lastname, cellphone, email, password, confirmpassword = data_row
        # test case for login flow
        logger = LogGen.loggen()
        logger.info("************Test_001_Incorrect_Create_User_Functionality************")
        logger.info("************Test incorrect create user************")
        login = Aeropay_LoginPage(self.driver)
        create_user = Aeropay_CreateNewAccountPage(self.driver)
        assert login.is_create_account_button_display() is True, "The button is not displayed"
        login.create_account_button_click()
        time.sleep(3)
        create_user.firstname_input_click()
        create_user.enter_firstname_text(firstname)
        create_user.lastname_input_click()
        create_user.enter_lastname_text(lastname)
        create_user.cellphone_input_click()
        create_user.enter_cellphone_text(cellphone)
        create_user.email_input_click()
        create_user.enter_email_text(email)
        create_user.new_password_input_click()
        create_user.enter_new_password_text(password)
        create_user.confirm_password_input_click()
        create_user.enter_confirm_password_text(confirmpassword)
        create_user.accept_terms_bt_click()
        create_user.continue_bt_click()
        time.sleep(7)
        logger.info("************Test_001_Incorrect_Login_Functionality is successful************")
