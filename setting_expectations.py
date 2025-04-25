import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = " http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    element=WebDriverWait(browser, 12).until(EC. text_to_be_present_in_element((By.ID, "price"), "$100"))
    button1=browser.find_element(By.ID, "book")
    button1.click()
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    span = browser.find_element(By.ID, "input_value")
    x = int(span.text)
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()