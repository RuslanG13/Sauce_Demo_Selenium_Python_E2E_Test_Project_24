from pages.base_page import BasePage

from data.utils import get_int_value_from_str


class ItemCardPage(BasePage):
    ADD_TO_CART_BUTTON = ("xpath", "//button[@class='btn btn_primary btn_small btn_inventory']")
    SHOPPING_CART_BADGE = ("xpath", "//span[@class='shopping_cart_badge']")

    def __init__(self, driver):
        super().__init__(driver=driver, url=None)

    @property
    def get_items_badge_text(self):
        return self.get_element_text(self.element_is_visible(self.SHOPPING_CART_BADGE))

    def click_shopping_cart_link(self):
        return self.click_element(self.SHOPPING_CART_BADGE)

    def click_add_to_cart_btn(self):
        return self.element_is_clickable(self.ADD_TO_CART_BUTTON).click()

    def check_amount_items_in_cart_badge(self, num_of_items_in_cart_badge):
        """This method checks amount of items in shopping cart badge"""
        amount_of_items_in_shop_cart_badge = get_int_value_from_str(self.get_items_badge_text)

        assert amount_of_items_in_shop_cart_badge == num_of_items_in_cart_badge, \
            f"The number in {amount_of_items_in_shop_cart_badge} is not equal {num_of_items_in_cart_badge}"
