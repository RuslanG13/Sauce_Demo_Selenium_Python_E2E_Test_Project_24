class LoginPageLocators:
    USERNAME_FIELD = ("xpath", "//input[@id='user-name']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON = ("xpath", "//input[@data-test='login-button']")

    ERROR_MESSAGE_CONTAINER = ("xpath", "//div[contains(@class, 'error-message-container')]")
    ERROR_LOGIN_MESSAGE = ("xpath", "//h3[@data-test='error']")
    LOGIN_LOGO = ("xpath", "//div[@class='login_logo']")


class InventoryPageLocators:
    ADD_TO_CART_BUTTON = ("xpath", "//button[@class='btn btn_primary btn_small btn_inventory ']")
    REMOVE_BUTTON = ("xpath", "//button[@class='btn btn_secondary btn_small btn_inventory ']")
    SHOPPING_CART_LINK = ("xpath", "//a[@data-test='shopping-cart-link']")

    INVENTORY_ITEMS = ("xpath", "//div[@class='inventory_item']")
    INVENTORY_ITEM_NAME = ("xpath", "//div[@class='inventory_item_name ']")
    INVENTORY_ITEMS_CARD_LINK_IMAGE = ("xpath", "//a[contains(@id, 'img_link')]")

    INVENTORY_ITEMS_PRICE = ("xpath", "//div[@class='inventory_item_price']")
    SHOPPING_CART_BADGE = ("xpath", "//span[@class='shopping_cart_badge']")
    CART_ITEM_LABEL = ("xpath", "cart_item_label")

    DROPDOWN_PRODUCT_SORT_CONTAINER_BTN = ("xpath", "//select[@data-test='product-sort-container']")
    SORT_A_Z_DROPDOWN_ITEM = ("xpath", "//option[text()='Name (A to Z)']")
    SORT_Z_A_DROPDOWN_ITEM = ("xpath", "//option[text()='Name (Z to A)']")
    SORT_LOW_HIGH_DROPDOWN_ITEM = ("xpath", "//option[text()='Price (low to high)']")
    SORT_HIGH_LOW_DROPDOWN_ITEM = ("xpath", "//option[text()='Price (high to low)']")

    BURGER_MENU_BUTTON = ("xpath", "//button[@id='react-burger-menu-btn']")
    LOGOUT_SIDEBAR_LINK = ("xpath", "//a[@id='logout_sidebar_link']")
    PRODUCTS_TITLE = ("xpath", "//span[@data-test='title']")

class CartPageLocators:
    CART_ITEMS = ("xpath", "//div[@class='cart_item']")
    CART_ITEMS_NAME = ("xpath", "//div[@class='inventory_item_name']")
    CART_ITEMS_PRICE = ("xpath", "//div[@class='inventory_item_price']")

    REMOVE_BUTTON_CART = ("xpath", "//button[@class='btn btn_secondary btn_small cart_button']")
    CHECKOUT_BUTTON = ("xpath", "//button[@id='checkout']")
    SHOPPING_CART_BADGE = ("xpath", "//span[@class='shopping_cart_badge']")


class ItemCardDetailLocators:
    ADD_TO_CART_BUTTON = ("xpath", "//button[@id='add-to-cart']")
    ITEM_NAME = ("xpath", "//div[@class='inventory_details_name large_size']")
    SHOPPING_CART_LINK = ("xpath", "//a[@class='shopping_cart_link']")
    REMOVE_BUTTON = ("xpath", "//button[@id='remove']")


class CheckoutPageLocators:
    FIRST_NAME_FIELD = ("xpath", "//input[@id='first-name']")
    LAST_NAME_FIELD = ("xpath", "//input[@id='last-name']")
    POSTAL_CODE_FIELD = ("xpath", "//input[@id='postal-code']")
    CONTINUE_BUTTON = ("xpath", "//input[@id='continue']")

    FINISH_BUTTON = ("xpath", "//button[@id='finish']")
    GREEN_TICK = ("xpath", "//img[@data-test='pony-express']")
    COMPLETE_HEADER = ("xpath", "//h2[@data-test='complete-header']")
