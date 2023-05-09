import allure

from models.register_post_model import RegisterPostModel
import requests
from driver import Driver
from pages.login_page import LoginPage
from pages.garage_page import GaragePage
from facade.login_facade import LoginFacade
import time

from test_base import TestBase


class TestAuthentication(TestBase):
    def setup_class(self):
        self.init_elements(self)
        self.driver = Driver.get_chrome_driver()
        self.login_page = LoginPage()
        self.garage_page = GaragePage()
        self.session = requests.session()
        register_user = RegisterPostModel("Jon", "Snow", "tes3t5132334ts@rs.fd", "Qwerty123", "Qwerty123")
        self.session.post("https://qauto2.forstudy.space/api/auth/signup", json=register_user.__dict__)

    def setup_method(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    def test_check_login_window(self):
        self.login_page.get_sign_in_button().click()
        assert self.login_page.get_email_field().is_displayed()

    def test_check_incorrect_email(self):
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("asd123")
        self.login_page.get_remember_me_button().click()
        assert self.login_page.get_login_incorrect_alert().is_displayed()

    def test_check_successful_login(self):
        self.login_facade.open_login_form()
        self.login_facade.set_email_and_password_and_click_login_button("test1234ts@rs.fd", "Qwerty123")
        assert self.login_facade.check_if_profile_displayed()

    @allure.step("Fill email and password fields")
    def set_email_and_password(self, email, password):
        self.login_page.get_email_field().fill_field(email)
        self.login_page.get_password_field().fill_field(password)

    def test_check_login_with_removed_user(self):
        new_user = RegisterPostModel("Jon", "Snow", "teasds3t5132334ts@rs.fd", "Qwerty123", "Qwerty123")
        self.session.post("https://qauto2.forstudy.space/api/auth/signup", json=new_user.__dict__)
        self.session.delete("https://qauto2.forstudy.space/api/users")
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("teasds3t5132334ts@rs.fd")
        self.login_page.get_password_field().fill_field("Qwerty123")
        self.login_page.get_login_enabled_button().click()
        self.login_page.get_wrong_user_alert().is_displayed()

    def teardown_method(self):
        screen_name_using_current_time = time.strftime("%Y%m%d-%H%M%S")
        allure.attach(self.driver.get_screenshot_as_png(), name=screen_name_using_current_time)


    def teardown_class(self):
        self.session.delete("https://qauto2.forstudy.space/api/users")



# a = requests.post("auth_link")
# Headers = { "Bearer_token" : "our_unique_secret_token" }
#
# response = request.post("https://example.com/get-my-account-detail", headers=Headers)