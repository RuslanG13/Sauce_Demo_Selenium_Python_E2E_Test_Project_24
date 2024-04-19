import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage

from locators.login_locators import LoginPageLocators as lpl
from locators.main_locators import MainPageLocators as mpl

from data.page_data.login_data import LoginData
from data.page_data.main_data import MainData

from data.urls import Urls


class TestAuth:
    urls = Urls()

    @pytest.fixture()
    def login_page(self, driver):
        login_page = LoginPage(driver, self.urls.BASE_URL)
        login_page.open_page()
        return login_page

    @pytest.fixture()
    def main_page(self, driver):
        main_page = MainPage(driver, self.urls.MAIN_PAGE_URL)
        return main_page

    def test_auth_positive(self, driver, login_page, main_page):
        """Verify that a user successfully logged in with valid data"""
        login_page.login(username=LoginData.valid_login_data[0], password=LoginData.valid_login_data[1])

        main_page_title_text = main_page.get_element_text(mpl.PRODUCTS_TITLE)

        assert (main_page.get_url_text() == self.urls.MAIN_PAGE_URL and \
                main_page_title_text == MainData.products_title), "The main page is not open. User is not logged in"


    @pytest.mark.parametrize("username, password", LoginData.invalid_login_data)
    def test_auth_negative(self, driver, login_page, username, password):
        """Verify that a user will not be able to log in with invalid data"""
        login_page.login(username=username, password=password)
        login_error_text = login_page.get_element_text(lpl.ERROR_LOGIN_MESSAGE_LOCATOR)
        background_color_error_container = login_page.get_ccs_property(lpl.ERROR_MESSAGE_CONTAINER_LOCATOR,
                                                                       "background-color")

        assert login_error_text == LoginData.login_error_text, \
            f"The {login_error_text} is not equal {LoginData.login_error_text}"
        assert background_color_error_container == LoginData.background_color_error_container, \
            f"The {background_color_error_container} is different than {LoginData.background_color_error_container}"
