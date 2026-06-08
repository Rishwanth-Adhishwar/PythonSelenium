from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
wait = WebDriverWait(driver, 15)
lpText = driver.find_element(By.XPATH, "//a[@href='/login']").text

try:
    assert lpText == "Signup / Login"
    print("Website Launched Successfully")

except AssertionError:
    print("Launch Failed")

act = ActionChains(driver)
subscription = driver.find_element(By.XPATH, value="//input[@id='susbscribe_email']")
act.scroll_to_element(subscription)
subscription.send_keys("rishwa@gmail.com")
driver.find_element(By.XPATH, value="//button[@id='subscribe']").click()
actual = wait.until(
    ec.visibility_of_element_located(
        (By.XPATH, "//div[@id='success-subscribe']/child::div")
    )
).text

try:
    assert actual.__contains__("You have been successfully subscribed!")
    print("Subscribed Sucessfully")
except AssertionError as e:
    print(e)
