import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utilities.readProperties import ReadConfig


@pytest.fixture(scope="function")
def setup(request):
    # Chrome

    service_obj = Service('C:\AutomationDrivers\chromedriver.exe')
    #driver = webdriver.Chrome(service=service_obj)
    ###This block allows to keep the browser open while testing
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service_obj, options=options)
    base_url = ReadConfig.get_url()
    driver.get(base_url)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
