import time

from page_object_pattern.pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def go_to_checkout_page(self):
        self.driver.get("https://www.saucedemo.com/v1/checkout-step-one.html")
        self.wait_until_visibility(self.input_first_name)

    def click_continue_button(self):
        element = self.driver.find_element_by_css_selector(self.button_continue_checkout)
        element.click()

    def send_value_to_first_name(self):
        element = self.driver.find_element_by_css_selector(self.input_first_name)
        element.send_keys("Tomasz")

    def send_value_to_last_name(self):
        element = self.driver.find_element_by_css_selector(self.input_last_name)
        element.send_keys("Kowalski")

    def send_value_to_zip_code(self):
        element = self.driver.find_element_by_css_selector(self.input_zip_code)
        element.send_keys("1234567")

    def send_all_inputs_and_continue(self):
        first_name = self.driver.find_element_by_css_selector(self.input_first_name)
        first_name.send_keys("Tomasz")
        last_name = self.driver.find_element_by_css_selector(self.input_last_name)
        last_name.send_keys("Kowalski")
        code = self.driver.find_element_by_css_selector(self.input_zip_code)
        code.send_keys("1234567")
        continue_button = self.driver.find_element_by_css_selector(self.button_continue_checkout)
        continue_button.click()
        self.wait_until_visibility(self.button_finish)