#(1)Ans:Web Driver is a component that allows us to communicate with web browsers and automate interactions with web elements.

#(8)Ans: There are 8 types of locators in selenium :ID , NAME,TAGNAME,CLASSNAME,LINK TEXT,PARTIAL LINK TEXT,XAPTH,CSS SELECTOR

#(2) Ans: Selective drop down :
'''Exa :
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
var=driver.find_element(By.TAG_NAME,'select')
time.sleep(2)
Select(var).select_by_index(1)
or
Select(var).select_by_value('option2')
or
Select(var).select_by_visible_text('Option3')
time.sleep(3)'''

#(3)ANS : Auto suggestive dropdown
'''Exa: 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element(By.ID,'autocomplete').send_keys('au')
time.sleep(3)
var=driver.find_elements(By.XPATH,'//ul/li[@class="ui-menu-item"]')
#print(len(var))
for i in var:
    if i.text=='Palau':
        i.click()
        break
    print(i.text)'''

#(4) Window Handles:
'''Exa : 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element(By.LINK_TEXT,'Open Tab').click()
time.sleep(2)
driver.find_element(By.ID,'openwindow').click()
time.sleep(2)
var=driver.window_handles
driver.switch_to.window(var[1])
time.sleep(3)
driver.switch_to.window(var[2])
time.sleep(2)
driver.switch_to.window(var[0])'''

#(9) Ans:
#Exa:
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
table = driver.find_element(By.XPATH,"//table[@name='courses']")
time.sleep(3)
heading=table.find_element(By.XPATH,"//th[text()='Price']")
print(heading.text)
time.sleep(2)
value=table.find_element(By.XPATH,'//table[1]/tbody/tr[4]/td[3]')
print(value.text)'''


#(10)Ans:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.nseindia.com/')
driver.find_element()