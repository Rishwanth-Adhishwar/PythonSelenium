from Pages.HomePage import HomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePageAction:

    def __init__(self, driver):

        self.driver = driver
        self.hp = HomePage(driver)
        self.wait = WebDriverWait(driver, 15)

    def click_my_account(self):

        self.wait.until(ec.element_to_be_clickable(self.hp.myAccBtn)).click()

    def click_login(self):

        self.wait.until(ec.element_to_be_clickable(self.hp.loginBtn)).click()

    def pass_word_SB(self, w):
        self.wait.until(
            ec.visibility_of_element_located((self.hp.searchBar))
        ).send_keys(w)
        self.driver.find_element(*self.hp.search).click()
