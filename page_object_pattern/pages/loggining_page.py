import time

from selenium.webdriver.common.by import By

from page_object_pattern.locators.locators import HomePageLocators
from page_object_pattern.pages.base_page import BasePage


class LogginingPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def move_to_login_page(self):
        self.driver.get("https://www.saucedemo.com/v1/index.html")
        self.wait_until_clicable(self.input_login_name)

    def send_login(self, login):
        self.wait_until_clicable(self.input_login_name)
        input_login = self.driver.find_element_by_name(self.input_login_name)
        input_login.send_keys(login)

    def send_password(self):
        self.wait_until_clicable(self.input_password_name)
        input_password = self.driver.find_element_by_name(self.input_password_name)
        input_password.send_keys("secret_sauce")

    def submit(self):
        login = self.driver.find_element_by_css_selector(self.login_button_locator)
        login.click()
        self.wait_until_visibility(self.inventory_containter)

    def get_error_message(self):
        error_notyfication = self.driver.find_element_by_css_selector(self.error_notyfication)
        error_text = error_notyfication.text
        return error_text

    def loggining_to_account(self):
        self.send_login("standard_user")
        self.send_password()
        self.submit()