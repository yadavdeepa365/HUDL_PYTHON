from selenium.webdriver.common.keys import Keys
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
#from pages.MainPage import MainPage
from utils.locators import *


# Page objects are written in this module.
# Depends on this Main page functionality we can have more functions for new classes, Currently I have only included below 2 functions for the test purpose

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.MAINCONTENT) else False

    def click_sign_in_button(self):
        self.find_element(*self.locator.LOGIN_BUTTON).click()
        return LoginPage(self.driver)
