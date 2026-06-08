from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://thinking-tester-contact-list.herokuapp.com/")
wait=WebDriverWait(driver,15)
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='email']"))).send_keys("ra@gmail.com")
driver.find_element(By.XPATH,value="//input[@id='password']").send_keys("ra12345")
driver.find_element(By.XPATH,value="//button[@id='submit']").click()
wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@id='add-contact']")))
wait.until(EC.visibility_of_element_located((By.XPATH,"//table//tr")))
l=driver.find_elements(By.XPATH,value="//table//tr")
print('-'*150)
for i in l:
    print(i.text)
    print('-'*150)
    
name=input("Enter the name to Search:")
print('-'*150)
for i in l:
    if name in i.text:
        print(i.text)
        print('-'*150)
    

