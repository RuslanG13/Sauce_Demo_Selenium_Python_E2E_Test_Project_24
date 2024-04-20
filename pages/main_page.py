from pages.base_page import BasePage

from locators.main_locators import MainPageLocators


class MainPage(BasePage):
    main_page_locators = MainPageLocators()

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @property
    def products_title(self):
        return self.element_is_visible(self.main_page_locators.PRODUCTS_TITLE)
