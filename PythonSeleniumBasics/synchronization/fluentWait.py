from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,15,poll_frequency=5,ignored_exceptions=[NoSuchElementException])
driver.get("https://automationexercise.com/")
driver.find_element(By.XPATH,value="//a[@href='/test_cases']/child::i").click()
wait.until(EC.visibility_of_element_located((By.XPATH,"//h2/b")))
actual=driver.find_element(By.XPATH,value="//h2/b").text

try:
    assert actual=="TEST CASES"
    print("Test Case page is Visited Successfully")
except(AssertionError):
    print("Test Case page is Not Displayed")
