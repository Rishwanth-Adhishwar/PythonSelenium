import selenium 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/browser-windows")
wait=WebDriverWait(driver,15)
wait.until(ec.element_to_be_clickable((By.XPATH,"//button[@id='windowButton']"))).click()
p=driver.current_window_handle

for c in driver.window_handles:
    if c!=p:
        driver.switch_to.window(c)
wait.until(ec.visibility_of_element_located((By.XPATH,"//h1[@id='sampleHeading']")))
w=driver.find_element(By.XPATH,value="//h1[@id='sampleHeading']").text
print(w)
driver.switch_to.window(p)
print(driver.find_element(By.XPATH,value="//h1[@class='text-center']").text)