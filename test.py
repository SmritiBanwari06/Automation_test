import time
import pytest
from selenium import webdriver
from search_page import SearchPage

BASE_URL = "https://www.flipkart.com"
BASE_PRODUCT = "iphone 15 pro max"


@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def search(browser):
    return SearchPage(browser)


@pytest.mark.usefixtures("browser")
class TestFlipkartSearch:

    def test_search_existing_product(self, search):
        search.browser.get(BASE_URL)
        search.search_product(BASE_PRODUCT)
        search.click_on_phone()
        assert search.get_search_results().is_displayed(), 'No search results found'
        time.sleep(4)

    def test_pincode(self, search):
        search.pincode_availability('560002')
        time.sleep(3)

    def test_add_to_cart(self, search):
        time.sleep(3)
        search.add_to_cart()

