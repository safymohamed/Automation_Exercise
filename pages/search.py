import time
from selenium.webdriver.common.by import By

class search_product:
    URL = 'http://www.automationexercise.com/'
    products = (By.XPATH, '//a[text() = " Products"]')
    search_element = (By.XPATH, '//input[@id="search_product"]')
    icon_element = (By.XPATH, '//i[@class="fa fa-search"]')
    result_element =(By.XPATH, '//div[@class="features_items"]')


    def __init__(self, browser):
        self.browser = browser

    def click_products(self):
        Products= self.browser.find_element(*self.products)
        click= Products.click()

    def search_input(self, phrase):
        input = self.browser.find_element(*self.search_element)
        search= input.send_keys(phrase)

    def search_icon(self):
        icon = self.browser.find_element(*self.icon_element)
        icon_search = icon.click()
        # self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")


    def result_items(self):
        results = self.browser.find_elements(*self.result_element)
        # self.browser.execute_script("arguments[0].scrollIntoView(true);", results);

        self.browser.execute_script("window.scrollTo(0,(document.body.scrollHeight)/2)")
        time.sleep(2)
        items = [item.text for item in results]
        return items










