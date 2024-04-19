class MainPageLocators:
    PRODUCTS_TITLE = ("xpath", "//span[@data-test='title']")

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
    ABOUT_SIDEBAR_LINK = ("xpath", "//a[@id='about_sidebar_link']")