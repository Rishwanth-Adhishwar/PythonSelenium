from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 15)

driver.get("https://automationexercise.com/")

driver.find_element(
    By.XPATH,
    "//ul[@class='nav navbar-nav']/child::li/a[@href='/products']",
).click()

a1 = wait.until(
    ec.visibility_of_element_located((By.XPATH, "//h2[@class='title text-center']"))
).text

try:
    assert "All Products" in a1
    print("Product Page Displayed Successfully")

except AssertionError as e:
    print(e)

act = webdriver.ActionChains(driver)

addtocart = driver.find_element(
    By.XPATH,
    "//div[@class='productinfo text-center']/child::a[@data-product-id='1']",
)

act.move_to_element(addtocart).perform()

# only one click
driver.execute_script("arguments[0].click();", addtocart)

wait.until(
    ec.visibility_of_element_located(
        (
            By.XPATH,
            "//p[@class='text-center']/child::a[@href='/view_cart']",
        )
    )
).click()

actual = wait.until(
    ec.visibility_of_element_located(
        (
            By.XPATH,
            "//a[@href='/product_details/1']",
        )
    )
).text

try:
    assert "Blue Top" in actual
    print("Added Product is in cart Matched")

except AssertionError as e:
    print(e)

driver.quit()
