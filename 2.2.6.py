from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    browser.execute_script("window.scrollBy(0, 100);")

    #button = browser.find_element(By.ID, "peopleRule")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #button.click()

    button = browser.find_element(By.ID, 'robotCheckbox')
    button.click()

    button = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    button.click()

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()