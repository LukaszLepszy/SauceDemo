from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from page_object_pattern.locators.locators import HomePageLocators


class BasePage(HomePageLocators):
    def __init__(self, driver):
        self.driver = driver

    def wait_until_visibility(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located)

    def wait_until_clicable(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable)

    def wait_until_invisibility(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located)

    def wait_until_presence(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located)

    def find_by_css_selector(self, by_locator):
        return self.driver.find_element_by_css_selector(by_locator)

    def find_by_xpath_selector(self, by_locator):
        return self.driver.find_element_by_xpath_selector(by_locator)

    def find_by_name(self, by_locator):
        return self.driver.find_element(By.NAME, by_locator)

    def get_atribute(self, atribute_name, path):
        element = self.driver.find_element(By.CSS_SELECTOR, path)
        text = element.get_attribute(atribute_name)
        return text