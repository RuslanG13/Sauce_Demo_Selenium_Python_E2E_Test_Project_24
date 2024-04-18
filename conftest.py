import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import urls, login_credentials, page_elements_data
from data.utils import rand_index

from locators.login_locators import LoginPageLocators as LPL
from locators.locators_saucedemo import InventoryPageLocators as IPL
from locators.locators_saucedemo import ItemCardDetailLocators as ICD
from locators.locators_saucedemo import CartPageLocators as CPL


@pytest.fixture()
def driver():
    """Chrome webdriver initialization"""

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def auth_positive(driver):
    """Fixture: Positive authentication on the https://www.saucedemo.com"""

    driver.get(urls.BASE_URL)

    driver.find_element(*LPL.USERNAME_FIELD_LOCATOR).send_keys(input_data.username_valid)
    driver.find_element(*LPL.PASSWORD_FIELD_LOCATOR).send_keys(input_data.password_valid)

    driver.find_element(*LPL.LOGIN_BUTTON_LOCATOR).click()


@pytest.fixture()
def add_item_to_cart_through_catalog(driver, auth_positive):
    """Fixture: add item to cart through catalog"""

    list_catalog_items = driver.find_elements(*IPL.INVENTORY_ITEMS)
    list_add_to_cart_btn = driver.find_elements(*IPL.ADD_TO_CART_BUTTON)

    selected_item_idx = rand_index(len(list_catalog_items))
    selected_item_name = list_catalog_items[selected_item_idx].text.split("\n")[0]

    list_add_to_cart_btn[selected_item_idx].click()
    numbers_of_items_in_shop_cart = int(driver.find_element(*IPL.SHOPPING_CART_BADGE).text)

    assert selected_item_name in page_elements_data.catalog_items_names, \
        "The selected item not present in catalog"
    assert numbers_of_items_in_shop_cart == page_elements_data.count_items_in_cart[0], \
        f"The number in shopping cart badge is different than {page_elements_data.count_items_in_cart[0]}"


@pytest.fixture()
def add_item_to_cart_through_item_card(driver, auth_positive):
    """Fixture: add item to cart through item card"""

    list_catalog_items = driver.find_elements(*IPL.INVENTORY_ITEMS)
    list_items_card_link = driver.find_elements(*IPL.INVENTORY_ITEMS_CARD_LINK_IMAGE)
    selected_item_idx = rand_index(len(list_catalog_items))
    selected_item_name_catalog = list_catalog_items[selected_item_idx].text.split("\n")[0]

    list_items_card_link[selected_item_idx].click()

    selected_item_name_product_card = driver.find_element(*ICD.ITEM_NAME).text.split("\n")[0]

    assert selected_item_name_product_card == selected_item_name_catalog, \
        "Item at the item's card details and catalog are different"

    driver.find_element(*ICD.ADD_TO_CART_BUTTON).click()

    numbers_of_items_in_shop_cart_in_badge = int(driver.find_element(*IPL.SHOPPING_CART_BADGE).text)

    assert numbers_of_items_in_shop_cart_in_badge == page_elements_data.count_items_in_cart[0], \
        f"The number in shopping cart badge is different than {page_elements_data.count_items_in_cart[0]}"


@pytest.fixture()
def check_exist_item_in_cart(driver, auth_positive):
    """Fixture: check the added item in shopping cart"""

    driver.find_element(*IPL.SHOPPING_CART_BADGE).click()

    amount_items_in_cart = len(driver.find_elements(*CPL.CART_ITEMS))

    assert amount_items_in_cart == page_elements_data.count_items_in_cart[0], \
        f"The amount is different than {page_elements_data.count_items_in_cart[0]} or cart is empty"
