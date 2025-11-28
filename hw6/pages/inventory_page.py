from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    ITEM_BUTTONS = {
        "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
        "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
        "Sauce Labs Bike Light": (By.ID, "add-to-cart-sauce-labs-bike-light"),
        "Sauce Labs Fleece Jacket": (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
        "Test.allTheThings() T-Shirt (Red)": (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    }

    def add_item_to_cart(self, item_name):

        if item_name in self.ITEM_BUTTONS:
            add_to_cart_btn = self.wait.until(EC.element_to_be_clickable(self.ITEM_BUTTONS[item_name]))
            add_to_cart_btn.click()
        else:
            raise ValueError(f"Товар '{item_name}' не найден в предопределенных локаторах")
        return self

    def go_to_cart(self):
        cart_btn = self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON))
        cart_btn.click()
        return self