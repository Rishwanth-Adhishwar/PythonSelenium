import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://www.hyrtutorials.com/p/alertsdemo.html")

driver.execute_script("alert('welcome')")
wait.until(EC.alert_is_present())
driver.switch_to.alert.accept()

driver.execute_script("prompt('Enter Your Favorite Color:')")
wait.until(EC.alert_is_present())

alrt = driver.switch_to.alert
alrt.send_keys("purple")
alrt.accept()

driver.execute_script("confirm('Are you sure want to delete it?')")
wait.until(EC.alert_is_present())
driver.switch_to.alert.accept()

driver.quit()