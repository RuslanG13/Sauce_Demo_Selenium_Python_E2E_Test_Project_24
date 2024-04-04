from data import urls
from data import page_elements_data
from locators.locators_saucedemo import SauceDemoLocators as SDL


# tests block
def test_auth_positive(browser, auth_positive):
    """Test Authorization using correct data"""

    assert browser.current_url == urls.INVENTORY_PAGE_ENDPOINT
    assert browser.title == page_elements_data.invertory_page_title


def test_auth_negative(browser, auth_negative):
    """Test Authorization using incorrect data"""

    login_error_elem = browser.find_element(*SDL.ERROR_LOGIN_MESSAGE)
    background_color_of_error_container = (browser.find_element(*SDL.ERROR_MESSAGE_CONTAINER)
                                           .value_of_css_property("background-color"))

    assert browser.current_url == urls.BASE_URL
    assert login_error_elem.text == page_elements_data.login_error_text
    assert background_color_of_error_container == page_elements_data.background_color_error_container
