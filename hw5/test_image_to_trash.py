import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_drag_and_drop_with_popups(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    # Согласие на куки
    button_first = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-button.fc-cta-consent.fc-primary-button"))
    )
    button_first.click()

    target_iframe = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "demo-frame"))
            )
    driver.switch_to.frame(target_iframe)

    # Что перетаскиваем:
    source = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#gallery li"))
    )
    # Куда перетаскиваем:
    target = driver.find_element(By.CLASS_NAME, "ui-widget-content.ui-state-default.ui-droppable")

    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()
    sleep(3)

    remaining_photos = driver.find_elements(By.CSS_SELECTOR, "ul#gallery li")
    trash_photos = driver.find_elements(By.CSS_SELECTOR, "#trash ul li")

    print(f"\nФотографий осталось: {len(remaining_photos)}")
    print(f"Фотографий в корзине: {len(trash_photos)}")

    assert len(trash_photos) == 1, f"В корзине должна быть одна фотография, но найдено {len(trash_photos)}"
    assert len(
        remaining_photos) == 3, f"В основной области должно остаться 3 фотографии, но найдено {len(remaining_photos)}"


    driver.switch_to.default_content()

    print("Тест пройден: фотография успешно перемещена в корзину")

