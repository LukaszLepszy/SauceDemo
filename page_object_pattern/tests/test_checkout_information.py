import time

from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import pytest

from page_object_pattern.locators.locators import HomePageLocators
from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.pages.checkout_page import CheckoutPage
from page_object_pattern.pages.products_page import ProductsPage
from page_object_pattern.pages.saucedemo_home_page import SauceDemoHomePage
from page_object_pattern.pages.shop_page import ShopPage

@pytest.mark.usefixtures("setup")
class TestCheckoutInformation:

    def test_notyfication_first_name(self):
        checkout = CheckoutPage(self.driver)
        checkout.go_to_checkout_page()
        checkout.click_continue_button()
        notyfication = self.driver.find_element_by_css_selector(HomePageLocators.error_notyfication_checkout)
        assert notyfication.text == "Error: First Name is required"

    def test_notyfication_last_name(self):
        checkout = CheckoutPage(self.driver)
        checkout.go_to_checkout_page()
        checkout.send_value_to_first_name()
        checkout.click_continue_button()
        notyfication = self.driver.find_element_by_css_selector(HomePageLocators.error_notyfication_checkout)
        assert notyfication.text == "Error: Last Name is required"

    def test_notyfication_zip_code(self):
        checkout = CheckoutPage(self.driver)
        checkout.go_to_checkout_page()
        checkout.send_value_to_first_name()
        checkout.send_value_to_last_name()
        checkout.click_continue_button()
        notyfication = self.driver.find_element_by_css_selector(HomePageLocators.error_notyfication_checkout)
        assert notyfication.text == "Error: Postal Code is required"

    def test_fill_all_informations(self):
        checkout = CheckoutPage(self.driver)
        checkout.go_to_checkout_page()
        checkout.send_all_inputs_and_continue()
        get_url = self.driver.current_url
        assert get_url == "https://www.ssaucedemo.com/v1/checkout-step-two.html"

