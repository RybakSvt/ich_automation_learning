from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://itcareerhub.de/ru/contact-us#popup-close")
    yield driver
    driver.quit()



def test_text_displayed(driver):

    # 1. Найти и кликнуть по иконке телефонной трубки
    phone_icon = driver.find_element(
        By.CSS_SELECTOR, ".t396__elem.tn-elem.tn-elem__11949824661710153310161  img"
    )
    phone_icon.click()

    # 2. Дождаться появления текста
    sleep(3)

    # 3. Проверить отображение текста
    expected_text = "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"
    text_element = driver.find_element(
        By.CSS_SELECTOR, ".t396__elem.tn-elem.tn-elem__11949836861711363912027 div"
    )
    assert text_element.text == expected_text

