import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = " http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    span1 = browser.find_element(By.ID, "num1").text
    span2 = browser.find_element(By.ID, "num2").text

    x = str(int(span1)+int(span2))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(x)
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

