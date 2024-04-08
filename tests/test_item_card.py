from locators.locators_saucedemo import InventoryPageLocators as IPL
from locators.locators_saucedemo import ItemCardDetailLocators as ICD
from data.utils import rand_index


def test_successful_redirect_to_item_card_after_click_item_image(browser, auth_positive):
    """Test successful redirect to the item card after clicking on the item image"""

    list_catalog_items = browser.find_elements(*IPL.INVENTORY_ITEMS)
    list_catalog_items_image = browser.find_elements(*IPL.INVENTORY_ITEMS_CARD_LINK_IMAGE)

    selected_item_idx = rand_index(len(list_catalog_items))
    selected_item_name_on_catalog = list_catalog_items[selected_item_idx].text.split("\n")[0]

    list_catalog_items_image[selected_item_idx].click()

    selected_item_name_on_item_card = browser.find_element(*ICD.ITEM_NAME).text.split("\n")[0]

    assert selected_item_name_on_item_card == selected_item_name_on_catalog, \
        f"The item names {selected_item_name_on_item_card} and {selected_item_name_on_catalog} did not match"


def test_successful_redirect_to_item_card_after_click_item_name(browser, auth_positive):
    """Test successful redirect to the item card after clicking on the item name"""

    list_catalog_items_name = browser.find_elements(*IPL.INVENTORY_ITEM_NAME)

    selected_item_idx = rand_index(len(list_catalog_items_name))
    selected_item_name_on_catalog = list_catalog_items_name[selected_item_idx].text

    list_catalog_items_name[selected_item_idx].click()

    selected_item_name_on_item_card = browser.find_element(*ICD.ITEM_NAME).text.split("\n")[0]

    assert selected_item_name_on_item_card == selected_item_name_on_catalog, \
        f"The item names {selected_item_name_on_item_card} and {selected_item_name_on_catalog} did not match"