import time

import allure

from locators.locators_saucedemo import ItemCardDetailLocators as ICD

from pages.main_page import MainPage
from data.login_data import LoginData

from data.utils import rand_index


class TestProductCard:

    @allure.title("TC_03_01 | Verify successful redirect to the product card after clicking on the item image")
    def test_redirect_to_product_card_after_click_product_image(self, login_page, main_page, item_card_page):
        """Verify successful redirect to the product card after clicking on the item image"""
        login_page.login(username=LoginData.valid_username, password=LoginData.valid_password)
        main_page.open_specific_item_card_click_by_item_image()

        is_back_to_products_btn_displayed = item_card_page.is_back_to_products_brn_displayed()

        assert is_back_to_products_btn_displayed is True, \
            "A user was not redirected to the product card after clicking on the item image"

    def test_redirect_to_product_card_after_click_product_name(self, driver, auth_positive):
        """Test: successful redirect to the product card after clicking on the product name"""

        list_catalog_items_name = driver.find_elements(*MainPage.INVENTORY_ITEM_NAME)

        selected_item_idx = rand_index(len(list_catalog_items_name))
        selected_item_name_on_catalog = list_catalog_items_name[selected_item_idx].text

        list_catalog_items_name[selected_item_idx].click()

        selected_item_name_on_item_card = driver.find_element(*ICD.ITEM_NAME).text.split("\n")[0]

        assert selected_item_name_on_item_card == selected_item_name_on_catalog, \
            f"The product names {selected_item_name_on_item_card} and {selected_item_name_on_catalog} did not match"
