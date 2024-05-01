class LoginData:
    login_error_text = "Epic sadface: Username and password do not match any user in this service"
    background_color_error_container = "rgba(226, 35, 26, 1)"

    valid_username = "standard_user"
    valid_password = "secret_sauce"
    invalid_login_data = [("user", "secret_sauce"), ("standard_user", "user"), ("user", "user")]
