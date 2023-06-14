# Import the webdriver and keys modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import locator as lc
import time 
# Create a new Chrome browser
driver = webdriver.Chrome()

# Navigate to the Google website
driver.maximize_window()
driver.get('https://leetcode.com/')
time.sleep(3)

def find_elem(description):
    html_source_code = driver.execute_script("return document.body.innerHTML;")
    html_soup: BeautifulSoup = BeautifulSoup(html_source_code, 'html.parser')
    elem =  lc.Elem(description["tag"],description["attrs"],description["value"])
    xp = lc.get_xpath(html_soup,elem)
    res = driver.find_element(By.XPATH,xp)
    actions = ActionChains(driver)
    actions.move_to_element(res).perform()
    return res



create_account=find_elem({"tag":"a", "attrs":{"href":"signup"}, "value" :"Create Account"})
create_account.click()


time.sleep(10)


username=find_elem({"tag":"input", "attrs":{"placeholder":"username"}, "value" :""})
username.send_keys("marountestalpha")




pass1=find_elem({"tag":"input", "attrs":{"placeholder":"password"}, "value" :""})
pass1.send_keys("marountestalpha")



pass2=find_elem({"tag":"input", "attrs":{"placeholder":"confirm password"}, "value" :""})
pass2.send_keys("marountestalpha")



make_chart=find_elem({"tag":"input", "attrs":{"placeholder":"email address"}, "value" :""})
make_chart.send_keys("marountest@gmail.com")




time.sleep(10)
