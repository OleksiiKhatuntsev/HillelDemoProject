from pages.garage_page import GaragePage
from pages.login_page import LoginPage


class FacadeBase:
    def __init__(self):
        self._login_page = LoginPage()
        self._garage_page = GaragePage()