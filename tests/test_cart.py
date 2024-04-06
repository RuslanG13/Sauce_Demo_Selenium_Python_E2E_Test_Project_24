import time

from data import urls
from data import page_elements_data
from locators.locators_saucedemo import InventoryPageLocators as IPL
from locators.locators_saucedemo import CartPageLocators as CPL


def test_add_goods_to_cart_through_catalog(browser, auth_positive, add_goods_to_cart):
    """Test adding an item to the cart from catalog"""

    item_name_cart = browser.find_element(*CPL.CART_ITEMS_NAME).text
    item_price_cart = browser.find_element(*CPL.CART_ITEMS_PRICE).text

    assert item_name_cart == page_elements_data.catalog_items_names[0]
    assert item_price_cart == page_elements_data.catalog_items_price[0]

# def test_delete_item_from_cart(browser, auth_positive):
#     """Test delete an item from the cart"""
#
#     item_name_catalog = browser.find_elements(*IPL.INVENTORY_ITEMS)[0].text.split("\n")[0]
#     item_price_catalog = browser.find_elements(*IPL.INVENTORY_ITEMS_PRICES)[0].text
#
#     assert item_name_catalog == page_elements_data.catalog_items_names[0]
#     assert item_price_catalog == page_elements_data.catalog_items_price[0]
#
#     browser.find_elements(*IPL.ADD_TO_CART_BUTTONS)[0].click()
#
#     assert browser.find_element(*IPL.REMOVE_BUTTON).text == page_elements_data.remove_button_name
#     assert browser.find_element(*IPL.SHOPPING_CART_BADGE).text == page_elements_data.count_items_in_cart[0]
#
#     browser.find_element(*IPL.SHOPPING_CART_BADGE).click()
#
#     item_name_cart = browser.find_element(*IPL.INVENTORY_ITEMS_NAME).text
#     item_price_cart = browser.find_element(*IPL.INVENTORY_ITEMS_PRICES).text
#
#     assert item_name_cart == page_elements_data.catalog_items_names[0]
#     assert item_price_cart == page_elements_data.catalog_items_price[0]
