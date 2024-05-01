from pages.base_page import BasePage

from data.utils import rand_index, get_int_value_from_str, get_length_list
from data.page_data.main_data import MainData


class MainPage(BasePage):
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

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @property
    def get_products_title_text(self):
        return self.get_element_text(self.element_is_visible(self.PRODUCTS_TITLE))

    @property
    def get_list_to_cart_btn(self):
        return self.elements_are_visible(self.ADD_TO_CART_BUTTON)

    @property
    def get_items_card_link_images(self):
        return self.elements_are_visible(self.INVENTORY_ITEMS_CARD_LINK_IMAGE)

    @property
    def select_random_item_index(self):
        return rand_index(get_length_list(self.get_items_card_link_images))

    def get_items_badge_text(self):
        return self.get_element_text(self.element_is_visible(self.SHOPPING_CART_BADGE))

    def click_shopping_cart_link(self):
        return self.click_element(self.SHOPPING_CART_BADGE)

    def check_amount_items_in_cart(self):
        amount_of_items_in_shop_cart_badge = get_int_value_from_str(self.get_items_badge_text())

        assert amount_of_items_in_shop_cart_badge == MainData.count_items_in_cart[0], \
            f"The number in {amount_of_items_in_shop_cart_badge} is not equal {MainData.count_items_in_cart[0]}"

    def add_random_item_from_catalog_to_cart(self):
        """This method add to cart one random product from the main page"""
        selected_item_idx = self.select_random_item_index
        self.get_list_to_cart_btn[selected_item_idx].click()
        self.check_amount_items_in_cart()

    def add_random_item_from_item_card(self):
        selected_item_idx = self.select_random_item_index
        self.get_items_card_link_images[selected_item_idx].click()
        self.check_amount_items_in_cart()
