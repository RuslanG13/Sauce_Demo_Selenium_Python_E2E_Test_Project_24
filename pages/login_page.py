from pages.base_page import BasePage

from locators.login_locators import LoginPageLocators


class LoginPage(BasePage):
    login_page_locators = LoginPageLocators()

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def login(self, username, password):
        self.element_is_visible(self.login_page_locators.USERNAME_FIELD_LOCATOR).send_keys(username)
        self.element_is_visible(self.login_page_locators.PASSWORD_FIELD_LOCATOR).send_keys(password)
        self.element_is_clickable(self.login_page_locators.LOGIN_BUTTON_LOCATOR).click()

    @property
    def error_login_msg(self):
        return self.element_is_visible(self.login_page_locators.ERROR_LOGIN_MESSAGE_LOCATOR)

    @property
    def error_msg_container_background_color(self):
        return self.get_ccs_property(self.login_page_locators.ERROR_MESSAGE_CONTAINER_LOCATOR,
                                     "background-color")
