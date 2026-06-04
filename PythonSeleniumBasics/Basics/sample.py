import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.google.com/")
print("Title Of Browser:", driver.title)
time.sleep(2)
driver.save_screenshot("Google.png")
driver.find_element(By.XPATH, "//textarea[@name='q']").send_keys("Selenium")
time.sleep(5)
searchButton = driver.find_element(
    By.XPATH, "//div[@class='T14B5e iThwld']/child::center/child::input[1]"
)
if searchButton.is_enabled():
    searchButton.click()
time.sleep(3)
driver.save_screenshot("Selenium.png")
time.sleep(5)
driver.close()
