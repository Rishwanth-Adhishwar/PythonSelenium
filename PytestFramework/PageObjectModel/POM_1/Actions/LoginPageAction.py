from Pages.LoginPage import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPageAction:

    def __init__(self, driver):

        self.driver = driver
        self.lp = LoginPage(driver)
        self.wait = WebDriverWait(driver, 15)

    def login(self, email, password):

        self.wait.until(ec.visibility_of_element_located(self.lp.emailInput)).send_keys(
            email
        )

        self.driver.find_element(*self.lp.passwordInput).send_keys(password)

        self.driver.find_element(*self.lp.submitLogin).click()

    def click_Rcontinue(self):
        self.wait.until(ec.visibility_of_element_located(self.lp.registerAcc)).click()
