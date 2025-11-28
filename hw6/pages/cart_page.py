from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def proceed_to_checkout(self):
        checkout_btn = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        checkout_btn.click()
        return self