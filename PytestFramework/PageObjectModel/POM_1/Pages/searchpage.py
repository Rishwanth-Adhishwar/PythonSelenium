from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):

        self.driver = driver
        self.searchResult = (By.XPATH, "//div[@id='content']/h1")
