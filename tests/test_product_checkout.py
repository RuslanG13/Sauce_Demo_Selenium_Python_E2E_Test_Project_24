from locators.main_locators import MainPageLocators as mlp
from locators.locators_saucedemo import CartPageLocators as CPL
from locators.locators_saucedemo import CheckoutPageLocators as CheckPL

from data import page_elements_data
from data.utils import fake_first_name_data, fake_last_name_data, fake_post_code_data


class TestProductCheckout:
    def test_product_checkout_with_valid_data(self, driver, auth_positive, add_item_to_cart_through_catalog):
        """Test: checkout product using correct data"""

        driver.find_element(*mlp.SHOPPING_CART_BADGE).click()

        checkout_button = driver.find_element(*CPL.CHECKOUT_BUTTON)
        numbers_of_items_in_shop_cart = int(driver.find_element(*mlp.SHOPPING_CART_BADGE).text)

        assert checkout_button, "A user isn't at cart page"
        assert numbers_of_items_in_shop_cart == page_elements_data.count_items_in_cart[0], \
            f"The number in shopping cart badge is different than {page_elements_data.count_items_in_cart[0]}"

        checkout_button.click()

        first_name_data = fake_first_name_data()
        last_name_data = fake_last_name_data()
        postalcode_data = fake_post_code_data()

        first_name_field = driver.find_element(*CheckPL.FIRST_NAME_FIELD)
        first_name_field.send_keys(first_name_data)

        last_name_field = driver.find_element(*CheckPL.LAST_NAME_FIELD)
        last_name_field.send_keys(last_name_data)

        postalcode_field = driver.find_element(*CheckPL.POSTAL_CODE_FIELD)
        postalcode_field.send_keys(postalcode_data)

        assert first_name_field.get_attribute("value") == first_name_data, "Entered first name data does not match"
        assert last_name_field.get_attribute("value") == last_name_data, "Entered last name data does not match"
        assert postalcode_field.get_attribute("value") == postalcode_data, "Entered postalcode data does not match"

        driver.find_element(*CheckPL.CONTINUE_BUTTON).click()
        driver.find_element(*CheckPL.FINISH_BUTTON).click()

        complete_checkout_header_text = driver.find_element(*CheckPL.COMPLETE_HEADER).text

        green_tick_img = driver.find_element(*CheckPL.GREEN_TICK)
        green_tick_img_alt_text = green_tick_img.get_attribute("alt")

        assert complete_checkout_header_text == page_elements_data.complete_checkout_header, \
            "complete header does not match"
        assert green_tick_img_alt_text == page_elements_data.green_tick_img_alt_text
