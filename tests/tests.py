from base import BaseCase
from bs4 import BeautifulSoup
import requests
import re


def check_page(url):
    pattern = re.compile(r'\s*\w+\s?\w+\s?\w+')
    page = requests.get(url).content
    soup = BeautifulSoup(page, 'html.parser')
    headers = soup.find_all(['h1', 'h2', 'p'], string=pattern)
    elements = [elem for elem in soup.find_all(True) if elem.has_attr('class') or elem.has_attr('id')]
    assert len(elements) > 3, 'Кол-во css-селекторов меньше 3'
    assert len(headers) > 0, 'Отсутствует эталонный текст на странице'


class TestCase(BaseCase):

    def test_scenario(self, registration_user, config):
        self.logger.info('Check selectors and text on page')
        check_page(url=config['url'])
        repo_name = self.faker.bothify(text='??????')
        self.main_page.create_repo(name_repo=repo_name)
        file_name = self.faker.bothify(text='????##?##??')
        file_text = self.faker.bothify(text='?#?#??##??????######')
        self.main_page.upload_file(file_name=file_name, file_text=file_text)
        self.main_page.click(self.main_page.locators.raw_button)
        assert file_text in self.driver.page_source
        self.driver.back()
        self.main_page.delete_repo(repo_name)
