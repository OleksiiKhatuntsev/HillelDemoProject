import allure

from facade.facade_base import FacadeBase

class LoginFacade(FacadeBase):
    def __init__(self):
        super().__init__()

    @allure.step("Fill email and password fields")
    def set_email_and_password(self, email, password):
        self._login_page.get_email_field().fill_field(email)
        self._login_page.get_password_field().fill_field(password)

    @allure.step("Fill email and password fields and click login button")
    def set_email_and_password_and_click_login_button(self, email, password):
        self._login_page.get_email_field().fill_field(email)
        self._login_page.get_password_field().fill_field(password)
        self.click_login_button()

    @allure.step("Click login button")
    def click_login_button(self):
        self._login_page.get_login_enabled_button().click()

    @allure.step("Open login form")
    def open_login_form(self):
        self._login_page.get_sign_in_button().click()

    def check_if_profile_displayed(self):
        return self._garage_page.get_my_profile_button().is_displayed()
