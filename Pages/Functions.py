from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class Functions:
    """The BasePage class holds all common functionality  across the app.
        Also provides a nice wrapper when dealing with selenium/appium functions that may
        not be easy to understand.
        """

    def __init__(self, driver):
        """This function is called everytime a new object of the base class is created"""
        self.driver = driver

    def is_displayed(self, by_locator, time_out_in_seconds=40) -> bool:
        """Performs is _displayed on web element whose locator is passed to it"""
        try:
            return WebDriverWait(self.driver, time_out_in_seconds).until(
                EC.visibility_of_element_located(by_locator)).is_displayed()
        except TimeoutException:
            return False

    def click(self, by_locator, time_out_in_seconds=20):
        """Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, time_out_in_seconds).until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator: By, text: str, time_out_in_seconds=10):
        """Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        WebDriverWait(self.driver, time_out_in_seconds).until(EC.visibility_of_element_located(by_locator)) \
            .send_keys(text)

    def enter_key(self, by_locator: By, time_out_in_seconds=10):

        """Performs clear on web element whose locator is passed to it"""
        WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def get_text(self, by_locator, time_out_in_seconds=10) -> str:
        """Take in the by_locator and returns the elements text"""
        return WebDriverWait(self.driver, time_out_in_seconds).until(
            EC.visibility_of_element_located(by_locator)).text
