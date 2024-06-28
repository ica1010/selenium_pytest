# tests/test_login.py
import unittest
import logging
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import os

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
        cls.logger = logging.getLogger(__name__)

        os.environ['WDM_LOCAL'] = '/usr/bin/google-chrome'

        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        cls.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
        cls.logger.info('Initialized WebDriver.')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.logger.info('Closed the browser.')

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.go_to_page()
        self.logger.info('Opened login page.')

        login_page.enter_username("misselapp@gmail.com")
        self.logger.info('Entered username.')

        login_page.enter_password("testK@GO228")
        login_page.click_login()
        self.logger.info('Entered password and logged in.')

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'sub-toggle')]//span[text()='MonCompte']"))
        )
        self.logger.info('Login confirmed.')

if __name__ == "__main__":
    unittest.main()
