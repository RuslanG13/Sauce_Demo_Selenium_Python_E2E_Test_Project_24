from selenium.webdriver.support.select import Select

from data import page_elements_data

from locators.locators_saucedemo import InventoryPageLocators as IPL


def test_check_filter_a_to_z(browser, auth_positive):
    "Test checking the effectiveness of the filter (A-Z)"

    dropdown_filter_product = Select(browser.find_element(*IPL.DROPDOWN_PRODUCT_SORT_CONTAINER))
    filter_a_to_z_option_text = dropdown_filter_product.first_selected_option.text

    assert filter_a_to_z_option_text == page_elements_data.filter_dropdown[0]

    item_names = browser.find_elements(*IPL.INVENTORY_ITEM_NAME)
    list_item_names_text = [item.text for item in item_names]
    sorted_a_z_list = sorted(list_item_names_text)

    assert list_item_names_text == sorted_a_z_list
