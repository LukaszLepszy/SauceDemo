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
    sorting_dropdown = "div[class='product_label']"
    products_list = "div[class='inventory_list']"

    #constants
        #Login Page
    input_login_selecotor = "input[id='user-name']"
    input_password_selector = "input[id='password']"
    input_login_name = "user-name"
    input_password_name = "password"
    logins = [("locked_out_user"), ("problem_user"), ("performance_glitch_user")]
        #Products Page
