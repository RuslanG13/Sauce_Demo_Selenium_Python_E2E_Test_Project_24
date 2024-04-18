from locators.main_locators import MainPageLocators as mpl
from locators.locators_saucedemo import CartPageLocators as CPL
from locators.locators_saucedemo import ItemCardDetailLocators as ICD

from data import page_elements_data


class TestCart:
    def test_add_item_through_catalog(self, driver, auth_positive, add_item_to_cart_through_catalog):
        """Test: adding an item to the cart from through catalog"""

        driver.find_element(*mpl.SHOPPING_CART_BADGE).click()

        checkout_button = driver.find_element(*CPL.CHECKOUT_BUTTON)
        numbers_of_items_in_shop_cart = int(driver.find_element(*mpl.SHOPPING_CART_BADGE).text)

        assert checkout_button, "A user isn't at cart page"
        assert numbers_of_items_in_shop_cart == page_elements_data.count_items_in_cart[0], \
            f"The number in shopping cart badge is different than {page_elements_data.count_items_in_cart[0]}"

        item_name_in_cart = driver.find_element(*CPL.CART_ITEMS_NAME).text
        amount_items_in_cart = len(driver.find_elements(*CPL.CART_ITEMS))

        assert item_name_in_cart in page_elements_data.catalog_items_names, "The item's isn't present in the cart"
        assert amount_items_in_cart == page_elements_data.count_items_in_cart[0], \
            f"The amount is different than {page_elements_data.count_items_in_cart[0]} or cart is empty"

    def test_delete_item(self, driver, auth_positive, add_item_to_cart_through_catalog):
        """Test: deleting an item from the cart"""

        driver.find_element(*mpl.SHOPPING_CART_BADGE).click()

        checkout_button = driver.find_element(*CPL.CHECKOUT_BUTTON)
        numbers_of_items_in_shop_cart = int(driver.find_element(*mpl.SHOPPING_CART_BADGE).text)

        assert checkout_button, "A user isn't at cart page"
        assert numbers_of_items_in_shop_cart == page_elements_data.count_items_in_cart[0], \
            f"The number in shopping cart badge is different than {page_elements_data.count_items_in_cart[0]}"

        driver.find_element(*CPL.REMOVE_BUTTON_CART).click()
        amount_items_in_cart = len(driver.find_elements(*CPL.CART_ITEMS))

        assert amount_items_in_cart == 0, "The cart is not empty"

    def test_add_item_through_item_card(self, driver, auth_positive, add_item_to_cart_through_item_card):
        """Test: adding a product to the cart from the item card"""

        driver.find_element(*ICD.SHOPPING_CART_LINK).click()
        amount_items_in_cart = len(driver.find_elements(*CPL.CART_ITEMS))

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
        amount_items_in_cart = len(driver.find_elements(*CPL.CART_ITEMS))

        assert amount_items_in_cart == 0, "The cart is not empty"
