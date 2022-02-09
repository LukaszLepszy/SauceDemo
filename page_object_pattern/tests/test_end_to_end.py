import time

from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import pytest

from page_object_pattern.locators.locators import HomePageLocators
from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.pages.checkout_page import CheckoutPage
from page_object_pattern.pages.loggining_page import LogginingPage
from page_object_pattern.pages.order_page import OrderPage
from page_object_pattern.pages.products_page import ProductsPage
from page_object_pattern.pages.saucedemo_home_page import SauceDemoHomePage
from page_object_pattern.pages.shop_page import ShopPage

@pytest.mark.usefixtures("setup")
class TestEndToEnd:

    def test_login_addproduct_checkout_finish(self):
        loggining = LogginingPage(self.driver)
        loggining.move_to_login_page()
        loggining.loggining_to_account()
        add_product = ProductsPage(self.driver)
        add_product.choose_type_sorting("az")
        add_product.add_product_to_shop(HomePageLocators.backpack_produkt)
        shop = ShopPage(self.driver)
        shop.go_to_basket()
        shop.click_checkout_button()
        checkout = CheckoutPage(self.driver)
        checkout.send_all_inputs_and_continue()
        finish = OrderPage(self.driver)
        assert finish.get_name_and_price_produkt() == ('Sauce Labs Backpack', '$29.99')







