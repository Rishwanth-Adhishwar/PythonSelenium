import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")
lpText = driver.find_element(By.XPATH, "//a[@href='/login']").text

try:
    assert lpText == "Signup / Login"
    print("Website Launched Successfully")

except AssertionError:
    print("Launch Failed")

# Open Login Page
driver.find_element(By.XPATH, "//a[@href='/login']").click()

# Signup Details
driver.find_element(By.XPATH, "//input[@data-qa='signup-name']").send_keys("TamilK")

driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(
    "TamilK123456@gmail.com"
)
driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

actual = driver.find_element(By.XPATH, value="//form[@action='/signup']/child::p").text
try:
    assert actual == "Email Address already exist!"
    print("Email Already Registered Message Showed")

except AssertionError as e:
    print(e)
