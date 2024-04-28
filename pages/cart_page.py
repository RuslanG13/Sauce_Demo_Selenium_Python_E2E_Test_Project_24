from pages.base_page import BasePage

from data.utils import get_length_list


class CartPage(BasePage):
    CART_ITEM = ("xpath", "//div[@class='cart_item']")
    CART_ITEM_NAME = ("xpath", "//div[@class='inventory_item_name']")
    CART_ITEMS_PRICE = ("xpath", "//div[@class='inventory_item_price']")

    REMOVE_BUTTON_CART = ("xpath", "//button[@class='btn btn_secondary btn_small cart_button']")
    CHECKOUT_BUTTON = ("xpath", "//button[@id='checkout']")
    SHOPPING_CART_BADGE = ("xpath", "//span[@class='shopping_cart_badge']")
    CONTINUE_SHOPPING_BUTTON = ("xpath", "//button[@id='continue-shopping']")

    BURGER_MENU_BUTTON = ("xpath", "//button[@id='react-burger-menu-btn']")
    RESET_APP_STATE_LINK = ("xpath", "//a[@id='reset_sidebar_link']")

    @property
    def get_item_name_in_cart(self):
        return self.elements_are_visible(self.CART_ITEM)

    @property
    def get_item_title_in_cart_text(self):
        return self.get_element_text(self.element_is_visible(self.CART_ITEM_NAME))

    @property
    def get_amount_items_in_cart(self):
        return get_length_list(self.get_item_name_in_cart)
