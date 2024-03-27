from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

from data import urls
from data import input_data
from data import page_elements_data
from locators.locators_saucedemo import SauceDemoLocators as SDL

# chrome webdriver settings
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")

browser = webdriver.Chrome(options=chrome_options)


# tests block
def test_auth_positive():
    """Authorization using correct data"""

    browser.get(urls.BASE_URL)

    browser.find_element(*SDL.USERNAME_FIELD).send_keys(input_data.username_valid)
    browser.find_element(*SDL.PASSWORD_FIELD).send_keys(input_data.password_valid)

    browser.find_element(*SDL.LOGIN_BUTTON).click()

    assert browser.current_url == urls.INVENTORY_PAGE_ENDPOINT
    assert browser.title == page_elements_data.invertory_page_title


def test_auth_negative():
    """Authorization using incorrect data"""

    browser.get(urls.BASE_URL)

    browser.find_element(*SDL.USERNAME_FIELD).send_keys(input_data.username_invalid)
    browser.find_element(*SDL.PASSWORD_FIELD).send_keys(input_data.password_invalid)

    browser.find_element(*SDL.LOGIN_BUTTON).click()

    login_error_elem = browser.find_element(*SDL.ERROR_LOGIN_MESSAGE)
    background_color_of_error_container = (browser.find_element(*SDL.ERROR_MESSAGE_CONTAINER)
                                           .value_of_css_property("background-color"))

    assert browser.current_url == urls.BASE_URL
    assert login_error_elem.text == page_elements_data.login_error_text
    assert background_color_of_error_container == page_elements_data.background_color_error_container
