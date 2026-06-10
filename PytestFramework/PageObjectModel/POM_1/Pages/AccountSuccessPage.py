from selenium.webdriver.common.by import By


class AccountSuccessPage:
    def __init__(self, driver):
        self.driver = driver
        self.rsuccess = (By.XPATH, "//div[@id='content']/child::h1")
