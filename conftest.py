import time

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import urls
from data import input_data
from data import page_elements_data
from data.utils import rand_index

from locators.locators_saucedemo import LoginPageLocators as LPL
from locators.locators_saucedemo import InventoryPageLocators as IPL
from locators.locators_saucedemo import CartPageLocators as CPL


@pytest.fixture()
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    return driver
    # driver.quit()


@pytest.fixture()
def auth_positive(browser):
    browser.get(urls.BASE_URL)

    browser.find_element(*LPL.USERNAME_FIELD).send_keys(input_data.username_valid)
    browser.find_element(*LPL.PASSWORD_FIELD).send_keys(input_data.password_valid)

    browser.find_element(*LPL.LOGIN_BUTTON).click()


@pytest.fixture()
def add_item_to_cart_through_catalog(browser, auth_positive):
    list_catalog_items = browser.find_elements(*IPL.INVENTORY_ITEMS)
    list_add_to_cart_btn = browser.find_elements(*IPL.ADD_TO_CART_BUTTONS)

    selected_item_idx = rand_index(len(list_catalog_items))
    selected_item_name = list_catalog_items[selected_item_idx].text.split("\n")[0]
    list_add_to_cart_btn[selected_item_idx].click()
    numbers_of_items_in_shop_cart = int(browser.find_element(*IPL.SHOPPING_CART_BADGE).text)

    assert selected_item_name in page_elements_data.catalog_items_names, \
        "The selected item not present in catalog"
    assert numbers_of_items_in_shop_cart == page_elements_data.count_items_in_cart[0], \
        f"The number in shopping cart badge is different than {page_elements_data.count_items_in_cart[0]}"

    browser.find_element(*IPL.SHOPPING_CART_BADGE).click()

    checkout_button = browser.find_element(*CPL.CHECKOUT_BUTTON)
    numbers_of_items_in_shop_cart = int(browser.find_element(*IPL.SHOPPING_CART_BADGE).text)

    assert checkout_button, "A user isn't at cart page"
    assert numbers_of_items_in_shop_cart == page_elements_data.count_items_in_cart[0], \
        f"The number in shopping cart badge is different than {page_elements_data.count_items_in_cart[0]}"
