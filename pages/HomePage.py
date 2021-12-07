from pages.BasePage import BasePage

class HomePage(BasePage):
    
    def is_homepage_opened_after_login(self):
        current_url = self.get_url
        print(current_url.title)
        return self.get_title()
