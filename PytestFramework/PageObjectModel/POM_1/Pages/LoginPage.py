from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):

        self.driver = driver

        self.emailInput = (By.XPATH, "//input[@name='email']")

        self.passwordInput = (By.XPATH, "//input[@name='password']")

        self.submitLogin = (By.XPATH, "//input[@type='submit']")

        self.registerAcc = (By.XPATH, "//div[@class='well']/child::a")
