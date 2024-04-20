from pages.main_page import MainPage


class TestFilter:
    def test_check_by_name_a_to_z(self, driver, auth_positive):
        """Test: checking filter functionality (A to Z)"""

        driver.find_element(*MainPage.DROPDOWN_PRODUCT_SORT_CONTAINER_BTN).click()
        driver.find_element(*MainPage.SORT_A_Z_DROPDOWN_ITEM).click()

        item_names = driver.find_elements(*MainPage.INVENTORY_ITEM_NAME)
        list_items_name_text = [item.text for item in item_names]
        sorted_a_to_z_list = sorted(list_items_name_text)

        assert list_items_name_text == sorted_a_to_z_list, "Items name sort A to Z is not correct"

    def test_check_by_name_z_to_a(self, driver, auth_positive):
        """Test: checking filter functionality (Z to A)"""

        driver.find_element(*MainPage.DROPDOWN_PRODUCT_SORT_CONTAINER_BTN).click()
        driver.find_element(*MainPage.SORT_Z_A_DROPDOWN_ITEM).click()

        item_names = driver.find_elements(*MainPage.INVENTORY_ITEM_NAME)
        list_items_name_text = [item.text for item in item_names]
        sorted_z_to_a_list = sorted(list_items_name_text, reverse=True)

        assert list_items_name_text == sorted_z_to_a_list, "Items name sort Z to A is not correct"

    def test_check_by_price_low_to_high(self, driver, auth_positive):
        """Test: checking filter functionality (low to high)"""

        driver.find_element(*MainPage.DROPDOWN_PRODUCT_SORT_CONTAINER_BTN).click()
        driver.find_element(*MainPage.SORT_LOW_HIGH_DROPDOWN_ITEM).click()

        item_names = driver.find_elements(*MainPage.INVENTORY_ITEMS_PRICE)
        list_items_price_text = [float(item.text[1:]) for item in item_names]
        sorted_low_to_high_list = sorted(list_items_price_text)

        assert list_items_price_text == sorted_low_to_high_list, "Items price sort low to high is not correct"

    def test_check_by_price_high_to_low(self, driver, auth_positive):
        """Test: checking filter functionality (high to low)"""

        driver.find_element(*MainPage.DROPDOWN_PRODUCT_SORT_CONTAINER_BTN).click()
        driver.find_element(*MainPage.SORT_HIGH_LOW_DROPDOWN_ITEM).click()

        item_names = driver.find_elements(*MainPage.INVENTORY_ITEMS_PRICE)
        list_items_price_text = [float(item.text[1:]) for item in item_names]
        sorted_high_to_low_list = sorted(list_items_price_text, reverse=True)

        assert list_items_price_text == sorted_high_to_low_list, "Items price sort high to low is not correct"
