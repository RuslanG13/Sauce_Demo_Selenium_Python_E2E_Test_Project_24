from pages.base_page import BasePage

from data.utils import get_length_list


class CartPage(BasePage):
    CART_ITEM_LOCATOR = ("xpath", "//div[@class='cart_item']")
    CART_ITEM_NAME_LOCATOR = ("xpath", "//div[@class='inventory_item_name']")
    CART_ITEMS_PRICE_LOCATOR = ("xpath", "//div[@class='inventory_item_price']")

    REMOVE_BUTTON_CART_LOCATOR = ("xpath", "//button[@class='btn btn_secondary btn_small cart_button']")
    CHECKOUT_BUTTON_LOCATOR = ("xpath", "//button[@id='checkout']")
    SHOPPING_CART_BADGE_LOCATOR = ("xpath", "//span[@class='shopping_cart_badge']")
    CONTINUE_SHOPPING_BUTTON_LOCATOR = ("xpath", "//button[@id='continue-shopping']")

    BURGER_MENU_BUTTON_LOCATOR = ("xpath", "//button[@id='react-burger-menu-btn']")
    RESET_APP_STATE_LINK_LOCATOR = ("xpath", "//a[@id='reset_sidebar_link']")

    @property
    def get_items_in_cart(self):
        return self.elements_are_visible(self.CART_ITEM_LOCATOR)

    def is_cart_empty(self):
        return self.element_is_invisible(self.CART_ITEM_LOCATOR)

    @property
    def get_item_title_in_cart_text(self):
        return self.get_element_text(self.element_is_visible(self.CART_ITEM_NAME_LOCATOR))

    def click_remove_button(self):
        return self.click_element(self.REMOVE_BUTTON_CART_LOCATOR)

    @property
    def get_amount_items_in_cart(self):
        return get_length_list(self.get_items_in_cart)
