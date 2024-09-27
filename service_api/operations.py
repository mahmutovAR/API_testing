import requests
from requests.models import Response

from . import ServiceAPI


def get_all_entities() -> Response:
    return requests.get(ServiceAPI.get_all_entities)


def add_entity(input_data: dict) -> Response:
    return requests.post(ServiceAPI.add_entity, json=input_data)


def get_entity(input_id: int | str) -> Response:
    return requests.get(ServiceAPI.get_entity.replace('{id}', str(input_id)))


def delete_entity(input_id: int | str) -> Response:
    return requests.delete(ServiceAPI.delete_entity.replace('{id}', str(input_id)))


def patch_entity(input_id: int | str, input_data: dict) -> Response:
    return requests.patch(ServiceAPI.patch_entity.replace('{id}', str(input_id)), json=input_data)
