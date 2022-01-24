import time

from selenium.webdriver.common.by import By

from page_object_pattern.locators.locators import HomePageLocators
from page_object_pattern.pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class ProductsPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def choose_type_sorting(self, dropdown_value):
        select = Select(self.driver.find_element_by_css_selector(HomePageLocators.sorting_dropdown))
        select.select_by_value(dropdown_value)

    def get_names_products_list(self):
        element = self.driver.find_elements_by_css_selector(HomePageLocators.product_name)
        products_title_list = []
        for x in element:
            products_title_list.append(x.text)
        return products_title_list

    def get_prices_products_list(self):
        element = self.driver.find_elements_by_css_selector(HomePageLocators.product_price)
        products_price_list = []
        for x in element:
            products_price_list.append(x.text)
        return products_price_list




