import time
from selenium.webdriver.common.by import By

class contact_us_form:
    name_element= (By.XPATH, '//input[@name="name"]')
    email_element = (By.XPATH, '//input[@name="email"]')
    subject_element = (By.XPATH, '//input[@name="subject"]')
    message_element = (By.XPATH, '//textarea[@name="message"]')
    file_element = (By.XPATH, '//input[@name="upload_file"]')
    contact_element = (By.XPATH, '//a[@href="/contact_us"]')
    submit_element = (By.XPATH, '//input[@name="submit"]')
    success_element = (By.XPATH, ' //div[@class="status alert alert-success"]')

    def __init__(self, browser):
        self.browser = browser

    def click_contact(self):
        contact = self.browser.find_element(*self.contact_element)
        contact.click()

    def name_text(self, name):
        select_name = self.browser.find_element(*self.name_element)
        select_name.send_keys(name)

    def email_text(self, email):
        select_email = self.browser.find_element(*self.email_element)
        select_email.send_keys(email)

    def subject_text(self, subject):
        select_subject = self.browser.find_element(*self.subject_element)
        select_subject.send_keys(subject)

    def message_text(self, message):
        select_message = self.browser.find_element(*self.message_element)
        select_message.send_keys(message)


    def choose_file(self):
        file = self.browser.find_element(*self.file_element)
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        file.send_keys("C:/Users/scs/Pictures/Screenshots/flower.png")
        time.sleep(3)

    def click_submit(self):
        submit = self.browser.find_element(*self.submit_element)
        submit.click()

    def message(self):
        success = self.browser.find_element(*self.success_element)
        message = success.text
        return message










