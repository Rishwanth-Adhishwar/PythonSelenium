from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
wait=WebDriverWait(driver,15,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
wait.until(ec.element_to_be_clickable((By.XPATH,"//ul[@class='nav navbar-nav']/child::li[8]"))).click()
wait.until(ec.visibility_of_element_located((By.XPATH,"//input[@name='name']"))).send_keys("Rishwa")
driver.find_element(By.XPATH,value="//input[@name='email']").send_keys("rishwa@gmail.com")
driver.find_element(By.XPATH,value="//input[@name='subject']").send_keys("Regarding Order Return")
driver.find_element(By.XPATH,value="//textarea[@name='message']").send_keys("I had Returned Order, But I didn't get any update on it kindly contuct us")
driver.find_element(By.XPATH,value="//input[@name='submit']").click()
wait.until(ec.alert_is_present())
driver.switch_to.alert.accept()
actual=wait.until(ec.visibility_of_element_located((By.XPATH,"//div[@class='status alert alert-success']"))).text
try:
    assert actual=="Success! Your details have been submitted successfully."
    print("Contact Message Sent Successfully")
except AssertionError as e:
    print(e)
