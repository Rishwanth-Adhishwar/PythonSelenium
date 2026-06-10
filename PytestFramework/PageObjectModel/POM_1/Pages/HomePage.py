from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):

        self.driver = driver

        self.myAccBtn = (By.XPATH, "//a[@title='My Account']")

        self.loginBtn = (
            By.XPATH,
            "//li[@class='dropdown open']/child::ul/li/a[text()='Login']",
        )
        self.searchBar = (By.XPATH, "//input[@name='search']")
        self.search = (By.XPATH, "//span[@class='input-group-btn']/child::button")
