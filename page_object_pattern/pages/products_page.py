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

    def add_product_to_shop(self, locator):
        self.wait_until_visibility(locator)
        product = self.driver.find_element_by_xpath(locator)
        product.click()
        self.wait_until_visibility(HomePageLocators.icon_shop_with_red_caunter)
        button_remove = self.driver.find_element_by_xpath(locator)
        button_remove = button_remove.text
        return button_remove

    def clicking_in_remove_button(self):
        self.wait_until_visibility(self.remove_button_in_shop)
        element = self.driver.find_element_by_css_selector(self.remove_button_in_shop)
        element.click()
        self.wait_until_invisibility(self.icon_shop_with_red_caunter)
        add_button = self.driver.find_element_by_xpath(self.backpack_produkt)
        add_button = add_button.text
        return add_button






