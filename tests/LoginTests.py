from selenium import webdriver
from tests.BaseTests import BaseTest
from pages.MainPage import *
from utils.test_cases import test_cases

class LoginTests(BaseTest):

    #USING UNITTEST

    def test_page_load(self):
        print("\n"+str(test_cases(0)))
        page = MainPage(self.driver)
        print(page.check_page_loaded())
        self.assertTrue(page.check_page_loaded())

    def test_sign_in_button(self):
        print("\n" + str(test_cases(1)))
        page = MainPage(self.driver)
        login_page = page.click_sign_in_button()
        self.assertIn("/login", login_page.get_url())

    def test_signin_with_valid_user(self):
        print("\n" + str(test_cases(2)))
        main_page = MainPage(self.driver)
        login_page = main_page.click_sign_in_button()
        home_page = login_page.login_with_valid_user("valid_user")
        self.assertIn("/home", home_page.get_url()) 

    def test_signin_with_invalid_user(self):
        print("\n" + str(test_cases(3)))
        main_page = MainPage(self.driver)
        login_page = main_page.click_sign_in_button()
        result = login_page.login_with_invalid_user("invalid_user")
        self.assertIn("We didn't recognize that email and/or password.", result)

    def test_sign_up_button(self):
        print("\n" + str(test_cases(4)))
        page = MainPage(self.driver)
        login_page = page.click_sign_in_button()
        self.assertIn("/login", login_page.get_url())
        signup_page = login_page.click_signup_btn()
        self.assertIn("register/signup", self.driver.current_url)

    def test_password_reset(self):
        print("\n" + str(test_cases(5)))
        page = MainPage(self.driver)
        login_page = page.click_sign_in_button()
        self.assertIn("/login", login_page.get_url())
        result = login_page.click_need_help()
        self.assertTrue(result)

    def test_remember_me(self):
        print("\n" + str(test_cases(6)))
        page = MainPage(self.driver)
        login_page = page.click_sign_in_button()
        self.assertIn("/login", login_page.get_url())
        result = login_page.check_remember_me()
        self.assertTrue(result)

    def test_organisation_login(self):
        print("\n" + str(test_cases(7)))
        page = MainPage(self.driver)
        login_page = page.click_sign_in_button()
        self.assertIn("/login", login_page.get_url())
        login_page.check_login_with_organisation()
        self.assertIn("/app/auth/login/organization", self.driver.current_url)

