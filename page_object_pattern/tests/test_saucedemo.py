import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from page_object_pattern.pages.saucedemo_home_page import SauceDemoHomePage

@pytest.mark.usefixtures("setup")
class TestSouceDemo:

    def test_burger(self):
        page = SauceDemoHomePage(self.driver)
        page.expanding_menu_burger()
        time.sleep(2)




