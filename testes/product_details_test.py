import time
from pages.product_details import product_details_page
from pages.Home import Home_page

def test_product_page(browser):
     product_page = product_details_page(browser)
     load_object = Home_page(browser)

     load_object.load()
     product_page.choose_product()
     product_page.view_product()
     time.sleep(3)
     product_page.add_to_cart()
     product_page.continue_shopping()

