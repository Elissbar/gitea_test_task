from ui.pages.reg_page import RegPage
from ui.pages.main_page import MainPage
from ui.pages.base_page import BasePage
from faker import Faker
import pytest


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger):
        self.driver = driver
        self.logger = logger
        self.faker = Faker()
        self.base_page = BasePage(self.driver)
        self.main_page = MainPage(self.driver)

    @pytest.fixture(scope='function')
    def registration_user(self):
        user = self.faker.profile()
        password = self.faker.bothify(text='?#?#??##??')
        main_page = BasePage(self.driver)
        main_page.click(main_page.locators.register)
        reg_page = RegPage(self.driver)
        reg_page.registration_user(user['username'], user['mail'], password)
