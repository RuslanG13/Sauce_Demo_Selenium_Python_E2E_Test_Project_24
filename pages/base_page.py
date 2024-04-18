class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = wait
