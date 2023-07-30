import time
from pages.Home import Home_page
from pages.review import review_product
from pages.Home import Home_page

def test_review_product(browser):
    review_object = review_product(browser)
    load_object= Home_page(browser)


    name = "safy"
    email= "safymohamed87@gmail.com"
    add = "Great product"

    load_object.load()
    review_object.choose_product()
    review_object.view_product()
    review_object.review()
    review_object.review_name(name)
    review_object.review_email(email)
    review_object.add_review(add)
    review_object.submit()
    time.sleep(3)

