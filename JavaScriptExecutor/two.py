import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
button = driver.find_element(By.ID, value='alert1')
driver.execute_script("arguments[0].click()",button)
driver.switch_to.alert.accept
time.sleep(4)
driver.execute_script("history.go(0)")