from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 15)

driver.get("https://automationexercise.com/")

loginbtn = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//a[@href='/login']"))
)
loginbtn.click()
wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@data-qa='login-email']"))
).send_keys("TamilK@gmail.com")

driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("tamil2k")

driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

logout = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//a[@href='/logout']"))
)

logout.click()
loginbtn = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//a[@href='/login']"))
)

lbs = loginbtn.text

try:
    assert lbs == "Signup / Login"
    print("Login and Logout done successfully")

except AssertionError:
    print("Login or Logout failed")

driver.quit()
