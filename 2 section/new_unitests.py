import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def test_assert(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser: WebDriver = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, '//label[text()="First name*"]/following-sibling::input')
        input1.send_keys("Ivan")
        button = browser.find_element(By.XPATH, '//label[text()="Address:"]/following-sibling::input')
        button.click()
        input2 = browser.find_element(By.XPATH, '//label[text()="Last name*"]/following-sibling::input')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '//label[text()="Email*"]/following-sibling::input')
        input3.send_keys("asd@mail.com")
        input4 = browser.find_element(By.XPATH, '//label[text()="Phone:"]/following-sibling::input')
        input4.send_keys("89103568899")
        button = browser.find_element(By.XPATH, '//label[text()="Address:"]/following-sibling::input')
        button.click()

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_find_xpath(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser: WebDriver = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.ID, 'namename' )
        input1.send_keys("Ivan")
        button = browser.find_element(By.XPATH, '//label[text()="Address:"]/following-sibling::input')
        button.click()
        input2 = browser.find_element(By.XPATH, '//label[text()="Last name*"]/following-sibling::input')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '//label[text()="Email*"]/following-sibling::input')
        input3.send_keys("asd@mail.com")
        input4 = browser.find_element(By.XPATH, '//label[text()="Phone:"]/following-sibling::input')
        input4.send_keys("89103568899")
        button = browser.find_element(By.XPATH, '//label[text()="Address:"]/following-sibling::input')
        button.click()

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

