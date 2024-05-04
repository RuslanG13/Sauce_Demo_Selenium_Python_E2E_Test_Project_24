from pages.base_page import BasePage

from data.utils import rand_index, get_length_list


class MainPage(BasePage):
    PRODUCTS_TITLE_LOCATOR = ("xpath", "//span[@data-test='title']")

    ADD_TO_CART_BUTTON_LOCATOR = ("xpath", "//button[@class='btn btn_primary btn_small btn_inventory ']")
    REMOVE_BUTTON = ("xpath", "//button[@class='btn btn_secondary btn_small btn_inventory ']")
    SHOPPING_CART_LINK_LOCATOR = ("xpath", "//a[@data-test='shopping-cart-link']")

    INVENTORY_ITEMS = ("xpath", "//div[@class='inventory_item']")
    INVENTORY_ITEM_NAME = ("xpath", "//div[@class='inventory_item_name ']")
    INVENTORY_ITEMS_CARD_LINK_IMAGE_LOCATOR = ("xpath", "//a[contains(@id, 'img_link')]")

    INVENTORY_ITEMS_PRICE = ("xpath", "//div[@class='inventory_item_price']")

    CART_ITEM_LABEL = ("xpath", "cart_item_label")

    DROPDOWN_PRODUCT_SORT_CONTAINER_BTN = ("xpath", "//select[@data-test='product-sort-container']")
    SORT_A_Z_DROPDOWN_ITEM = ("xpath", "//option[text()='Name (A to Z)']")
    SORT_Z_A_DROPDOWN_ITEM = ("xpath", "//option[text()='Name (Z to A)']")
    SORT_LOW_HIGH_DROPDOWN_ITEM = ("xpath", "//option[text()='Price (low to high)']")
    SORT_HIGH_LOW_DROPDOWN_ITEM = ("xpath", "//option[text()='Price (high to low)']")

    BURGER_MENU_BUTTON = ("xpath", "//button[@id='react-burger-menu-btn']")
    LOGOUT_SIDEBAR_LINK = ("xpath", "//a[@id='logout_sidebar_link']")
    ABOUT_SIDEBAR_LINK = ("xpath", "//a[@id='about_sidebar_link']")

    @property
    def get_products_title_text(self):
        return self.get_element_text(self.element_is_visible(self.PRODUCTS_TITLE_LOCATOR))

    @property
    def get_list_add_to_cart_btn(self):
        return self.elements_are_visible(self.ADD_TO_CART_BUTTON_LOCATOR)

    @property
    def get_items_card_link_images(self):
        return self.elements_are_visible(self.INVENTORY_ITEMS_CARD_LINK_IMAGE_LOCATOR)

    @property
    def select_random_item_index(self):
        """This property returns a random item from a product catalog"""
        return rand_index(get_length_list(self.get_items_card_link_images))

    def add_item_to_cart_from_catalog(self):
        """This method adds to cart one random product from the main page"""
        selected_item_idx = self.select_random_item_index
        self.get_list_add_to_cart_btn[selected_item_idx].click()

    def open_specific_item_card_click_by_item_image(self):
        """This method redirect user to an item of selected product"""
        selected_item_idx = self.select_random_item_index
        self.get_items_card_link_images[selected_item_idx].click()
