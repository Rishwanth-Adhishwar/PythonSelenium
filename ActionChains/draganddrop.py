import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://leafground.com/drag.xhtml")
act=ActionChains(driver)
de=driver.find_element(By.XPATH,value="//div[@id='form:conpnl_header']")
act.click_and_hold(de).move_by_offset(xoffset=300,yoffset=0).release().perform()
time.sleep(5)
