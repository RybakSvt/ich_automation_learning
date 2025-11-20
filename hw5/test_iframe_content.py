import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_text_in_iframe(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)

    # Получаем весь текст body
    body = driver.find_element(By.TAG_NAME, "body")
    full_text = body.text

    # Проверяем что body отображается и содержит нужный текст
    assert body.is_displayed(), "Body не отображается"

    target_text = "semper posuere integer et senectus justo curabitur."
    assert target_text in full_text, f"Текст '{target_text}' не найден в содержимом iframe"

    print("Текст успешно найден и отображается в iframe.")


# Текст находится в iframe, но он разбит на несколько элементов, поэтому поиск по всему
# содержимому работает, а поиск по отдельным элементам - нет. Body содержит весь видимый
# текст, включая нужную фразу, поэтому проверка через body.text успешна.



