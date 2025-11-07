import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.quit()


def test_button_text_updated(driver):
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.clear()
    input_field.send_keys("ITCH")
    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()
    wait = WebDriverWait(driver, 2)
    new_button_text = wait.until(EC.visibility_of_element_located((By.ID, "updatingButton")))
    assert new_button_text.text == "ITCH"