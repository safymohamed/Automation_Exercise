from selenium.webdriver.common.by import By

class review_product:

    URL = 'https://www.automationexercise.com/'
    product_element = (By.XPATH, '//img[@src="/get_product_picture/42"]')
    view_product_element = (By.XPATH, '//a[@href="/product_details/42"]')
    review_element = (By.XPATH, '//a[@href="#reviews"]')
    name_element = (By.XPATH,'//input[@id="name"]')
    email_element = (By.ID, "email")
    add_review_element =(By.XPATH, '//textarea[@name="review"]')
    submit_element = (By.ID, 'button-review')


    def __init__(self, browser):
        self.browser = browser

    def choose_product(self):
        choose= self.browser.find_element(*self.product_element)
        choose.location_once_scrolled_into_view

    def view_product(self):
        view = self.browser.find_element(*self.view_product_element)
        view.click()

    def review (self):
       find_review = self.browser.find_element(*self.review_element)
       find_review.location_once_scrolled_into_view

    def review_name(self, name):
        find_name = self.browser.find_element(*self.name_element)
        find_name.send_keys(name)

    def review_email(self, email):
        find_email = self.browser.find_element(*self.email_element)
        find_email.send_keys(email)

    def add_review(self, add):
        find_add_review = self.browser.find_element(*self.add_review_element)
        find_add_review.send_keys(add)

    def submit(self):
        find_submit = self.browser.find_element(*self.submit_element)
        find_submit.click()




















