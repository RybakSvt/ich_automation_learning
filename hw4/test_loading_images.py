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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    yield driver
    driver.quit()


def test_third_image_alt_attribute(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(lambda l: len(driver.find_elements(By.CSS_SELECTOR, "#compass, #calendar, #award, #landscape")) >= 4)
    expected_attr = "award"
    third_image = driver.find_element(By.ID, "award")
    actual_attr = third_image.get_attribute("alt")
    assert actual_attr == expected_attr, f"Expected: '{expected_attr}', Actual: '{actual_attr}'"


