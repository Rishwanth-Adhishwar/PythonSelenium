import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.hyrtutorials.com/p/alertsdemo.html")

wait = WebDriverWait(driver, 15)

driver.find_element(By.ID, "promptBox").click()

wait.until(EC.alert_is_present())

alrt = driver.switch_to.alert

print(alrt.text)

alrt.send_keys("I am Rishwanth")

time.sleep(2)

alrt.accept()

print(driver.find_element(By.ID, "output").text)

time.sleep(2)

driver.quit()