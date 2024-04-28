import pytest

from locators.locators_saucedemo import AboutSauceLabPageLocators as ASLoginPage

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage

from data.page_data.base_data import BaseData


class TestBurgerMenu:
    def test_log_out(self, driver, auth_positive):
        """Test: log out from the product"""

        driver.find_element(*MainPage.BURGER_MENU_BUTTON).click()
        driver.find_element(*MainPage.LOGOUT_SIDEBAR_LINK).click()

        login_button = driver.find_element(*LoginPage.LOGIN_BUTTON_LOCATOR)

        assert login_button, "The user is not on the login page"

    def test_about_button(self, driver, auth_positive):
        """Test: the functionality of the “About” button in the burger menu"""

        driver.find_element(*MainPage.BURGER_MENU_BUTTON).click()
        driver.find_element(*MainPage.ABOUT_SIDEBAR_LINK).click()

        saucelabs_logo = driver.find_element(*ASLoginPage.SAUCELABS_LOGO)
        alt_text_logo = saucelabs_logo.get_attribute("alt")

        assert saucelabs_logo, "The Sauce Labs logo is not shown"
        assert alt_text_logo == BaseData.sauce_labs_logo_alt_text, \
            f"The {alt_text_logo} is not equal to the {BaseData.sauce_labs_logo_alt_text}"

    @pytest.mark.xfail
    def test_reset_app_state_button(self, driver, auth_positive, add_item_to_cart_through_catalog,
                                    check_exist_item_in_cart):
        """Test: the functionality of the “Reset App State” button in the burger menu"""

        driver.find_element(*CartPage.BURGER_MENU_BUTTON).click()
        driver.find_element(*CartPage.RESET_APP_STATE_LINK).click()

        amount_items_in_cart_after_reset = len(driver.find_elements(*CartPage.CART_ITEM))

        assert amount_items_in_cart_after_reset == 0, "The cart is not empty"
