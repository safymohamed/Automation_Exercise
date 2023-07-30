import time
from pages.search import search_product
from pages.Home import Home_page

def test_basic_search(browser):
    search_object= search_product(browser)
    load_object= Home_page(browser)
    phrase = "tops"

    load_object.load()
    search_object.click_products()
    time.sleep(3)
    search_object.search_input(phrase)
    search_object.search_icon()
    time.sleep(5)


    titles = search_object.result_items()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0





