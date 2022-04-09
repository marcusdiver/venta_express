from seleniumbase import BaseCase
from pages.login_page import LoginPage
from web_locators.locators import HomePageLocators


class LoginTest(BaseCase):

    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")
        LoginPage.open_page(self)

    def test_login_with_valid_credential(self):
        # make sure title is available
        .click_popup_button(self)

    def tearDown(self):
        # self.driver.quit()
        super().tearDown()
        print("RUNNING AFTER EACH TEST")
