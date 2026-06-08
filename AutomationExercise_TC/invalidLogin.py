from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

driver =webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")
wait=WebDriverWait(driver,15)
loginbtn = wait.until(
    ec.visibility_of_element_located(
        (By.XPATH, "//a[@href='/login']")
    )
)
loginbtn.click()
wait.until(
    ec.visibility_of_element_located(
        (By.XPATH, "//input[@data-qa='login-email']")
    )
).send_keys("tommy@gmail.com")

driver.find_element(
    By.XPATH,
    "//input[@data-qa='login-password']"
).send_keys("tommy2k")

driver.find_element(
    By.XPATH,
    "//button[@data-qa='login-button']"
).click()
actual=wait.until(ec.visibility_of_element_located((By.XPATH,"//form[@action='/login']/child::p"))).text
try:
    assert actual=="Your email or password is incorrect!"
    print("Error Message Thrown Successfully")
except AssertionError as e:
    print(e)
