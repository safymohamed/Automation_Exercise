import time
from pages.Home import Home_page
from pages.contact import contact_us_form

def test_contact_form(browser):
    load_object = Home_page(browser)
    contact_object = contact_us_form(browser)
    name = "safy"
    email = "safymohamed87@gmail.com"
    subject = "testing"
    message = "Hi its my first project"
    success = "Success! Your details have been submitted successfully."



    load_object.load()
    contact_object.click_contact()
    contact_object.name_text(name)
    contact_object.email_text(email)
    contact_object.subject_text(subject)
    contact_object.message_text(message)
    contact_object.choose_file()
    contact_object.click_submit()
    time.sleep(3)
    contact_object.message()





