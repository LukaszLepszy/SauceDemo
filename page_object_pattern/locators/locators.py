class HomePageLocators:
    # Links
    home_page_link = "https://www.saucedemo.com/v1/inventory.html"

    #Locators
    burger_locator = "div[class='bm-burger-button'] > button"
    login_button_locator = "input[id='login-button']"
    inventory_containter = "div[id='inventory_container']"
    error_notyfication = "h3[data-test='error']"
    error_button = "button[class='error-button']"

    #constants
    input_login_name = "user-name"
    input_password_name = "password"
    logins = [("locked_out_user"), ("problem_user"), ("performance_glitch_user")]