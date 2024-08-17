from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num1 = int(num1.text)
    print(num1)
    num2 = browser.find_element(By.ID, "num2")
    num2 = int(num2.text)
    sum = str(num1 + num2)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sum)

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()