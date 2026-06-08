import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/alertsdemo.html")
wait=WebDriverWait(driver,15)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//h1[@itemprop='name']")))
btn=driver.find_element(By.CSS_SELECTOR,value="#confirmBox")
btn.click()
wait.until(expected_conditions.alert_is_present())
time.sleep(5)
# driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()