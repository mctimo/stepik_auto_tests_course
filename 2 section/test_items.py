import time as t
from datetime import datetime
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    t.sleep(30)
    browser.find_element(By.TAG_NAME, "button")