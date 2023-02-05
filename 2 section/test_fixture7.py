import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_guest_should_see_login_link(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    time.sleep(5)
    btn = browser.find_element(By.ID, "ember33")
    btn.click()

    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("Paranorm21")

    log_in = browser.find_element(By.CLASS_NAME, "btn-google")
    log_in.click()
    registered = browser.find_element(By.ID, "identifierId")
    registered.send_keys("timfenomen@gmail.com")

    time.sleep(5)
