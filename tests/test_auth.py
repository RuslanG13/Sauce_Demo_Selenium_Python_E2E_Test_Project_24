from pages.base_page import BasePage

from locators.login_locators import LoginPageLocators as lpl
from locators.main_locators import MainPageLocators as mpl
from data.page_data.login_data import LoginData
from data.page_data.main_data import MainData

from data import urls
from data.login_credentials import invalid_login


class TestAuth:
    def test_auth_positive(self, driver, auth_positive):
        """Test: authorization using correct data"""

        # base_page = BasePage(driver, urls.BASE_URL)
        inventory_page_title = driver.find_element(*mpl.PRODUCTS_TITLE).text

        assert driver.current_url == urls.MAIN_PAGE_URL, "a user isn't at inventory page"
        assert inventory_page_title == MainData.products_title, "wrong inventory page products title"

    def test_auth_negative(self, driver):
        """Test: authorization using incorrect data"""

        driver.get(urls.BASE_URL)

        driver.find_element(*lpl.USERNAME_FIELD_LOCATOR).send_keys(invalid_login["username_invalid"])
        driver.find_element(*lpl.PASSWORD_FIELD_LOCATOR).send_keys(invalid_login["username_invalid"])

        driver.find_element(*lpl.LOGIN_BUTTON_LOCATOR).click()

        login_error_elem = driver.find_element(*lpl.ERROR_LOGIN_MESSAGE_LOCATOR)
        background_color_of_error_container = (driver.find_element(*lpl.ERROR_MESSAGE_CONTAINER_LOCATOR)
                                               .value_of_css_property("background-color"))

        assert driver.current_url == urls.BASE_URL, "a user isn't at login page"
        assert login_error_elem.text == LoginData.login_error_text, "error message is wrong"
        assert background_color_of_error_container == LoginData.background_color_error_container, \
            "background color of error container is incorrect"
