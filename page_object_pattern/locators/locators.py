class HomePageLocators:
    # Links
    home_page_link = "https://www.saucedemo.com/v1/inventory.html"

    #Locators
        #Login Page
    login_button_locator = "input[id='login-button']"
    login_wrapper = "div[class='login_wrapper-inner]"
    error_notyfication = "h3[data-test='error']"
    error_button = "button[class='error-button']"
        #Products Page
    burger_locator = "div[class='bm-burger-button'] > button"
    inventory_containter = "div[id='inventory_container']"
    menu = "div[class='bm-menu-wrap']"
    button_logout = "a[id='logout_sidebar_link']"
    sorting_dropdown = "select[class='product_sort_container']"
    products_list = "div[class='inventory_list']"
    product_name = "div[class='inventory_item_name']"
    product_price = "div[class='inventory_item_price']"

    #constants
        #Login Page
    input_login_selecotor = "input[id='user-name']"
    input_password_selector = "input[id='password']"
    input_login_name = "user-name"
    input_password_name = "password"
    logins = [("locked_out_user"), ("problem_user"), ("performance_glitch_user")]
        #Products Page
    products_list_A_to_Z = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket",
                "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    products_list_Z_to_A = ["Test.allTheThings() T-Shirt (Red)", "Sauce Labs Onesie", "Sauce Labs Fleece Jacket", "Sauce Labs Bolt T-Shirt",
                            "Sauce Labs Bike Light", "Sauce Labs Backpack"]
    products_price_list_hight_to_low = ["$49.99", "$29.99", "$15.99", "$15.99", "$9.99", "$7.99"]

    products_price_list_low_to_hight = ["$7.99", "$9.99", "$15.99", "$15.99", "$29.99", "$49.99"]