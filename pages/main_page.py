from pages.login_page import LoginPage


class MainPage(LoginPage):
    def __init__(self, driver, url):
        super().__init__(self, driver=driver, url=url)


