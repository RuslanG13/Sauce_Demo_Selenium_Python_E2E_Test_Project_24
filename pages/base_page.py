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

    def get_element_text(self, locator):
        return self.element_is_visible(locator).text

    @staticmethod
    def element_is_displayed(element):
        return element.is_displayed()
