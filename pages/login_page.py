from pages.base_page import BasePage
from locators.login_locators import LoginPageLocators as lpl


class LoginPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def login(self, username, password):
        self.element_is_visible(lpl.USERNAME_FIELD_LOCATOR).send_keys(username)
        self.element_is_visible(lpl.PASSWORD_FIELD_LOCATOR).send_keys(password)
        self.element_is_clickable(lpl.LOGIN_BUTTON_LOCATOR).click()
