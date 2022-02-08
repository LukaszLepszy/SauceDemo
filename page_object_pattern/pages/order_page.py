from page_object_pattern.pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_finish_button(self):
        element = self.driver.find_element_by_css_selector(self.button_finish)
        element.click()
        self.wait_until_visibility(self.complete_container)

    def get_name_and_price_produkt(self):
        name = self.driver.find_element_by_css_selector(self.name)
        price = self.driver.find_element_by_css_selector(self.price)
        name = name.text
        price = price.text
        self.click_finish_button()
        return name, price

    def complete_order(self):
        self.click_finish_button()
        self.get_name_and_price_produkt()