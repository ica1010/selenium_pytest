# pages/login_page.py
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def go_to_page(self):
        self.driver.get("https://pay.kagoservices.com/")

    def enter_username(self, username):
        self.send_keys_to_element(By.ID, "username", username)

    def enter_password(self, password):
        self.send_keys_to_element(By.ID, "password", password)

    def click_login(self):
        self.send_keys_to_element(By.ID, "password", Keys.ENTER)
