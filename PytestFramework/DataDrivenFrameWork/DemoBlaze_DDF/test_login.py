import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from configReader import config_read
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("up_and_down")
class TestLogin:
    def test_validLogin(self):
        uname = config_read("login credential", "uname")
        upass = config_read("login credential", "pass")
        wait = WebDriverWait(self.driver, 15)
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//a[@id='login2']")
            )
        ).click()
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//input[@id='loginusername']")
            )
        ).send_keys(uname)
        self.driver.find_element(
            By.XPATH, value="//input[@id='loginpassword']"
        ).send_keys(upass)

        wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//button[@onclick='logIn()']")
            )
        ).click()
        actual = wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//a[@id='nameofuser']")
            )
        ).text
        try:
            assert actual.__contains__("jolly")
            print("Login Successful")
        except AssertionError as a:
            print(a)

    def test_invalidLogin(self):
        uname = config_read("login credential", "u")
        upass = config_read("login credential", "p")
        wait = WebDriverWait(self.driver, 15)
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//a[@id='login2']")
            )
        ).click()
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//input[@id='loginusername']")
            )
        ).send_keys(uname)
        self.driver.find_element(
            By.XPATH, value="//input[@id='loginpassword']"
        ).send_keys(upass)

        wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//button[@onclick='logIn()']")
            )
        ).click()

        wait.until(expected_conditions.alert_is_present())
        actual = self.driver.switch_to.alert.text

        try:
            assert actual.__contains__("hello")
            print("A warning Pop up displayed")
        except AssertionError as a:
            print(a)
