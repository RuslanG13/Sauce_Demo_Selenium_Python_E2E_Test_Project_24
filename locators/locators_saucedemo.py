class LoginPageLocators:
    USERNAME_FIELD = ("xpath", "//input[@id='user-name']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")

    LOGIN_BUTTON = ("xpath", "//input[@data-test='login-button']")

    ERROR_MESSAGE_CONTAINER = ("xpath", "//div[contains(@class, 'error-message-container')]")
    ERROR_LOGIN_MESSAGE = ("xpath", "//h3[@data-test='error']")


class InventoryPageLocators:
    ADD_TO_CART_BUTTON = ("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
    ADD_TO_CART_BUTTONS = ("xpath", "//button[@class='btn btn_primary btn_small btn_inventory ']")

    REMOVE_BUTTON = ("xpath", "//button[@class='btn btn_secondary btn_small btn_inventory ']")
    SHOPPING_CART_LINK = ("xpath", "//a[@data-test='shopping-cart-link']")

    INVENTORY_ITEMS = ("xpath", "//div[@class='inventory_item']")
    INVENTORY_ITEMS_NAME = ("xpath", "//div[@class='inventory_item_name']")

    INVENTORY_ITEMS_PRICES = ("xpath", "//div[@class='inventory_item_price']")

    SHOPPING_CART_BADGE = ("xpath", "//span[@class='shopping_cart_badge']")

    CART_ITEM_LABEL = ("xpath", "cart_item_label")
