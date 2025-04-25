import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import random,  time

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--start-maximized")

browser = webdriver.Chrome()
browser.get('https://nielsgercama.github.io/pano/panoviewer/')

xinput = browser.find_element(By.ID, "x")
yinput = browser.find_element(By.ID, "y")
button = browser.find_element(By.ID, "submitbutton")

while True:
    x = random.randint(-180, 180)
    y = random.randint(-90, 90)

    if x == "exit" or y == "exit":
        break

    xinput.clear()
    xinput.send_keys(x)
    yinput.clear()
    yinput.send_keys(y)
    button.click()

