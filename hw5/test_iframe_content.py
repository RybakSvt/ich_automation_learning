import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_text_in_iframe(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

    target_text = "semper posuere integer et senectus justo curabitur."

    body = driver.find_element(By.TAG_NAME, "body")
    assert target_text in body.text, "Элемент не найден"
    assert body.is_displayed(), "Текст не отображается"

    driver.switch_to.default_content()