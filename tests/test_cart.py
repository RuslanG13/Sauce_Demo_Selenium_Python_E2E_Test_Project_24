import allure

from locators.locators_saucedemo import ItemCardDetailLocators as ICD

from pages.cart_page import CartPage

from data import page_elements_data
from data.page_data.login_data import LoginData
from data.page_data.main_data import MainData


@allure.feature("Shopping Cart")
class TestCart:
    @allure.title("TC_02_01 - Verify adding a product to the cart through the catalog")
    def test_add_item_through_catalog(self, login_page, main_page, cart_page):
        """Verify success in adding a product to the cart through the catalog"""
        login_page.login(username=LoginData.valid_login_data[0], password=LoginData.valid_login_data[1])
        main_page.add_random_item_from_catalog_to_cart()
        main_page.click_shopping_cart_link()

        item_title_in_cart = cart_page.get_item_title_in_cart_text
        amount_items_in_cart = cart_page.get_amount_items_in_cart

        assert item_title_in_cart in MainData.catalog_items_names, \
            f"The selected {item_title_in_cart} item is not present in the cart"
        assert amount_items_in_cart == MainData.count_items_in_cart[0], \
            f"The {amount_items_in_cart} amount is not equal {MainData.count_items_in_cart[0]}"

    @allure.title("TC_02_02 - Verify removing an item from the cart via the cart")
    def test_delete_item(self, login_page, main_page, cart_page):
        """Verify success in deleting a product from the cart"""
        login_page.login(username=LoginData.valid_login_data[0], password=LoginData.valid_login_data[1])
        main_page.add_random_item_from_catalog_to_cart()
        main_page.click_shopping_cart_link()
        cart_page.click_remove_button()

        is_no_items_in_cart = cart_page.is_cart_empty()

        assert is_no_items_in_cart is True, "The cart is not empty"

    def test_add_item_through_item_card(self, driver, auth_positive, add_item_to_cart_through_item_card):
        """Test: adding a product to the cart from the item card"""

        driver.find_element(*ICD.SHOPPING_CART_LINK).click()
        amount_items_in_cart = len(driver.find_elements(*CartPage.CART_ITEM))

        assert amount_items_in_cart == page_elements_data.count_items_in_cart[0], \
            f"The amount is different than {page_elements_data.count_items_in_cart[0]} or cart is empty"

    def test_delete_item_through_item_card(self, driver, auth_positive, add_item_to_cart_through_item_card):
        """Test: removing an item from the cart using the item card"""

        remove_button = driver.find_element(*ICD.REMOVE_BUTTON)
        assert remove_button, "The 'remove' button is not displayed in the item card"

        remove_button.click()

        add_to_cart_button = driver.find_element(*ICD.ADD_TO_CART_BUTTON)
        assert add_to_cart_button, "The 'Add to cart' button is not displayed in the item card"

        driver.find_element(*ICD.SHOPPING_CART_LINK).click()
        amount_items_in_cart = len(driver.find_elements(*CartPage.CART_ITEM))

        assert amount_items_in_cart == 0, "The cart is not empty"
