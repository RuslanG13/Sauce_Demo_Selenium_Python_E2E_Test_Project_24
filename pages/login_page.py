from pages.base_page import BasePage
from locators.login_locators import LoginPageLocators as lpl
from data.login_credentials import valid_login


class LoginPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def login(self):
        self.element_is_visible(lpl.USERNAME_FIELD_LOCATOR).send_keys(valid_login["username_valid"])
        self.element_is_visible(lpl.PASSWORD_FIELD_LOCATOR).send_keys(valid_login["password_valid"])
        self.element_is_clickable(lpl.LOGIN_BUTTON_LOCATOR).click()
