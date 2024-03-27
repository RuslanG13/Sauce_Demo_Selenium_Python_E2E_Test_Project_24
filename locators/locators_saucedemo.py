class SauceDemoLocators:
    # login page
    USERNAME_FIELD = ("xpath", "//input[@id='user-name']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")

    LOGIN_BUTTON = ("xpath", "//input[@data-test='login-button']")