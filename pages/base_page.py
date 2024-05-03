from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from data.utils import get_int_value_from_str


class BasePage:
    SHOPPING_CART_BADGE_LOCATOR = ("xpath", "//span[@class='shopping_cart_badge']")
    SHOPPING_CART_LINK_LOCATOR = ("xpath", "//a[@class='shopping_cart_link']")
    REMOVE_BUTTON_LOCATOR = ("xpath", "//button[@id='remove']")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    @property
    def get_items_badge_text(self):
        return self.get_element_text(self.element_is_visible(self.SHOPPING_CART_BADGE_LOCATOR))

    def open_page(self):
        return self.driver.get(self.url)

    def get_url_text(self):
        return self.driver.current_url

    def element_is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def elements_are_visible(self, locator):
        return self.wait.until(ec.visibility_of_all_elements_located(locator))

    def element_is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def element_is_invisible(self, locator):
        return self.wait.until(ec.invisibility_of_element(locator))

    def click_element(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator)).click()

    def get_ccs_property(self, locator, css_property):
        return self.element_is_visible(locator).value_of_css_property(css_property)

    def get_length_list_web_elements(self, locator):
        return len(self.elements_are_visible(locator))

    def click_remove_button(self):
        self.click_element(self.REMOVE_BUTTON_LOCATOR)

    def click_shopping_cart_link(self):
        self.click_element(self.SHOPPING_CART_LINK_LOCATOR)

    def check_amount_items_in_cart_badge(self, num_of_items_in_cart_badge: int):
        """This method checks amount of items in shopping cart badge"""
        amount_of_items_in_shop_cart_badge = get_int_value_from_str(self.get_items_badge_text)

        assert amount_of_items_in_shop_cart_badge == num_of_items_in_cart_badge, \
            f"The number in {amount_of_items_in_shop_cart_badge} is not equal {num_of_items_in_cart_badge}"

    @staticmethod
    def element_is_displayed(web_element):
        return web_element.is_displayed()

    @staticmethod
    def get_element_text(web_element):
        return web_element.text
