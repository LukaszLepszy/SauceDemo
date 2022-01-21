class HomePageLocators:
    # Links
    home_page_link = "https://www.saucedemo.com/v1/inventory.html"

    #Locators
    burger_locator = "div[class='bm-burger-button'] > button"
    login_button_locator = "input[id='login-button']"
    login_wrapper = "div[class='login_wrapper-inner]"
    inventory_containter = "div[id='inventory_container']"
    error_notyfication = "h3[data-test='error']"
    error_button = "button[class='error-button']"
    menu = "div[class='bm-menu-wrap']"
    button_logout = "a[id='logout_sidebar_link']"

    #constants
    input_login_name = "user-name"
    input_password_name = "password"
    logins = [("locked_out_user"), ("problem_user"), ("performance_glitch_user")]