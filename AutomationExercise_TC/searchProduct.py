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

driver.find_element(By.XPATH, value="//input[@name='search']").send_keys("tshirt")
driver.find_element(By.XPATH, value="//button[@id='submit_search']").click()

s = wait.until(
    ec.visibility_of_element_located((By.XPATH, "//h2[@class='title text-center']"))
).text
try:
    assert s.__contains__("SEARCHED PRODUCTS")
    print("Search Results Came")
except AssertionError as a:
    print(a)

products = driver.find_elements(
    By.XPATH, value="//div[@class='productinfo text-center']/child::p"
)
c = 0
for i in products:
    if "Tshirt" in i.text:
        c += 1
    elif "T SHIRT" in i.text:
        c += 1
    elif "T-Shirt" in i.text:
        c += 1
    elif "T-Shirts" in i.text:
        c += 1
try:
    assert c == 6
    print("All Products Matches Search Results")
except AssertionError as e:
    print(e)
