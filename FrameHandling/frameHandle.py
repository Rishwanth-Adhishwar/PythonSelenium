from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
#f=driver.find_element(By.XPATH,"//iframe[@id='iframe1']")
#driver.switch_to.frame(f)
#driver.switch_to.frame(1)
driver.switch_to.frame("iframe1")
print(driver.find_element(By.XPATH,"//a[text()='What is Selenium?']").text)
driver.switch_to.default_content()
driver.quit()