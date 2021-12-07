import unittest
from unittest import suite
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.test_cases import test_cases
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# I am using python unittest for asserting cases.

class BaseTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        # options.add_argument("--headless") # Runs Chrome in headless mode
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        s=Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s,options=options)
        self.driver.get("https://www.hudl.com")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(test_cases)
    unittest.TextTestRunner(verbosity=1).run(suite)