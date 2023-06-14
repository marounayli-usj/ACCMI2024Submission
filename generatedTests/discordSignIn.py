# Import the webdriver and keys modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import locator as lc
import time 
import base64
import io
from PIL import Image
import socketio


driver = webdriver.Chrome()



def send_screenshot(sio):
    # Take a screenshot using Selenium
    screenshot = driver.get_screenshot_as_png()

    # Convert the PNG image to a PIL Image object
    img = Image.open(io.BytesIO(screenshot))

    # Convert the PIL Image to a base64-encoded string
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

    # Send the base64-encoded string to the server using SocketIO
    sio.emit("images",{'image':img_str})


# Navigate to the Google website
driver.maximize_window()
driver.get('https://discord.com')
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

def main():
    sio = socketio.Client()
    sio.connect('http://localhost:5555')

    elem = find_elem({'tag': 'button', 'value': 'Login', 'attrs': {'class': 'login-button', 'position': 'top-right'}})
    
    elem.click()
    
    time.sleep(3)
    send_screenshot(sio)

    elem = find_elem({'tag': 'input', 'value': '', 'attrs': {'name': 'username', 'placeholder': 'username'}})
    
    elem.send_keys("username")
    
    time.sleep(3)
    send_screenshot(sio)

    elem = find_elem({'tag': 'input', 'value': '', 'attrs': {'type': 'password', 'placeholder': 'password'}})
    
    elem.send_keys("password")
    
    time.sleep(3)
    send_screenshot(sio)

    elem = find_elem({'tag': 'button', 'value': 'Login', 'attrs': {'type': 'submit', 'value': 'Login'}})
    
    elem.click()
    
    time.sleep(3)
    send_screenshot(sio)


