import time
from pages.add_remove import products_page
from pages.Home import Home_page

def test_add_to_cart(browser):
    load_object= Home_page(browser)
    add_object= products_page(browser)

    load_object.load()
    add_object.first_product()
    time.sleep(3)
    add_object.View_cart()
    add_object.cart_page()
    add_object.remove_from_cart()
    time.sleep(5)



