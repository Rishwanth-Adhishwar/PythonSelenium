from selenium import webdriver
from selenium.webdriver.common.by import By


def setup_function(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://tutorialsninja.com/demo/")


def teardown_function(function):
    driver.quit()


def test_validproduct():
    driver.find_element(By.NAME, value="search").send_keys("HP")
    driver.find_element(
        By.XPATH, value="//button[contains(@class,'btn-default')]"
    ).click()
    assert driver.find_element(By.LINK_TEXT, value="HP LP3065").is_displayed()
    print("Displayed")


def test_invalidproduct():
    driver.find_element(By.NAME, value="search").send_keys("Honda")
    driver.find_element(
        By.XPATH, value="//button[contains(@class,'btn-default')]"
    ).click()
    etext = "There is no produ that matches the search criteria."
    assert driver.find_element(
        By.XPATH, value="//input[@id='button-search']/following-sibling::p"
    ).text.__eq__(etext)
    print("m1")


def test_noproduct():
    driver.find_element(By.NAME, value="search").send_keys("")
    driver.find_element(
        By.XPATH, value="//button[contains(@class,'btn-default')]"
    ).click()
    etext = "There is no product that matches the search criteria."
    assert driver.find_element(
        By.XPATH, value="//input[@id='button-search']/following-sibling::p"
    ).text.__eq__(etext)
    print("m2")
