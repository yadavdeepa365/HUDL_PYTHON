from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException

'''
from selenium.webdriver.common.action_chains import ActionChains
'''

# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage(object):
    def __init__(self,driver,base_url='https://www.hudl.com'):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
        self.driver.implicitly_wait(5)

    def find_element(self,*locator):
        return self.driver.find_element(*locator)
    
    def open(self,url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def wait_for_element(self,*locator):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n *ELEMENT NOT FOUND WITHIN GIVEN TIME->"%locator)
            self.driver.quit()
    