import pytest
import requests
from requests.models import Response
from os import getcwd, chdir
from os import system as os_system
from os.path import join as os_path_join
from service_api import ServiceAPI
from urllib.parse import urljoin

pytest_plugins = 'tests.fixtures'


@pytest.fixture
def service_api():
    pass
    # base_dir = getcwd()
    # service_api_dir = os_path_join(getcwd(), 'test-service')
    # chdir(service_api_dir)
    # os_system('docker compose up --build -d')
    # chdir(base_dir)
    yield
    # chdir(service_api_dir)
    # os_system('docker compose down')


@pytest.fixture
def delete_data():
    def delete_test_data(input_id: int | str):
        requests.delete(urljoin('http://localhost:8080/api/delete/', str(input_id)))
    return delete_test_data

