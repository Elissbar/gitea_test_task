from selenium.webdriver.common.by import By


class MainPageLocators:

    # Локаторы для создания архива
    new_repo = (By.XPATH, '//a[@data-content="New Repository"]')
    name_repo = (By.XPATH, '//*[@id="repo_name"]')
    gitignore_input = (By.XPATH, '//div[contains(@class, "multiple")]/input[@class="search"]')
    gitignore_file = (By.XPATH, '//div[@data-value="Python"]')
    create_repo = (By.XPATH, '//*[@class="ui green button"]')

    # Локаторы для создания файла
    new_file = (By.XPATH, '//a[contains(@href, "/_new/master/")]')
    name_file = (By.XPATH, '//*[@id="file-name"]')
    text_file = (By.XPATH, '//textarea[@data-mprt="6"]')
    commit_changes = (By.XPATH, '//button[@id="commit-button"]')
    raw_button = (By.XPATH, '//a[contains(@href, "/raw/") and not(@download)]')

    # Локаторы для удаления архива
    settings = (By.XPATH, '//a[contains(@href, "/settings") and not(@id)]')
    delete_repo_button = (By.XPATH, '//*[@data-modal="#delete-repo-modal"]')
    modal_window = (By.XPATH, '//div[@id="delete-repo-modal" and contains(@class, "visible")]')
    delete_button = (By.XPATH, "//button[contains(text(), 'Delete Repository')]")
