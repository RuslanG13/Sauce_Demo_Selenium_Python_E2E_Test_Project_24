import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import urls
from data import input_data
from data import page_elements_data
from locators.locators_saucedemo import LoginPageLocators as LPL
from locators.locators_saucedemo import InventoryPageLocators as IPL


@pytest.fixture()
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    return driver
    # driver.quit()


@pytest.fixture()
def auth_positive(browser):
    browser.get(urls.BASE_URL)

    browser.find_element(*LPL.USERNAME_FIELD).send_keys(input_data.username_valid)
    browser.find_element(*LPL.PASSWORD_FIELD).send_keys(input_data.password_valid)

    browser.find_element(*LPL.LOGIN_BUTTON).click()


@pytest.fixture()
def add_goods_to_cart(browser, auth_positive):
    item_name_catalog = browser.find_elements(*IPL.INVENTORY_ITEMS)[0].text.split("\n")[0]
    item_price_catalog = browser.find_elements(*IPL.INVENTORY_ITEMS_PRICE)[0].text

    assert item_name_catalog == page_elements_data.catalog_items_names[0]
    assert item_price_catalog == page_elements_data.catalog_items_price[0]

    browser.find_elements(*IPL.ADD_TO_CART_BUTTONS)[0].click()

    assert browser.find_element(*IPL.REMOVE_BUTTON).text == page_elements_data.remove_button_name
    assert browser.find_element(*IPL.SHOPPING_CART_BADGE).text == page_elements_data.count_items_in_cart[0]

    browser.find_element(*IPL.SHOPPING_CART_BADGE).click()
