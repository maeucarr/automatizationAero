from selenium.webdriver.common.by import By


class Aeropay_CreateNewAccount:

    first_name_input = (By.XPATH, "//input[@id='r_name_first']")
    last_name_input = (By.XPATH, "//input[@id='r_name_last']")
    cellphone_input = (By.XPATH, "//input[@id='r_phone']")
    email_input = (By.XPATH, "//input[@id='r_email']")
    new_password_input = (By.XPATH, "//input[@id='r_password']")
    confirm_password_input = (By.XPATH, "//input[@id='r_password_confirmation']")
    accept_terms_bt = (By.XPATH, "//input[@id='accept-terms']")
    continue_bt = (By.XPATH, "//input[@name='continue']")
