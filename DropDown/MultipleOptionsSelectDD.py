import select
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
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//select[@id='ide']")))
s=Select(d.find_element(By.XPATH,value="//select[@id='ide']"))
s.is_multiple
s.select_by_index(1)
s.select_by_value("vs")
s.select_by_visible_text("NetBeans")
w=s.all_selected_options
print("All Selected optionS:")
for i in w:
    print(i.text)
time.sleep(3)
s.deselect_by_index(1)
s.deselect_all()