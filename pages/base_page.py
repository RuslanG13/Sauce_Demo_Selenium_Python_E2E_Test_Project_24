from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open_page(self, url):
        return self.driver.get(self.url)

    def element_is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def element_is_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def element_is_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element(locator))

    def element_is_displayed(self, element):
        return self.element.is_displayed()

    def get_element_text(self, locator):
        return self.element_is_visible(locator).text
