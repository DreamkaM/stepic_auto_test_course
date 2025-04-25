import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = " http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    image =browser.find_element(By.ID, "treasure")
    x_element = image.get_attribute("valuex")
    x = int(x_element)
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    checkb = browser.find_element(By.ID, "robotCheckbox")
    checkb.click()
    radiob = browser.find_element(By.ID, "robotsRule")
    radiob.click()
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


finally:

    time.sleep(30)

    browser.quit()

