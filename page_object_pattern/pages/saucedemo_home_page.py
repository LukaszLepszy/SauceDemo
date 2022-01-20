import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from page_object_pattern.pages.base_page import BasePage


class SauceDemoHomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver) # Konstruktor odwołuje się do klasy nadrzędnej, dodaje ją tutaj i wtedy nie musze
                                            # wpisywac za kazdym razem konstruktora gdy bede chcial wywolac metodę


    def expanding_menu_burger(self):
        burger = self.driver.find_element(By.CSS_SELECTOR, self.burger_locator)
        burger.click()










# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("http://www.google.pl")
# driver.maximize_window()
# driver.close()
# driver.quit()
