class LoginPageLocators:
    USERNAME_FIELD = ("xpath", "//input[@id='user-name']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")

    LOGIN_BUTTON = ("xpath", "//input[@data-test='login-button']")

    ERROR_MESSAGE_CONTAINER = ("xpath", "//div[contains(@class, 'error-message-container')]")
    ERROR_LOGIN_MESSAGE = ("xpath", "//h3[@data-test='error']")
