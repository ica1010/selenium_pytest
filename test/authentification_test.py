import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
class TestLoginLogout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configure WebDriver with options and specified version
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_driver_version = '114.0.5735.90'  # Replace with your Chrome version
        
        # Initialize WebDriver with the specified version
        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager(version=chrome_driver_version).install()), 
            options=chrome_options
        )

        # Open the login page
        cls.driver.get("https://pay.kagoservices.com/")

    @classmethod
    def tearDownClass(cls):
        # Quit the driver after the test class
        cls.driver.quit()

    def test_login_logout(self):

            # Enter username
            self.wait_and_send_keys((By.ID, "username"), "misselapp@gmail.com")

            # Enter password
            self.wait_and_send_keys((By.ID, "password"), "testK@GO228" + Keys.RETURN)

            # Wait for dropdown element for "MonCompte" to be clickable
            dropdown_element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'sub-toggle')]//span[text()='MonCompte']"))
            )

            # Click on the dropdown element for "MonCompte"
            dropdown_element.click()

            # Pause for observation
            time.sleep(2)

            # Wait for logout element to be clickable
            logout_element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/users/logout.php']"))
            )

            # Click on the logout element
            logout_element.click()

            # Pause for observation
            time.sleep(2)

            # Wait for logout confirmation (you might need to adjust this wait time)
            WebDriverWait(self.driver, 10).until(
                EC.url_matches("https://pay.kagoservices.com/")
            )

    def wait_and_send_keys(self, locator, keys, timeout=20):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.send_keys(keys)

    def wait_and_click(self, locator, timeout=80):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

if __name__ == "__main__":
    unittest.main()
