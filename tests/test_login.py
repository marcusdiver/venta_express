from seleniumbase import BaseCase
from pages.login_page import LoginPage
from web_locators.locators import HomePageLocators


class LoginTest(BaseCase):

    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")
        LoginPage.open_page(self)

    def test_login_with_valid_credential(self):
        # user clicks on popup button
        LoginPage.click_popup_button(self)

        # user clicks on login button
        LoginPage.click_login_button(self)
        self.wait(3)
        # user enters correct email
        LoginPage.enter_correctly_email_address(self, HomePageLocators.EMAIL_CREDENTIAL)
        self.wait(3)
        # user enters correct password
        LoginPage.enter_correctly_password(self, HomePageLocators.PASS_CREDENTIAL)

    def tearDown(self):
        # self.driver.quit()
        super().tearDown()
        print("RUNNING AFTER EACH TEST")
