import pytest
import allure

from locators.login_locators import LoginPageLocators as lpl
from locators.main_locators import MainPageLocators as mpl

from data.page_data.login_data import LoginData
from data.page_data.main_data import MainData

from data.urls import Urls


@allure.feature("Authorization")
class TestAuth:
    urls = Urls()

    @allure.title("TC_01_01 - Verify authorization using correct data")
    def test_auth_positive(self, driver, login_page, main_page):
        """Verify that a user successfully logged in with valid data"""
        login_page.login(username=LoginData.valid_login_data[0], password=LoginData.valid_login_data[1])

        main_page_title_text = main_page.get_element_text(main_page.products_title)

        assert main_page.get_url_text() == self.urls.MAIN_PAGE_URL and \
               main_page_title_text == MainData.products_title, "The main page is not open. User is not logged in"

    @allure.title("TC_01_02, TC_01_03, TC_01_04 - Verify authorization using incorrect data")
    @pytest.mark.parametrize("username, password", LoginData.invalid_login_data)
    def test_auth_negative(self, driver, login_page, username, password):
        """Verify that a user will not be able to log in with invalid data"""
        login_page.login(username=username, password=password)

        login_error_text = login_page.get_element_text(login_page.error_login_msg)
        background_color_error_container = login_page.error_msg_container_background_color

        assert login_error_text == LoginData.login_error_text, \
            f"The {login_error_text} is not equal {LoginData.login_error_text}"
        assert background_color_error_container == LoginData.background_color_error_container, \
            f"The {background_color_error_container} is not equal {LoginData.background_color_error_container}"
