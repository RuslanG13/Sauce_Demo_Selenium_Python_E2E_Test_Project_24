from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

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

    @staticmethod
    def element_is_displayed(web_element):
        return web_element.is_displayed()

    @staticmethod
    def get_element_text(web_element):
        return web_element.text
