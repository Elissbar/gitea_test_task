from selenium.webdriver.common.by import By


class RegPageLocators:

    username = (By.XPATH, '//*[@id="user_name"]')
    email = (By.XPATH, '//*[@id="email"]')
    password = (By.XPATH, '//*[@id="password"]')
    retype = (By.XPATH, '//*[@id="retype"]')
    submit = (By.XPATH, '//div[@class="inline field"]/button')
