from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD_LOCATOR = ("xpath", "//input[@id='user-name']")
    PASSWORD_FIELD_LOCATOR = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON_LOCATOR = ("xpath", "//input[@data-test='login-button']")
    ERROR_MESSAGE_CONTAINER_LOCATOR = ("xpath", "//div[contains(@class, 'error-message-container')]")
    ERROR_LOGIN_MESSAGE_LOCATOR = ("xpath", "//h3[@data-test='error']")
    LOGIN_LOGO_LOCATOR = ("xpath", "//div[@class='login_logo']")

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def login(self, username, password):
        self.element_is_visible(self.USERNAME_FIELD_LOCATOR).send_keys(username)
        self.element_is_visible(self.PASSWORD_FIELD_LOCATOR).send_keys(password)
        self.element_is_clickable(self.LOGIN_BUTTON_LOCATOR).click()

    @property
    def error_login_msg(self):
        return self.element_is_visible(self.ERROR_LOGIN_MESSAGE_LOCATOR)

    @property
    def error_msg_container_background_color(self):
        return self.get_ccs_property(self.ERROR_MESSAGE_CONTAINER_LOCATOR, "background-color")
