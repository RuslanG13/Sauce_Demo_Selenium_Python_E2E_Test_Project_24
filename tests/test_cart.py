from data import page_elements_data
from locators.locators_saucedemo import InventoryPageLocators as IPL
from locators.locators_saucedemo import CartPageLocators as CPL
from locators.locators_saucedemo import ItemCardDetail as ICD


def test_add_item_to_cart_via_catalog(browser, auth_positive, add_item_to_cart_via_catalog):
    """Test adding an item to the cart from via catalog"""

    browser.find_element(*IPL.SHOPPING_CART_BADGE).click()

    checkout_button = browser.find_element(*CPL.CHECKOUT_BUTTON)
    numbers_of_items_in_shop_cart = int(browser.find_element(*IPL.SHOPPING_CART_BADGE).text)

    assert checkout_button, "A user isn't at cart page"
    assert numbers_of_items_in_shop_cart == page_elements_data.count_items_in_cart[0], \
        f"The number in shopping cart badge is different than {page_elements_data.count_items_in_cart[0]}"

    item_name_in_cart = browser.find_element(*CPL.CART_ITEMS_NAME).text
    amount_items_in_cart = len(browser.find_elements(*CPL.CART_ITEMS))

    assert item_name_in_cart in page_elements_data.catalog_items_names, "The item's isn't present in the cart"
    assert amount_items_in_cart == page_elements_data.count_items_in_cart[0], \
        f"The amount is different than {page_elements_data.count_items_in_cart[0]} or cart is empty"


def test_delete_item_from_cart(browser, auth_positive, add_item_to_cart_via_catalog):
    """Test deleting an item from the cart"""

    browser.find_element(*IPL.SHOPPING_CART_BADGE).click()

    checkout_button = browser.find_element(*CPL.CHECKOUT_BUTTON)
    numbers_of_items_in_shop_cart = int(browser.find_element(*IPL.SHOPPING_CART_BADGE).text)

    assert checkout_button, "A user isn't at cart page"
    assert numbers_of_items_in_shop_cart == page_elements_data.count_items_in_cart[0], \
        f"The number in shopping cart badge is different than {page_elements_data.count_items_in_cart[0]}"

    browser.find_element(*CPL.REMOVE_BUTTON_CART).click()
    amount_items_in_cart = len(browser.find_elements(*CPL.CART_ITEMS))

    assert amount_items_in_cart == 0, "The cart is not empty"


def test_add_item_to_cart_via_item_card(browser, auth_positive, add_item_to_cart_via_item_card):
    """Test adding a product to the cart from the item card"""

    browser.find_element(*ICD.SHOPPING_CART_LINK).click()

    amount_items_in_cart = len(browser.find_elements(*CPL.CART_ITEMS))

    assert amount_items_in_cart == page_elements_data.count_items_in_cart[0], \
        f"The amount is different than {page_elements_data.count_items_in_cart[0]} or cart is empty"


def test_delete_item_from_cart(browser, auth_positive, add_item_to_cart_via_item_card):
    """Removing an item from the cart using the item card"""
    pass
