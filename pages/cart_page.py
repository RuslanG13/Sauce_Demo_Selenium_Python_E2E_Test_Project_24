from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = ("xpath", "//div[@class='cart_item']")
    CART_ITEMS_NAME = ("xpath", "//div[@class='inventory_item_name']")
    CART_ITEMS_PRICE = ("xpath", "//div[@class='inventory_item_price']")

    REMOVE_BUTTON_CART = ("xpath", "//button[@class='btn btn_secondary btn_small cart_button']")
    CHECKOUT_BUTTON = ("xpath", "//button[@id='checkout']")
    SHOPPING_CART_BADGE = ("xpath", "//span[@class='shopping_cart_badge']")
    CONTINUE_SHOPPING_BUTTON = ("xpath", "//button[@id='continue-shopping']")

    BURGER_MENU_BUTTON = ("xpath", "//button[@id='react-burger-menu-btn']")
    RESET_APP_STATE_LINK = ("xpath", "//a[@id='reset_sidebar_link']")
