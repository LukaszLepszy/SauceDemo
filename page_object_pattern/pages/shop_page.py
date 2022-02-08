import time

from page_object_pattern.pages.base_page import BasePage


class ShopPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def go_to_basket(self):
        shop_icon = self.driver.find_element_by_css_selector(self.icon_shop)
        shop_icon.click()
        self.wait_until_visibility(self.product_cart)

    def get_info_from_basket(self):
        self.wait_until_visibility(self.product_cart)
        item_name = self.driver.find_element_by_css_selector(self.product_cart_item_name)
        item_name = item_name.text
        price_item = self.driver.find_element_by_css_selector(self.product_cart_item_price)
        price_item = price_item.text
        return item_name, price_item

    def remove_product_from_basket(self):
        button = self.driver.find_element_by_css_selector(self.remove_button_in_basket)
        button.click()
        element = self.driver.find_element_by_css_selector(self.removed_item_cart)
        return element

    def click_continue_shopping_button(self):
        self.wait_until_visibility(self.button_continue_shopping)
        button = self.driver.find_element_by_css_selector(self.button_continue_shopping)
        button.click()
        self.wait_until_visibility(self.inventory_containter)
        shop_url = self.driver.current_url
        return shop_url

    def click_checkout_button(self):
        self.wait_until_visibility(self.button_checkout)
        button = self.driver.find_element_by_css_selector(self.button_checkout)
        button.click()
        self.wait_until_visibility(self.checkout_info)
        checkout_url = self.driver.current_url
        return checkout_url


