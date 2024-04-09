import time

from locators.locators_saucedemo import LoginPageLocators as LPL
from locators.locators_saucedemo import InventoryPageLocators as IPL

from data import urls
from data import page_elements_data


def test_log_out(browser, auth_positive):
    """Test: log out from the product"""

    browser.find_element(*IPL.BURGER_MENU_BUTTON).click()
    browser.find_element(*IPL.LOGOUT_SIDEBAR_LINK).click()

    login_button = browser.find_element(*LPL.LOGIN_BUTTON)

    assert login_button, "The user is not on the login page"
