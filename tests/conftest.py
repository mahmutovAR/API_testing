import pytest
from selenium import webdriver

pytest_plugins = 'tests.fixtures'


@pytest.fixture
def browser():
    pass
    # web_driver = webdriver.Chrome()
    # web_driver.maximize_window()
    # yield web_driver
    # web_driver.quit()
