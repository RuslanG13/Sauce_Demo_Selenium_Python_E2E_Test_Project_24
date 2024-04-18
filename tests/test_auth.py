from pages.base_page import BasePage

from locators.login_locators import LoginPageLocators as LPL
from locators.locators_saucedemo import InventoryPageLocators as IPL

from data import urls, page_elements_data, login_credentials


class TestAuth:
    def test_auth_positive(self, driver, auth_positive):
        """Test: authorization using correct data"""

        base_page = BasePage(driver, urls.BASE_URL)
        inventory_page_title = driver.find_element(*IPL.PRODUCTS_TITLE).text

        assert driver.current_url == urls.INVENTORY_PAGE_ENDPOINT, "a user isn't at inventory page"
        assert inventory_page_title == page_elements_data.products_title, "wrong inventory page products title"

    def test_auth_negative(self, driver):
        """Test: authorization using incorrect data"""

        driver.get(urls.BASE_URL)

        driver.find_element(*LPL.USERNAME_FIELD_LOCATOR).send_keys(input_data.username_invalid)
        driver.find_element(*LPL.PASSWORD_FIELD_LOCATOR).send_keys(input_data.password_invalid)

        driver.find_element(*LPL.LOGIN_BUTTON_LOCATOR).click()

        login_error_elem = driver.find_element(*LPL.ERROR_LOGIN_MESSAGE_LOCATOR)
        background_color_of_error_container = (driver.find_element(*LPL.ERROR_MESSAGE_CONTAINER_LOCATOR)
                                               .value_of_css_property("background-color"))

        assert driver.current_url == urls.BASE_URL, "a user isn't at login page"
        assert login_error_elem.text == page_elements_data.login_error_text, "error message is wrong"
        assert background_color_of_error_container == page_elements_data.background_color_error_container, \
            "background color of error container is incorrect"
