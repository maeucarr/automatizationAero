from selenium.webdriver.common.by import By


class Aeropay_Login:

    email_input = (By.XPATH, "//input[@id='l_email']")
    password_input = (By.XPATH, "//input[@id='l_password']")
    signin_bt = (By.XPATH, "//input[@name='signIn']")
    reset_password = (By.XPATH, "//a[normalize-space()='Reset password']")
    create_account = (By.XPATH, "//a[normalize-space()='Create an account']")
    error_message = (By.XPATH, "//div[@class='feedback']")
