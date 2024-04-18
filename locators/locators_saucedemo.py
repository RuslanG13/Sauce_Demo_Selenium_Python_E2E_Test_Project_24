class AboutSauceLabPageLocators:
    SAUCELABS_LOGO = ("xpath", "//img[@src='/images/logo.svg']")


class CartPageLocators:
    CART_ITEMS = ("xpath", "//div[@class='cart_item']")
    CART_ITEMS_NAME = ("xpath", "//div[@class='inventory_item_name']")
    CART_ITEMS_PRICE = ("xpath", "//div[@class='inventory_item_price']")

    REMOVE_BUTTON_CART = ("xpath", "//button[@class='btn btn_secondary btn_small cart_button']")
    CHECKOUT_BUTTON = ("xpath", "//button[@id='checkout']")
    SHOPPING_CART_BADGE = ("xpath", "//span[@class='shopping_cart_badge']")
    CONTINUE_SHOPPING_BUTTON = ("xpath", "//button[@id='continue-shopping']")

    BURGER_MENU_BUTTON = ("xpath", "//button[@id='react-burger-menu-btn']")
    RESET_APP_STATE_LINK = ("xpath", "//a[@id='reset_sidebar_link']")


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
