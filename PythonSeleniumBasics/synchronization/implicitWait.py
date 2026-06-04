import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://automationexercise.com/")
driver.maximize_window()
driver.implicitly_wait(15)
print("Title:", driver.title)
lpText = driver.find_element(By.XPATH, value="//a[@href='/login']").text
try:
    assert lpText == "Signup / Login"
    print("Website Launched Successfully")
except AssertionError:
    print(AssertionError.mro)

driver.find_element(By.XPATH, value="//a[@href='/login']").click()
driver.find_element(By.XPATH, value="//input[@data-qa='signup-name']").send_keys(
    "TamilK"
)
driver.find_element(By.XPATH, value="//input[@data-qa='signup-email']").send_keys(
    "TamilK@gmail.com"
)
driver.find_element(By.XPATH, value="//button[@data-qa='signup-button']").click()
driver.find_element(By.XPATH, value="//input[@data-qa='password']").send_keys("tamil2k")
driver.find_element(By.XPATH, value="//input[@data-qa='first_name']").send_keys("Tamil")
driver.find_element(By.XPATH, value="//i    nput[@data-qa='last_name']").send_keys("Kumar")
driver.find_element(By.XPATH, value="//input[@data-qa='address']").send_keys(
    "Salem,Bypass"
)
driver.find_element(By.XPATH, value="//input[@data-qa='state']").send_keys("Tamilnadu")
driver.find_element(By.XPATH, value="//input[@data-qa='city']").send_keys("Salem")
driver.find_element(By.XPATH, value="//input[@data-qa='zipcode']").send_keys("636001")
driver.find_element(By.XPATH, value="//input[@data-qa='mobile_number']").send_keys(
    "9876543210"
)
driver.find_element(By.XPATH, value="//button[@data-qa='create-account']").click()
accsuccess = driver.find_element(
    By.XPATH, value="//h2[@data-qa='account-created']"
).text

try:
    assert driver.current_url == "https://automationexercise.com/account_created"
    print("Account Registered  Successfully")
except AssertionError:
    driver.save_screenshot("failed1.png")
    print(AssertionError.mro)
