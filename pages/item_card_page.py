from pages.base_page import BasePage


class ItemCardPage(BasePage):
    ADD_TO_CART_BUTTON_ITEM_CARD_LOCATOR = ("xpath", "//button[@class='btn btn_primary btn_small btn_inventory']")

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

    @property
    def get_add_to_cart_btn(self):
        return self.element_is_visible(self.ADD_TO_CART_BUTTON_ITEM_CARD_LOCATOR)

    def click_add_to_cart_btn(self):
        self.click_element(self.ADD_TO_CART_BUTTON_ITEM_CARD_LOCATOR)

    def check_displays_of_add_to_cart_btn(self):
        assert self.get_add_to_cart_btn.is_displayed()
