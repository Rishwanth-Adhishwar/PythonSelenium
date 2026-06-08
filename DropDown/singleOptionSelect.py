import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


d=webdriver.Chrome()
d.maximize_window()
d.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")
wait=WebDriverWait(d,15)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//select[@id='course']")))
dd=d.find_element(By.XPATH,value="//select[@id='course']")
s=Select(dd)
a=s.options
for i in a:
    print(i.text)
# s.select_by_index(1)
# s.select_by_value("python")
s.select_by_visible_text("Javascript")
time.sleep(3)


