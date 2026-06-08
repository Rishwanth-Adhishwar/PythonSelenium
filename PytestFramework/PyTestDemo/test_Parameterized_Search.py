import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('search_item',[('Selenium'),('pytest'),('Java')])
def test_googleSearch(search_item):
    driver=webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.find_element(By.NAME,value="q").send_keys(search_item)
    time.sleep(5)
    driver.find_element(By.CLASS_NAME,value="gNO89b").click()
    time.sleep(5)
    driver.close()