import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

# chrome webdriver settings
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")

browser = webdriver.Chrome(options=chrome_options)

# urls
base_curl = "https://www.saucedemo.com/"
inventory_page_endpoint = "https://www.saucedemo.com/inventory.html"

# data
# login page
username_valid = "standard_user"
password = "secret_sauce"

# inventory page
invertory_page_title = "Swag Labs"

# locators
USERNAME_FIELD = ("xpath", "//input[@id='user-name']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")

LOGIN_BUTTON = ("xpath", "//input[@data-test='login-button']")


# tests block
def test_auth_positive():
    browser.get(base_curl)

    browser.find_element(*USERNAME_FIELD).send_keys(username_valid)
    browser.find_element(*PASSWORD_FIELD).send_keys(password)

    browser.find_element(*LOGIN_BUTTON).click()

    assert browser.current_url == inventory_page_endpoint
    assert browser.title == invertory_page_title

    time.sleep(2)
