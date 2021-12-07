from selenium.webdriver.common.by import By

# for maintainability  I have created seperate web objects by page name

class LoginPageLocators(object):
    EMAIL = (By.ID,'email')
    PASSWORD = (By.ID,'password')
    LOGIN_BUTTON = (By.ID,'logIn')
    REMEMBER_ME = (By.ID,'remember-me')
    FORGOT_PASSWORD = (By.ID,'forgot-password-link')
    RESET_BUTTON = (By.ID,'resetBtn')
    RESET_PANEL = (By.XPATH,"//*[@class = 'reset-info']")
    ORGANISATION_LOGIN = (By.ID,'logInWithOrganization')
    ERROR_MESSAGE = (By.XPATH,"//div[@class='login-error-container']/p[1]")
    SIGNUP = (By.XPATH,"//a[contains(text(),'Sign up')]")

class MainPageLocators(object):
    MAINCONTENT = (By.ID,'maincontent')
    LOGIN_BUTTON = (By.XPATH,"//*[@data-qa-id = 'login']")

class HomePageLocators(object):
    HOMENAV = (By.XPATH,"//*[@data-qa-id = 'webnav-globalnav-home']")
    EXPLORENAV = (By.XPATH,"//*[@data-qa-id = 'webnav-globalnav-explore']")

