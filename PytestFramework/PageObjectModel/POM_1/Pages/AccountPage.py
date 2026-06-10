from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):

        self.driver = driver

        self.accuSuccessLogin = (
            By.XPATH,
            "//div[@id='content']/child::h2[text()='My Account']",
        )
