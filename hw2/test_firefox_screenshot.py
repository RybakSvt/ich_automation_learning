from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver

    driver.quit()


def test_payment_methods(browser):
    browser.get("https://itcareerhub.de/ru")
    sleep(2)

    payment_link = browser.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_link.click()
    sleep(2)

    browser.save_screenshot("payment_methods.png")
    print("Скриншот сохранен")