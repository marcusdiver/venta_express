from seleniumbase import BaseCase
from web_locators.locators import HomePageLocators


class LoginPage(BaseCase):

    def open_page(self):
        self.open(HomePageLocators.OPEN_APP)

    def click_popup_button(self):
        self.click(HomePageLocators.CLOSE_POPUP_BUTTON)

    def click_login_button(self):
        self.click(HomePageLocators.LOGIN_BUTTON)



