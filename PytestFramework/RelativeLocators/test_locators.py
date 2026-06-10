import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestRelativeLocators:

    def test_all_relative_locators(self):

        driver = webdriver.Chrome()
        driver.maximize_window()

        wait = WebDriverWait(driver, 15)

        driver.get("https://demoblaze.com/")

        wait.until(ec.element_to_be_clickable((By.ID, "login2"))).click()

        username = wait.until(
            ec.visibility_of_element_located((By.ID, "loginusername"))
        )

        username.send_keys("admin")

        password = driver.find_element(
            locate_with(By.TAG_NAME, "input").below(username)
        )
        password.send_keys("admin")

        user_again = driver.find_element(
            locate_with(By.TAG_NAME, "input").above(password)
        )

        print("Above Password =", user_again.get_attribute("id"))

        login_btn = wait.until(
            ec.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))
        ).click()

        wait.until(ec.invisibility_of_element_located((By.ID, "logInModal")))

        user_label = wait.until(ec.visibility_of_element_located((By.ID, "nameofuser")))

        print("Logged in user :", user_label.text)

        phone = wait.until(
            ec.visibility_of_element_located(
                (By.XPATH, "//a[text()='Samsung galaxy s6']")
            )
        )

        price = driver.find_element(locate_with(By.TAG_NAME, "h5").near(phone))

        print("Near Product Price:", price.text)

        cart = driver.find_element(By.ID, "cartur")

        home = driver.find_element(locate_with(By.TAG_NAME, "a").to_left_of(cart))

        print("Left Locator:", home.text)

        driver.quit()
