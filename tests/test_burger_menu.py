import time

from locators.locators_saucedemo import LoginPageLocators as LPL
from locators.locators_saucedemo import InventoryPageLocators as IPL
from locators.locators_saucedemo import AboutSauceLabPageLocators as ASLPL

from data import urls
from data import page_elements_data


def test_log_out(browser, auth_positive):
    """Test: log out from the product"""

    browser.find_element(*IPL.BURGER_MENU_BUTTON).click()
    browser.find_element(*IPL.LOGOUT_SIDEBAR_LINK).click()

    login_button = browser.find_element(*LPL.LOGIN_BUTTON)

    assert login_button, "The user is not on the login page"


def test_about_button_burger_menu(browser, auth_positive):
    """Test: the functionality of the “About” button in the menu"""

    browser.find_element(*IPL.BURGER_MENU_BUTTON).click()
    browser.find_element(*IPL.ABOUT_SIDEBAR_LINK).click()
    time.sleep(5)
    saucelabs_logo = browser.find_element(*ASLPL.SAUCELABS_LOGO)
    alt_text_logo = saucelabs_logo.get_attribute("alt")

    assert saucelabs_logo, "The Sauce Labs logo is not shown"
    assert alt_text_logo == page_elements_data.sauce_labs_logo_alt_text, \
        f"The {alt_text_logo} is not equal to the {page_elements_data.sauce_labs_logo_alt_text}"
