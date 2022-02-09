import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

from page_object_pattern.pages.base_page import BasePage


class SauceDemoHomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)


    def expanding_menu_burger(self):
        burger = self.driver.find_element_by_css_selector(self.burger_locator)
        burger.click()
        self.wait_until_visibility(self.menu)

    def clicking_logout_from_menu(self):
        button = self.driver.find_element_by_css_selector(self.button_logout)
        button.click()
        self.wait_until_visibility(self.login_wrapper)











