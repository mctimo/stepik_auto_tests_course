import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = browser.find_element(By.ID, "price")
WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element(price, "$100"))

btn = browser.find_element(By.ID, "book")

btn.click()


x = browser.find_element(By.ID, "input_value").text
x = calc(x)

answer = browser.find_element(By.ID, "answer")
answer.send_keys(x)

btn = browser.find_element(By.ID, "solve")
btn.click()

time.sleep(20)

