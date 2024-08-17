from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element(By.NAME, 'firstname')
    input.send_keys('Vlad')

    input = browser.find_element(By.NAME, 'lastname')
    input.send_keys('M')

    input = browser.find_element(By.NAME, 'email')
    input.send_keys('@')

    element = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()