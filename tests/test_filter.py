import time

from data import page_elements_data

from locators.locators_saucedemo import InventoryPageLocators as IPL


def test_check_filter_a_to_z(browser, auth_positive):
    """Test checking filter functionality (A to Z)"""
    browser.find_element(*IPL.DROPDOWN_PRODUCT_SORT_CONTAINER_BTN).click()
    browser.find_element(*IPL.SORT_A_Z_DROPDOWN_ITEM).click()

    item_names = browser.find_elements(*IPL.INVENTORY_ITEM_NAME)
    list_item_names_text = [item.text for item in item_names]
    sorted_a_z_list = sorted(list_item_names_text)

    assert list_item_names_text == sorted_a_z_list, "Items sort A to Z is not correct"


def test_check_filter_z_to_a(browser, auth_positive):
    """Test checking filter functionality (Z to A)"""

    browser.find_element(*IPL.DROPDOWN_PRODUCT_SORT_CONTAINER_BTN).click()
    browser.find_element(*IPL.SORT_Z_A_DROPDOWN_ITEM).click()

    item_names = browser.find_elements(*IPL.INVENTORY_ITEM_NAME)
    list_item_names_text = [item.text for item in item_names]
    sorted_z_a_list = sorted(list_item_names_text, reverse=True)

    assert list_item_names_text == sorted_z_a_list, "Items sort Z to A is not correct"
