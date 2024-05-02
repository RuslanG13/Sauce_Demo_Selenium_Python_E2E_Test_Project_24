import pytest
import allure

from data.page_data.login_data import LoginData
from data.page_data.main_data import MainData

from data.urls import Urls


@allure.feature("Authorization")
class TestAuth:

    @allure.title("TC_01_01 | Verify authorization using correct data")
    def test_auth_positive(self, login_page, main_page):
        """Verify that a user successfully log in with valid data"""
        login_page.login(username=LoginData.valid_username, password=LoginData.valid_password)

        main_page_title_text = main_page.get_products_title_text

        assert main_page.get_url_text() == Urls.MAIN_PAGE_URL and \
               main_page_title_text == MainData.products_title, "The main page is not open. User is not logged in"

    @allure.title("TC_01_02, TC_01_03, TC_01_04 | Verify authorization using incorrect data")
    @pytest.mark.parametrize("username, password", LoginData.invalid_login_data)
    def test_auth_negative(self, login_page, username, password):
        """Verify that a user can not log in with invalid data"""
        login_page.login(username=username, password=password)

        login_error_text = login_page.get_error_login_msg_text
        background_color_error_container = login_page.get_error_msg_container_background_color

        assert login_error_text == LoginData.login_error_text, \
            f"The {login_error_text} is not equal {LoginData.login_error_text}"
        assert background_color_error_container == LoginData.background_color_error_container, \
            f"The {background_color_error_container} is not equal {LoginData.background_color_error_container}"
