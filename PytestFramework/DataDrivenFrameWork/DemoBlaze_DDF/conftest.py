import pytest
from selenium import webdriver
from configReader import config_read


@pytest.fixture()
def up_and_down(request):
    bro = config_read("basic info", "browser")
    if bro == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    else:
        print("Invalid Browser")
    driver.maximize_window()
    driver.implicitly_wait(15)
    url = config_read("basic info", "url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()
