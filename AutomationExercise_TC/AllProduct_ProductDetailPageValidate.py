import select

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

driver.get("https://automationexercise.com/")

driver.find_element(
    By.XPATH,
    value="//ul[@class='nav navbar-nav']/child::li/a[@href='/products']",
).click()

a1 = wait.until(
    ec.visibility_of_element_located((By.XPATH, "//h2[@class='title text-center']"))
).text

try:
    assert a1.__contains__("All Products")
    print("Product Page Displayed Successfully")

except AssertionError as e:
    print(e)

l = driver.find_elements(
    By.XPATH,
    "//div[@class='features_items']/child::div[@class='col-sm-4']",
)

try:
    assert len(l) == 34
    print("Products lists is displayed")

except AssertionError as e:
    print(e)

product = wait.until(
    ec.presence_of_element_located(
        (
            By.XPATH,
            "//div[@class='choose']/child::ul/li/a[@href='/product_details/1']",
        )
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    product,
)

driver.execute_script(
    "arguments[0].click();",
    product,
)

a2 = wait.until(ec.visibility_of_element_located((By.XPATH, "//span/button"))).text

try:
    assert a2.__contains__("Add to cart")
    print("First Product details is displayed")

except AssertionError as e:
    print(e)

a3 = driver.find_element(
    By.XPATH,
    "//div[@class='product-information']/child::h2",
).text

try:
    assert a3.__contains__("Blue Top")
    print("ProductName Displayed")

except AssertionError as e:
    print(e)

a4 = driver.find_element(
    By.XPATH,
    "//div[@class='product-information']/child::p",
).text

try:
    assert a4.__contains__("Category: Women > Tops")
    print("Product Category Displayed")

except AssertionError as e:
    print(e)

a5 = driver.find_element(
    By.XPATH,
    "//div[@class='product-information']/child::span/child::span",
).text

try:
    assert a5.__contains__("Rs. 500")
    print("Product Price Displayed")

except AssertionError as e:
    print(e)

a6 = driver.find_element(
    By.XPATH,
    "//div[@class='product-information']/child::p[2]/b",
).text

try:
    assert a6.__contains__("Availability:")
    print("Product Availability Displayed")

except AssertionError as e:
    print(e)

a7 = driver.find_element(
    By.XPATH,
    "//div[@class='product-information']/child::p[3]/b",
).text

try:
    assert a7.__contains__("Condition:")
    print("Product Condition Displayed")

except AssertionError as e:
    print(e)

a8 = driver.find_element(
    By.XPATH,
    "//div[@class='product-information']/child::p[4]/b",
).text


try:
    assert a8.__contains__("Brand:")
    print("Product Brand Displayed")

except AssertionError as e:
    print(e)

driver.quit()
