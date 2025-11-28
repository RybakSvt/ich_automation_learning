from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")


    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self


    def enter_username(self, username):
        username_field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD))
        username_field.clear()
        username_field.send_keys(username)
        return self


    def enter_password(self, password):
        password_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(password)
        return self


    def click_login(self):
        login_btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_btn.click()
        return self


    def login_as_standard_user(self):
        self.open()
        self.enter_username("standard_user")
        self.enter_password("secret_sauce")
        self.click_login()
        return self