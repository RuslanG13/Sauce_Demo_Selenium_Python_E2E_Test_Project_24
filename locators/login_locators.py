class LoginPageLocators:
    USERNAME_FIELD_LOCATOR = ("xpath", "//input[@id='user-name']")
    PASSWORD_FIELD_LOCATOR = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON_LOCATOR = ("xpath", "//input[@data-test='login-button']")
    ERROR_MESSAGE_CONTAINER_LOCATOR = ("xpath", "//div[contains(@class, 'error-message-container')]")
    ERROR_LOGIN_MESSAGE_LOCATOR = ("xpath", "//h3[@data-test='error']")
    LOGIN_LOGO_LOCATOR = ("xpath", "//div[@class='login_logo']")
