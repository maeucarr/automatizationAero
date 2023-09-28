import time
import pytest
from Pages.Aeropay_LoginPage import Aeropay_LoginPage
from TestCases.baseTest import BaseTest
from utilities.custom_logger import LogGen
from utilities.readProperties import ReadConfig
from utilities.utils import utils

# Read data from CSV
data_list = utils.read_data_from_csv()

# Remove the header (first row) if it exists
if data_list and data_list[0] == ['email', 'password']:
    data_list = data_list[1:]


class Test_Aeropay_LoginPage(BaseTest):

    @pytest.mark.parametrize("data_row", data_list)
    def test_Aeropay_incorrect_login(self, data_row):
        email, password = data_row
        # test case for login flow
        logger = LogGen.loggen()
        logger.info("************Test_001_Incorrect_Login_Functionality************")
        logger.info("************Test the login************")
        login = Aeropay_LoginPage(self.driver)
        assert login.is_email_input_display() is True, "The email input is not displayed"
        logger.info("The email input is displayed correctly")
        login.email_input_click()
        login.enter_email_text(email)
        login.password_input_click()
        login.enter_password_text(password)
        login.signin_button_click()
        assert login.get_error_message_text() == "Incorrect username or password.", \
            "The error message is not correct"
        time.sleep(5)
        logger.info("************Test_001_Incorrect_Login_Functionality is successful************")

    @pytest.mark.skip(reason="The case is skipped for now as it is not required")
    def test_Aeropay_login(self):
        # test case for login flow
        logger = LogGen.loggen()
        logger.info("************Test_002_Login_Functionality************")
        logger.info("************Execute a Successful Login************")
        login = Aeropay_LoginPage(self.driver)
        time.sleep(1)
        assert login.is_email_input_display() is True, "The email input is not displayed"
        logger.info("The email input is displayed correctly")
        login.email_input_click()
        time.sleep(1)
        login.enter_email_text(ReadConfig.get_user_name())
        login.password_input_click()
        login.enter_password_text(ReadConfig.get_user_password())
        login.signin_button_click()
        time.sleep(10)
        logger.info("************Test_002_Login_Functionality is successful************")
