import pytest

from locators.locators_saucedemo import LoginPageLocators as LPL
from locators.locators_saucedemo import InventoryPageLocators as IPL
from locators.locators_saucedemo import AboutSauceLabPageLocators as ASLPL
from locators.locators_saucedemo import CartPageLocators as CPL

from data import page_elements_data


class TestBurgerMenu:
    def test_log_out(self, browser, auth_positive):
        """Test: log out from the product"""

        browser.find_element(*IPL.BURGER_MENU_BUTTON).click()
        browser.find_element(*IPL.LOGOUT_SIDEBAR_LINK).click()

        login_button = browser.find_element(*LPL.LOGIN_BUTTON)

        assert login_button, "The user is not on the login page"

    def test_about_button(self, browser, auth_positive):
        """Test: the functionality of the “About” button in the burger menu"""

        browser.find_element(*IPL.BURGER_MENU_BUTTON).click()
        browser.find_element(*IPL.ABOUT_SIDEBAR_LINK).click()

        saucelabs_logo = browser.find_element(*ASLPL.SAUCELABS_LOGO)
        alt_text_logo = saucelabs_logo.get_attribute("alt")

        assert saucelabs_logo, "The Sauce Labs logo is not shown"
        assert alt_text_logo == page_elements_data.sauce_labs_logo_alt_text, \
            f"The {alt_text_logo} is not equal to the {page_elements_data.sauce_labs_logo_alt_text}"

    @pytest.mark.xfail
    def test_reset_app_state_button(self, browser, auth_positive, add_item_to_cart_through_catalog,
                                    check_exist_item_in_cart):
        """Test: the functionality of the “Reset App State” button in the burger menu"""

        browser.find_element(*CPL.BURGER_MENU_BUTTON).click()
        browser.find_element(*CPL.RESET_APP_STATE_LINK).click()

        amount_items_in_cart_after_reset = len(browser.find_elements(*CPL.CART_ITEMS))

        assert amount_items_in_cart_after_reset == 0, "The cart is not empty"
