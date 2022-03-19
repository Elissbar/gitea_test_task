from selenium.webdriver.common.by import By


class BasePageLocators:
    register = (By.XPATH, '//a[@href="/user/sign_up"]')
    login = (By.XPATH, "//a[contains(@href, '/user/login')]")
