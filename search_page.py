import time
from xpath_locator import *


class SearchPage:
    def __init__(self, browser):
        self.browser = browser

    def search_product(self, product_name):
        search_bar = self.browser.find_element(By.XPATH, SEARCH_BAR_XPATH)
        search_bar.send_keys(product_name)
        search_bar.submit()

    def click_on_phone(self):
        phone = self.browser.find_element(By.XPATH, PHONE_XPATH)
        phone.click()
        time.sleep(4)

    def get_search_results(self):
        return self.browser.find_element(By.XPATH, SEARCH_RESULTS_XPATH)

    def pincode_availability(self, pincode):
        self.browser.switch_to.window(self.browser.window_handles[-1])
        pincode_field = self.browser.find_element(By.XPATH, PIN_CODE_XPATH)
        pincode_field.send_keys(pincode)

        check_button = self.browser.find_element(By.XPATH, CHECK_XPATH)
        check_button.click()

    def add_to_cart(self):
        self.browser.switch_to.window(self.browser.window_handles[-1])
        cart_button = self.browser.find_element(By.XPATH, CART_XPATH)
        cart_button.click()
        time.sleep(2)

