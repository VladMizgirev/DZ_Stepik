from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x_value = x_element.get_attribute("valuex")
    y = calc(x_value)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)
    
    button = browser.find_element(By.ID, 'robotCheckbox')
    button.click()

    button = browser.find_element(By.ID, 'robotsRule')
    button.click()

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()