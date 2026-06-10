import pytest
from selenium import webdriver
from Utilities.configReader import get_Config_Data


@pytest.fixture()
def settingUp_and_Down(request):
    browser = get_Config_Data("basic info", "browser")
    url = get_Config_Data("basic info", "url")
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        request.cls.driver = driver
        yield
        driver.quit()
