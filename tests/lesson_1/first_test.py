from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

import data.urls as urls
import data.input_data as input_data
import data.page_elements_data as page_elements_data
from locators.locators_saucedemo import SauceDemoLocators as SDL

# chrome webdriver settings
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")

browser = webdriver.Chrome(options=chrome_options)


# tests block
def test_auth_positive():
    browser.get(urls.BASE_URL)

    browser.find_element(*SDL.USERNAME_FIELD).send_keys(input_data.username_valid)
    browser.find_element(*SDL.PASSWORD_FIELD).send_keys(input_data.password)

    browser.find_element(*SDL.LOGIN_BUTTON).click()

    assert browser.current_url == urls.INVENTORY_PAGE_ENDPOINT
    assert browser.title == page_elements_data.invertory_page_title
