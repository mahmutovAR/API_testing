import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

pytest_plugins = 'tests.fixtures'


@pytest.fixture
def browser():
    # option = webdriver.ChromeOptions()
    # option.add_argument("start-maximized")
    # web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()
