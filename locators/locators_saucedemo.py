class LoginPageLocators:
    USERNAME_FIELD = ("xpath", "//input[@id='user-name']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")

    LOGIN_BUTTON = ("xpath", "//input[@data-test='login-button']")

    ERROR_MESSAGE_CONTAINER = ("xpath", "//div[contains(@class, 'error-message-container')]")
    ERROR_LOGIN_MESSAGE = ("xpath", "//h3[@data-test='error']")


class InventoryPageLocators:
    # ADD_TO_CART_BUTTON = ("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
    ADD_TO_CART_BUTTON = ("xpath", "//button[@class='btn btn_primary btn_small btn_inventory ']")

    REMOVE_BUTTON = ("xpath", "//button[@class='btn btn_secondary btn_small btn_inventory ']")
    SHOPPING_CART_LINK = ("xpath", "//a[@data-test='shopping-cart-link']")

    INVENTORY_ITEMS = ("xpath", "//div[@class='inventory_item']")
    INVENTORY_ITEMS_NAME = ("xpath", "//div[@class='inventory_item_name'] ")
    INVENTORY_ITEMS_CARD_LINK = ("xpath", "//a[contains(@id, 'img_link')]")

    INVENTORY_ITEMS_PRICE = ("xpath", "//div[@class='inventory_item_price']")

    SHOPPING_CART_BADGE = ("xpath", "//span[@class='shopping_cart_badge']")

    CART_ITEM_LABEL = ("xpath", "cart_item_label")


class CartPageLocators:
    CART_ITEMS = ("xpath", "//div[@class='cart_item']")
    CART_ITEMS_NAME = ("xpath", "//div[@class='inventory_item_name']")

    CART_ITEMS_PRICE = ("xpath", "//div[@class='inventory_item_price']")

    REMOVE_BUTTON_CART = ("xpath", "//button[@class='btn btn_secondary btn_small cart_button']")

    CHECKOUT_BUTTON = ("xpath", "//button[@id='checkout']")

    SHOPPING_CART_BADGE = ("xpath", "//span[@class='shopping_cart_badge']")


class ItemCardDetail:
    ADD_TO_CART_BUTTON = ("xpath", "//button[@id='add-to-cart']")
    ITEM_NAME_CARD_DETAIL = ("xpath", "//div[@class='inventory_details_name large_size']")

    SHOPPING_CART_LINK = ("xpath", "//a[@class='shopping_cart_link']")

    REMOVE_BUTTON = ("xpath", "//button[@id='remove']")
