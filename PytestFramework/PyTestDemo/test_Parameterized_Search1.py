
from time import sleep

import pytest
from selenium import webdriver


@pytest.mark.parametrize("browser",[('chrome'),('firefox')])
@pytest.mark.parametrize("urlLink",[('https://www.flipkart.com/'),('https://www.amazon.com/')])
def test_para_1(browser,urlLink):
    if browser=='chrome':
        options=webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver=webdriver.Chrome(options=options)
    if browser=='firefox':
        options=webdriver.FirefoxOptions()
        options.add_argument("--headless=new")
        driver=webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get(urlLink)
    print(driver.title+"\n")
    sleep(5)
    driver.close()
    