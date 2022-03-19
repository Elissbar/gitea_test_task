import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import logging
import shutil
import requests
from time import time
from docker_client import *
import os


root_dir = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture(scope='session')
def config():
    url = 'http://localhost:3000/'
    return {'url': url, 'root_dir': root_dir}


def pytest_configure(config):
    timeout = 120
    start_time = time()
    run_docker_containers(root_dir)
    while time() - start_time < timeout:
        try:
            requests.get(url='http://localhost:3000/')
            break
        except:
            pass
    test_dir = os.path.join('tmp', 'tests')
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.makedirs(test_dir)
    if not os.path.exists(os.path.join(root_dir, 'gitea')):
        os.makedirs(os.path.join(root_dir, 'gitea'))
    setattr(config, 'test_dir', test_dir)


def pytest_unconfigure():
    stop_docker_containers()


@pytest.fixture(scope='function')
def driver(config):
    os.environ['WDM_LOG_LEVEL'] = '0'
    manager = ChromeDriverManager(version='latest')
    driver = webdriver.Chrome(executable_path=manager.install())
    driver.maximize_window()
    driver.get(config['url'])
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def test_dir(request, config):
    test_name = request._pyfuncitem.nodeid.replace(':', '_').replace('/', '_')
    dir_for_test = os.path.join(request.config.test_dir, test_name)
    os.makedirs(dir_for_test)
    return dir_for_test


@pytest.fixture(scope='function')
def logger(test_dir):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
    log_file = os.path.join(test_dir, 'test.log')
    log_level = logging.DEBUG

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

