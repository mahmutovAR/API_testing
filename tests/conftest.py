import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


pytest_plugins = 'tests.fixtures'


@pytest.fixture
def browser():
    # web_driver = webdriver.Chrome()
    options = Options()
    options.add_argument('--headless')
    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()
