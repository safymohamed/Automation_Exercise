from selenium.webdriver.common.by import By

class products_page:
    URL = 'http://www.automationexercise.com/'
    add_item = (By.CSS_SELECTOR, 'a[data-product-id="1"]')
    view = (By.XPATH, '//u[text() ="View Cart"]')
    first = (By.ID, 'product-1')
    remove = (By.XPATH, '//i[@class="fa fa-times"]')
    #remove_text = (By.XPATH, '//p/b')

    def __init__(self, browser):
        self.browser = browser


    def first_product(self):
        product = self.browser.find_element(*self.add_item)
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        click= product.click()

    def View_cart(self):
        view_cart = self.browser.find_element(*self.view)
        click= view_cart.click()

    def cart_page(self):
        top = self.browser.find_element(*self.first)
        Blue_top = top.text
        return Blue_top

    def remove_from_cart(self):
        remove_element = self.browser.find_element(*self.remove)
        click= remove_element.click()












