from pages.login_page import LoginPage
from pages.main_page import MainPage

from locators.login_locators import LoginPageLocators as lpl
from locators.main_locators import MainPageLocators as mpl

from data.page_data.login_data import LoginData
from data.page_data.main_data import MainData

from data.urls import Urls
from data.login_credentials import invalid_login


class TestAuth:
    urls = Urls()

    # main_url = urls.MAIN_PAGE_URL

    def test_auth_positive(self, driver):
        """Test: authorization using correct data"""

        login_page = LoginPage(driver, self.urls.BASE_URL)
        login_page.open_page()
        login_page.login()

        main_page = MainPage(driver, self.urls.MAIN_PAGE_URL)
        main_page_title_text = main_page.get_element_text(mpl.PRODUCTS_TITLE)

        assert main_page.get_url_text() == self.urls.MAIN_PAGE_URL, "The main page is not open. User is not logged in"
        assert main_page_title_text == MainData.products_title, "Wrong main page products title"

    def test_auth_negative(self, driver):
        """Test: authorization using incorrect data"""

        driver.get(self.urls.BASE_URL)

        driver.find_element(*lpl.USERNAME_FIELD_LOCATOR).send_keys(invalid_login["username_invalid"])
        driver.find_element(*lpl.PASSWORD_FIELD_LOCATOR).send_keys(invalid_login["username_invalid"])

        driver.find_element(*lpl.LOGIN_BUTTON_LOCATOR).click()

        login_error_elem = driver.find_element(*lpl.ERROR_LOGIN_MESSAGE_LOCATOR)
        background_color_of_error_container = (driver.find_element(*lpl.ERROR_MESSAGE_CONTAINER_LOCATOR)
                                               .value_of_css_property("background-color"))

        assert driver.current_url == self.urls.BASE_URL, "a user isn't at login page"
        assert login_error_elem.text == LoginData.login_error_text, "error message is wrong"
        assert background_color_of_error_container == LoginData.background_color_error_container, \
            "background color of error container is incorrect"
