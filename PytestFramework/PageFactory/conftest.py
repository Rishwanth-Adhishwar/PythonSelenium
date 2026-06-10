import pytest
from selenium import webdriver


@pytest.fixture()
def upAndDown(request):
    # bro = configReader.config_Read("basic info", "browser")
    # if bro == "chrome":
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome()
    # # else:
    #     print("Invalid Browser")
    driver.maximize_window()
    driver.implicitly_wait(15)
    # url = configReader.config_Read("basic info", "url")
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()
