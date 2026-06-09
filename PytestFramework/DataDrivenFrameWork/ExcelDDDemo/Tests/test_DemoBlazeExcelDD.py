import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Utility.excelReader import get_data
from Utility import logCreator


@pytest.mark.parametrize(
    "username,password",
    get_data("", "LoginDataPy"),
)
class Test_Logins:

    def test_validLogin(self, username, password):

        log = logCreator.log_generator()  # Create logger

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 15)

        try:
            self.driver.get("https://demoblaze.com/")
            log.info("Website Launched")

            wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()

            wait.until(
                EC.visibility_of_element_located((By.ID, "loginusername"))
            ).send_keys(username)

            log.info("Username entered")

            self.driver.find_element(By.ID, "loginpassword").send_keys(password)

            log.info("Password entered")

            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@onclick='logIn()']"))
            ).click()

            log.info("Clicked Login")

            actual = wait.until(
                EC.visibility_of_element_located((By.ID, "nameofuser"))
            ).text

            assert "Welcome" in actual

            log.info("Login Successful")

            self.driver.find_element(By.ID, "logout2").click()

        except Exception as e:

            try:
                wait.until(EC.alert_is_present())

                alert = self.driver.switch_to.alert

                print(alert.text)

                log.info(alert.text)

                alert.accept()

            except:
                log.info("Invalid Login Warning pop up thrown")

        finally:
            self.driver.quit()
