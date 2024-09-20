import pytest
import rstr
from bs4 import BeautifulSoup
from selenium import webdriver


@pytest.fixture
def form_data():
    post_code = rstr.digits(10)
    last_name = rstr.letters(6, 12)
    first_name = ''
    for index in range(0, 9, 2):
        num = int(post_code[index: index + 2])
        while num > 25:
            num -= 26
        first_name += chr(num + 97)

    return {'first_name': first_name,
            'last_name': last_name,
            'post_code': post_code}


@pytest.fixture
def all_customers():
    def get_data(web_driver: webdriver):
        html = web_driver.page_source
        soup_object = BeautifulSoup(html, "lxml")
        return soup_object.find('table', class_='table').tbody
    return get_data
