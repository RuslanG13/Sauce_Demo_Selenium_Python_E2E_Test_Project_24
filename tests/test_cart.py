import allure

from data.login_data import LoginData
from data.cart_data import CartData
from data.main_data import MainData
from data.item_card_data import ItemCardData


@allure.feature("Shopping Cart")
class TestCart:

    @allure.title("TC_02_01 | Verify adding a product to the cart through the catalog")
    def test_add_item_through_catalog(self, login_page, main_page, cart_page):
        """Verify success in adding a product to the cart through the catalog"""
        login_page.login(username=LoginData.valid_username, password=LoginData.valid_password)
        main_page.add_item_to_cart_from_catalog()
        main_page.check_amount_items_in_cart_badge(MainData.items_in_shop_cart_badge[0])
        main_page.click_shopping_cart_link()

        item_title_in_cart = cart_page.get_item_title_in_cart_text
        amount_items_in_cart = cart_page.get_amount_items_in_cart

        assert item_title_in_cart in CartData.catalog_items_names, \
            f"The selected {item_title_in_cart} item is not present in the cart"
        assert amount_items_in_cart == CartData.items_in_shop_cart_badge[0], \
            f"The {amount_items_in_cart} amount is not equal {CartData.items_in_shop_cart_badge[0]}"

    @allure.title("TC_02_02 | Verify removing an item from the cart via the cart")
    def test_delete_item(self, login_page, main_page, cart_page):
        """Verify success in deleting a product from the cart"""
        login_page.login(username=LoginData.valid_username, password=LoginData.valid_password)
        main_page.add_item_to_cart_from_catalog()
        main_page.check_amount_items_in_cart_badge(MainData.items_in_shop_cart_badge[0])
        main_page.click_shopping_cart_link()
        cart_page.click_remove_button()

        is_no_items_in_cart = cart_page.is_cart_empty()

        assert is_no_items_in_cart is True, "The cart is not empty"

    @allure.title("TC_02_03 | Verify adding a product to the cart from the product card")
    def test_add_item_through_item_card(self, login_page, main_page, item_card_page, cart_page):
        """Verify success in adding a product to the cart through the product card"""
        login_page.login(username=LoginData.valid_username, password=LoginData.valid_password)
        main_page.open_specific_item_card()
        item_card_page.click_add_to_cart_btn()
        item_card_page.check_amount_items_in_cart_badge(ItemCardData.items_in_shop_cart_badge[0])
        item_card_page.click_shopping_cart_link()

        item_title_in_cart = cart_page.get_item_title_in_cart_text
        amount_items_in_cart = cart_page.get_amount_items_in_cart

        assert item_title_in_cart in CartData.catalog_items_names, \
            f"The selected {item_title_in_cart} item is not present in the cart"
        assert amount_items_in_cart == CartData.items_in_shop_cart_badge[0], \
            f"The {amount_items_in_cart} amount is not equal {CartData.items_in_shop_cart_badge[0]}"

    @allure.title("TC_02_04 | Verify removing an item from the cart using the item card")
    def test_delete_item_through_item_card(self, login_page, main_page, item_card_page, cart_page):
        """Verify success in deleting a product from the cart through item card"""
        login_page.login(username=LoginData.valid_username, password=LoginData.valid_password)
        main_page.open_specific_item_card()
        item_card_page.click_add_to_cart_btn()
        item_card_page.check_amount_items_in_cart_badge(ItemCardData.items_in_shop_cart_badge[0])
        item_card_page.click_remove_button()
        item_card_page.check_displays_of_add_to_cart_btn()
        item_card_page.click_shopping_cart_link()

        is_no_items_in_cart = cart_page.is_cart_empty()

        assert is_no_items_in_cart is True, "The cart is not empty"
