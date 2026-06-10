from Pages.AccountPage import AccountPage

from selenium.webdriver.support.wait import WebDriverWait


from selenium.webdriver.support import expected_conditions as ec


class AccountPageAction:

    def __init__(self, driver):

        self.driver = driver
        self.ap = AccountPage(driver)
        self.wait = WebDriverWait(driver, 15)

    def success_login(self):

        actual = self.wait.until(
            ec.visibility_of_element_located(self.ap.accuSuccessLogin)
        ).text

        return "My Account" in actual
