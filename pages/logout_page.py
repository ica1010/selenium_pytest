# pages/logout_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class LogoutPage(BasePage):
    def click_mon_compte(self):
        self.click_element(By.XPATH, "//a[contains(@class, 'sub-toggle')]//span[text()='MonCompte']")

    def click_logout(self):
        self.click_element(By.XPATH, "//a[@href='/users/logout.php']")

    
