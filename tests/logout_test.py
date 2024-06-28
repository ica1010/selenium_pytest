# tests/test_logout.py
import unittest
import logging
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
import os

class TestLogout(unittest.TestCase):
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

        # Perform login before running the logout test
        cls.driver.get("https://pay.kagoservices.com/")
        login_page = LoginPage(cls.driver)
        login_page.enter_username("misselapp@gmail.com")
        login_page.enter_password("testK@GO228")
        login_page.click_login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.logger.info('Closed the browser.')

    def test_logout(self):
        logout_page = LogoutPage(self.driver)

        logout_page.click_mon_compte()
        self.logger.info('Clicked on MonCompte.')

        logout_page.click_logout()
        self.logger.info('Clicked on logout.')

        WebDriverWait(self.driver, 10).until(
            EC.url_matches("https://pay.kagoservices.com/")
        )
        self.logger.info('Logout confirmed.')

if __name__ == "__main__":
    unittest.main()
