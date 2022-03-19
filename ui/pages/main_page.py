from ui.pages.base_page import BasePage
from ui.locators.main_page import MainPageLocators


class MainPage(BasePage):

    locators = MainPageLocators()

    def create_repo(self, name_repo):
        self.logger.info(f'Create repository with name: {name_repo}')
        self.click(self.locators.new_repo)
        self.find(self.locators.name_repo).send_keys(name_repo)
        """gitignore добавляется, чтобы сделать initial commit, 
        т.к. до первого коммита кнопка загрузки файла в ui не появится"""
        self.find(self.locators.gitignore_input).send_keys('Python')
        self.click(self.locators.gitignore_file)
        self.click(self.locators.create_repo)

    def upload_file(self, file_name, file_text):
        self.logger.info(f'Create commit with file')
        self.click(self.locators.new_file)
        self.find(self.locators.name_file).send_keys(file_name)
        self.find(self.locators.text_file).send_keys(file_text)
        self.click(self.locators.commit_changes)

    def delete_repo(self, name_repo):
        self.logger.info(f'Delete repository with name: {name_repo}')
        self.click(self.locators.settings)
        self.click(self.locators.delete_repo_button)
        self.find(self.locators.modal_window).find_element(self.locators.name_repo[0], f'.{self.locators.name_repo[1]}').send_keys(name_repo)
        self.click(self.locators.delete_button)


