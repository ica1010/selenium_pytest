# pages/base_page.py

from abc import ABC, abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver
    
    def click_element(self, by, value, timeout=20):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))
        element.click()

    def send_keys_to_element(self, by, value, keys, timeout=20):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))
        element.send_keys(keys)
