import time
from selenium.webdriver.common.by import By

class product_details_page:
    URL = 'https://www.automationexercise.com/'
    product_element = (By.XPATH, '//img[@src="/get_product_picture/13"]')
    view_product_element = (By.XPATH, '//a[@href="/product_details/13"]')
    add_element = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button')
    shopping_element = (By.XPATH, '//button[text() = "Continue Shopping"]')

    def __init__(self, browser):
        self.browser = browser

    def choose_product(self):
        choose = self.browser.find_element(*self.product_element)
        choose.location_once_scrolled_into_view
        time.sleep(5)


    def view_product(self):
        view = self.browser.find_element(*self.view_product_element)
        view.click()

    def add_to_cart(self):
        add = self.browser.find_element(*self.add_element)
        add.click()

    def continue_shopping(self):
        shopping = self.browser.find_element(*self.shopping_element)
        time.sleep(5)
        shopping.click()









