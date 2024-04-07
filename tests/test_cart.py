from data import page_elements_data
from locators.locators_saucedemo import CartPageLocators as CPL


def test_add_item_to_cart_through_catalog(browser, auth_positive, add_item_to_cart):
    """Test adding an item to the cart from catalog"""

    item_name_in_cart = browser.find_element(*CPL.CART_ITEMS_NAME).text
    amount_items_in_cart = len(browser.find_elements(*CPL.CART_ITEMS))

    assert item_name_in_cart in page_elements_data.catalog_items_names, "The item's isn't present in the cart"
    assert amount_items_in_cart == page_elements_data.count_items_in_cart[0], \
        f"The amount is different than {page_elements_data.count_items_in_cart[0]} or cart is empty"


def test_delete_item_from_cart(browser, auth_positive, add_item_to_cart):
    browser.find_element(*CPL.REMOVE_BUTTON_CART).click()
    amount_items_in_cart = len(browser.find_elements(*CPL.CART_ITEMS))

    assert amount_items_in_cart == 0, "The cart is not empty"
