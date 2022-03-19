from ui.pages.base_page import BasePage
from ui.locators.reg_page import RegPageLocators


class RegPage(BasePage):

    locators = RegPageLocators()

    def registration_user(self, username, email, password):
        self.logger.info(f'Registration new user with credentials: {username, email, password}')
        self.find(self.locators.username).send_keys(username)
        self.find(self.locators.email).send_keys(email)
        self.find(self.locators.password).send_keys(password)
        self.find(self.locators.retype).send_keys(password)
        self.click(self.locators.submit)
