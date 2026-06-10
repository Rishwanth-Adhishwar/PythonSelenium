from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.AccountSuccessPage import AccountSuccessPage


class AccountSuccessPageAction:
    def __init__(self, driver):
        self.driver = driver
        self.asp = AccountSuccessPage(driver)
        self.wait = WebDriverWait(driver, 15)

    def success_register(self):

        actual = self.wait.until(
            expected_conditions.visibility_of_element_located(self.asp.rsuccess)
        ).text

        return "Your Account Has Been Created!" in actual
