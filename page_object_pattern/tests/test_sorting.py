import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from page_object_pattern.locators.locators import HomePageLocators
from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.pages.loggining_page import LogginingPage
from page_object_pattern.pages.products_page import ProductsPage
from page_object_pattern.pages.saucedemo_home_page import SauceDemoHomePage


@pytest.mark.usefixtures("setup")
class TestLoggining:

    def test_sorting_A_to_Z(self):
        products = ProductsPage(self.driver)
        products.choose_type_sorting("az")
        assert products.get_names_products_list() == HomePageLocators.products_list_A_to_Z

    def test_sorting_Z_to_A(self):
        products = ProductsPage(self.driver)
        products.choose_type_sorting("za")
        assert products.get_names_products_list() == HomePageLocators.products_list_Z_to_A

    def test_sorting_price_low_to_high(self):
        products = ProductsPage(self.driver)
        products.choose_type_sorting("lohi")
        assert products.get_prices_products_list() == HomePageLocators.products_price_list_low_to_hight

    def test_sorting_price_hight_to_low(self):
        products = ProductsPage(self.driver)
        products.choose_type_sorting("hilo")
        assert products.get_prices_products_list() == HomePageLocators.products_price_list_hight_to_low
