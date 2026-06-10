from Pages.HomePage import HomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Pages.searchpage import SearchPage


class SearchPageAction:

    def __init__(self, driver):
        self.driver = driver
        self.hp = HomePage(driver)
        self.sp = SearchPage(driver)
        self.wait = WebDriverWait(driver, 15)

    def search_result(self):

        actual = self.wait.until(
            ec.visibility_of_element_located((self.sp.searchResult))
        ).text

        return "iphone" in actual
