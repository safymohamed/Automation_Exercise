from selenium.webdriver.common.by import By

class Home_page:
    URL = 'http://www.automationexercise.com/'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)








