from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
import pytest

from page_object_pattern.Utils.driver_factory import DriverFactory


@pytest.fixture()
def setup(request):
    driver = DriverFactory.get_driver("chrome")
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    # c.add_argument("--incognito")
    # c.add_argument('ignore-certificate-errors')
    # driver = webdriver.Chrome(options=c)
    driver.implicitly_wait(1)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    request.cls.driver = driver
    yield
    driver.stop_client()
    driver.close()
    driver.quit()

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.saucedemo.com/v1/inventory.html")
# driver.maximize_window()
# yield
# driver.quit()