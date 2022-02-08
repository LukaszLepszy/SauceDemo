import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from page_object_pattern.locators.locators import HomePageLocators
from page_object_pattern.pages.products_page import ProductsPage
from page_object_pattern.pages.saucedemo_home_page import SauceDemoHomePage
from page_object_pattern.pages.shop_page import ShopPage


@pytest.mark.usefixtures("setup")
class TestSouceDemo:


    def test_adding_button(self):
        products = ProductsPage(self.driver)
        products.choose_type_sorting("az")
        assert products.add_product_to_shop(HomePageLocators.backpack_produkt) == "REMOVE"
    #
    def test_product_in_basket(self):
        products = ProductsPage(self.driver)
        products.choose_type_sorting("az")
        products.add_product_to_shop(HomePageLocators.backpack_produkt)
        product_in_shop = ShopPage(self.driver)
        product_in_shop.go_to_basket()
        assert product_in_shop.get_info_from_basket() == ('Sauce Labs Backpack', '29.99')

    def test_remove_product_from_basket(self):
        products = ProductsPage(self.driver)
        products.choose_type_sorting("az")
        products.add_product_to_shop(HomePageLocators.backpack_produkt)
        product_in_shop = ShopPage(self.driver)
        product_in_shop.go_to_basket()
        product_in_shop.get_info_from_basket()
        assert product_in_shop.remove_product_from_basket().is_displayed

    def test_remove_product_from_shop(self):
        products = ProductsPage(self.driver)
        products.choose_type_sorting("az")
        products.add_product_to_shop(HomePageLocators.backpack_produkt)
        assert products.clicking_in_remove_button() == "ADD TO CART"

    def test_continue_shopping_button(self):
        products = ProductsPage(self.driver)
        products.choose_type_sorting("az")
        products.add_product_to_shop(HomePageLocators.backpack_produkt)
        basket = ShopPage(self.driver)
        basket.go_to_basket()
        assert basket.click_continue_shopping_button() == "https://www.saucedemo.com/v1/inventory.html"

    def test_checkout_button(self):
        products = ProductsPage(self.driver)
        products.choose_type_sorting("az")
        products.add_product_to_shop(HomePageLocators.backpack_produkt)
        basket = ShopPage(self.driver)
        basket.go_to_basket()
        assert basket.click_checkout_button() == "https://www.saucedemo.com/v1/checkout-step-one.html"
