import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from page_object_pattern.locators.locators import HomePageLocators
from page_object_pattern.pages.loggining_page import LogginingPage

@pytest.mark.usefixtures("setup")
class TestLoggining:

    def test_properly_loggining(self):
        login = LogginingPage(self.driver)
        login.move_to_login_page()
        login.loggining_to_account()
        url_page = self.driver.current_url
        assert url_page == 'https://www.saucedemo.com/v1/inventory.html'

    def test_without_password(self):
        login = LogginingPage(self.driver)
        login.move_to_login_page()
        login.send_login("standard_user")
        login.submit()
        assert login.get_error_message() == "Epic sadface: Password is required"

    def test_without_login(self):
        login = LogginingPage(self.driver)
        login.move_to_login_page()
        login.send_password()
        login.submit()
        assert login.get_error_message() == "Epic sadface: Username is required"

    def test_without_login_and_password(self):
        login = LogginingPage(self.driver)
        login.move_to_login_page()
        login.submit()
        assert visibility_of_element_located(login.get_error_message())

    def test_locked_account(self):
        logins = LogginingPage(self.driver)
        logins.move_to_login_page()
        logins.send_login("locked_out_user")
        logins.send_password()
        logins.submit()
        assert logins.get_error_message() == "Epic sadface: Sorry, this user has been locked out."

    # @pytest.mark.parametrize("login", HomePageLocators.logins)
    # def test_with_diffrent_account(self, login):
    #     logins = LogginingPage(self.driver)
    #     logins.move_to_login_page()
    #     logins.send_login(login)
    #     logins.submit()
    #     url_page = self.driver.current_url
    #     assert url_page == 'https://www.saucedemo.com/v1/inventory.html'



