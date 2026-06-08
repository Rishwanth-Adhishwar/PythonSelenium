import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Chrome Options
options = Options()
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-notifications")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://automationexercise.com/")
driver.implicitly_wait(15)

print("Title:", driver.title)

# Remove Ads / iframe if present
try:
    driver.execute_script("""
    var ads=document.querySelectorAll("iframe,.ads,.advertisement");
    ads.forEach(ad=>ad.remove());
    """)
except:
    pass

# Verify Website
lpText = driver.find_element(
    By.XPATH,
    "//a[@href='/login']"
).text

try:
    assert lpText == "Signup / Login"
    print("Website Launched Successfully")

except AssertionError:
    print("Launch Failed")

# Open Login Page
driver.find_element(
    By.XPATH,
    "//a[@href='/login']"
).click()

# Signup Details
driver.find_element(
    By.XPATH,
    "//input[@data-qa='signup-name']"
).send_keys("TamilK")

driver.find_element(
    By.XPATH,
    "//input[@data-qa='signup-email']"
).send_keys("TamilK123456@gmail.com")

driver.find_element(
    By.XPATH,
    "//button[@data-qa='signup-button']"
).click()

# Account Details
driver.find_element(
    By.XPATH,
    "//input[@data-qa='password']"
).send_keys("tamil2k")

driver.find_element(
    By.XPATH,
    "//input[@data-qa='first_name']"
).send_keys("Tamil")

driver.find_element(
    By.XPATH,
    "//input[@data-qa='last_name']"
).send_keys("Kumar")

driver.find_element(
    By.XPATH,
    "//input[@data-qa='address']"
).send_keys("Salem,Bypass")

driver.find_element(
    By.XPATH,
    "//input[@data-qa='state']"
).send_keys("Tamilnadu")

driver.find_element(
    By.XPATH,
    "//input[@data-qa='city']"
).send_keys("Salem")

driver.find_element(
    By.XPATH,
    "//input[@data-qa='zipcode']"
).send_keys("636001")

driver.find_element(
    By.XPATH,
    "//input[@data-qa='mobile_number']"
).send_keys("9876543210")

# Remove iframe again before clicking
try:
    frames = driver.find_elements(By.TAG_NAME, "iframe")

    for frame in frames:
        driver.execute_script("""
        arguments[0].remove();
        """, frame)

except:
    pass

# Create Account Button
createBtn = driver.find_element(
    By.XPATH,
    "//button[@data-qa='create-account']"
)

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    createBtn
)

time.sleep(2)

driver.execute_script(
    "arguments[0].click();",
    createBtn
)

# Validation
try:
    accsuccess = driver.find_element(
        By.XPATH,
        "//h2[@data-qa='account-created']"
    ).text

    assert accsuccess == "ACCOUNT CREATED!"

    print("Account Registered Successfully")

except:
    driver.save_screenshot("failed1.png")
    print("Registration Failed")

time.sleep(5)

driver.quit()
