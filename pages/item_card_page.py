from pages.base_page import BasePage


class ItemCardPage(BasePage):
    ADD_TO_CART_BUTTON_ITEM_CARD_LOCATOR = ("xpath", "//button[@class='btn btn_primary btn_small btn_inventory']")
    BACK_TO_PRODUCTS_BUTTON_LOCATOR = ("xpath", "//button[@id='back-to-products']")

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

    @property
    def get_add_to_cart_btn(self):
        return self.element_is_visible(self.ADD_TO_CART_BUTTON_ITEM_CARD_LOCATOR)

    @property
    def get_back_to_products_btn(self):
        return self.element_is_visible(self.BACK_TO_PRODUCTS_BUTTON_LOCATOR)

    def click_add_to_cart_btn(self):
        self.click_element(self.ADD_TO_CART_BUTTON_ITEM_CARD_LOCATOR)

    def check_displays_of_add_to_cart_btn(self):
        assert self.get_add_to_cart_btn.is_displayed()

    def is_back_to_products_brn_displayed(self):
        return self.element_is_displayed(self.get_back_to_products_btn)
