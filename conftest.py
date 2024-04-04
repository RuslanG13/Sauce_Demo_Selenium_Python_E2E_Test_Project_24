import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import urls
from data import input_data
from locators.locators_saucedemo import LoginPageLocators as LPL


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    return driver
    # driver.quit()


@pytest.fixture(scope="function")
def auth_positive(browser):
    browser.get(urls.BASE_URL)

    browser.find_element(*LPL.USERNAME_FIELD).send_keys(input_data.username_valid)
    browser.find_element(*LPL.PASSWORD_FIELD).send_keys(input_data.password_valid)

    browser.find_element(*LPL.LOGIN_BUTTON).click()


@pytest.fixture(scope="function")
def auth_negative(browser):
    browser.get(urls.BASE_URL)

    browser.find_element(*LPL.USERNAME_FIELD).send_keys(input_data.username_invalid)
    browser.find_element(*LPL.PASSWORD_FIELD).send_keys(input_data.password_invalid)

    browser.find_element(*LPL.LOGIN_BUTTON).click()
