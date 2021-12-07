from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
from pages.HomePage import HomePage
from pages.SignUpPage import SignUpPage
from utils.locators import *
from utils import users
import time


class LoginPage(BasePage):
    def __init__(self,driver):
        self.locator = LoginPageLocators    #All Locators defined within LoginPageLocators class can now be accessed using self.locator

        super(LoginPage, self).__init__(driver)  # Python2 version

     
    def set_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def set_password(self, password):
       self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_btn(self):
        self.find_element(*self.locator.LOGIN_BUTTON).click()

    def click_signup_btn(self):
        self.find_element(*self.locator.SIGNUP).click()
        return SignUpPage(self.driver)

    def click_need_help(self):
        self.find_element(*self.locator.FORGOT_PASSWORD).click()
        time.sleep(1)
        result = self.find_element(*self.locator.RESET_PANEL).is_displayed() #Validating if reset_panel opens up when user clicks on need help?
        return result

    def check_remember_me(self):
        element = self.find_element(*self.locator.REMEMBER_ME)
        self.driver.execute_script("arguments[0].click();",element) #ClickInterceptedException received when clicking on RememberMe, hence used execute_Script
        result = self.find_element(*self.locator.REMEMBER_ME).is_selected() #Validating if rememberme checkbox is checked when clicked
        return result
    
    def check_login_with_organisation(self):
        self.find_element(*self.locator.ORGANISATION_LOGIN).click()


    def login(self, user):
        user = users.get_user(user)
        self.set_email(user["email"])
        self.set_password(user["password"])
        self.click_login_btn()
        time.sleep(2) # Sleep for 2 seconds, Tried all explicit wait types, but it didn't work in this case, hence using sleep explicitly.

    def login_with_valid_user(self, user):
        self.login(user)
        self.wait_for_element(*HomePageLocators.HOMENAV)
        return HomePage(self.driver)


    def login_with_invalid_user(self, user):
        self.login(user)
        print("Error Message:", self.find_element(*self.locator.ERROR_MESSAGE).text)
        return self.driver.find_element(*self.locator.ERROR_MESSAGE).text
