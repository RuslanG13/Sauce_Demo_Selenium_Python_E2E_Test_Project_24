from data import urls
from data import page_elements_data
from data import input_data
from locators.locators_saucedemo import LoginPageLocators as LPL


# tests block
def test_auth_positive(browser, auth_positive):
    """Test Authorization using correct data"""

    assert browser.current_url == urls.INVENTORY_PAGE_ENDPOINT
    assert browser.title == page_elements_data.invertory_page_title


def test_auth_negative(browser):
    """Test Authorization using incorrect data"""
    browser.get(urls.BASE_URL)

    browser.find_element(*LPL.USERNAME_FIELD).send_keys(input_data.username_invalid)
    browser.find_element(*LPL.PASSWORD_FIELD).send_keys(input_data.password_invalid)

    browser.find_element(*LPL.LOGIN_BUTTON).click()

    login_error_elem = browser.find_element(*LPL.ERROR_LOGIN_MESSAGE)
    background_color_of_error_container = (browser.find_element(*LPL.ERROR_MESSAGE_CONTAINER)
                                           .value_of_css_property("background-color"))

    assert browser.current_url == urls.BASE_URL
    assert login_error_elem.text == page_elements_data.login_error_text
    assert background_color_of_error_container == page_elements_data.background_color_error_container
