from urllib.parse import urljoin

import requests
from requests.models import Response


HOST = 'http://127.0.0.1:8080'


class ServiceAPI:
    """Service API endpoints and HTTP methods."""
    def __init__(self):
        self.add_entity = urljoin(HOST, '/api/create')
        self.delete_entity = urljoin(HOST, '/api/delete/{id}')
        self.get_entity = urljoin(HOST, '/api/get/{id}')
        self.get_all_entities = urljoin(HOST, '/api/getAll')
        self.patch_entity = urljoin(HOST, '/api/patch/{id}')

    def get_all(self) -> Response:
        return requests.get(self.get_all_entities)

    def add(self, input_data: dict) -> Response:
        return requests.post(self.add_entity, json=input_data)

    def get(self, input_id: int | str) -> Response:
        return requests.get(self.get_entity.replace('{id}', str(input_id)))

    def delete(self, input_id: int | str) -> Response:
        return requests.delete(self.delete_entity.replace('{id}', str(input_id)))

    def patch(self, input_id: int | str, input_data: dict) -> Response:
        return requests.patch(self.patch_entity.replace('{id}', str(input_id)), json=input_data)
