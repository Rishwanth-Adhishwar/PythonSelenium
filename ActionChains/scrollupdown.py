from sqlite3 import Time
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
act=ActionChains(driver)
act.scroll_by_amount(0,700).perform()
act.reset_actions()
time.sleep(5)
e=driver.find_element(By.XPATH,value="//a[normalize-space()='Blogger']")
origin=ScrollOrigin.from_element(e)
act.scroll_from_origin(origin,0,700).perform()
act.reset_actions()
time.sleep(5)

