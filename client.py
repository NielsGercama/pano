import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--start-maximized")

browser = webdriver.Chrome()
browser.get('http://127.0.0.1:5000/')

xinput = browser.find_element(By.ID, "x")
yinput = browser.find_element(By.ID, "y")
button = browser.find_element(By.ID, "submitbutton")

while True:
    x = input("x: ")
    y = input("y: ")

    if x == "exit" or y == "exit":
        break

    xinput.clear()
    xinput.send_keys(x)
    yinput.clear()
    yinput.send_keys(y)
    button.click()