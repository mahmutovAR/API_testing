from random import randint
from urllib.parse import urljoin

import pytest
import requests
from service_api import Addition, Entity
from rstr import letters


@pytest.fixture
def test_data():
    add_info = Addition(additional_info=f'{letters(4, 8).title()} {letters(10)}',
                        additional_number=randint(1, 100))

    imp_num = [randint(1, 100)
               for _ in range(randint(1, 5))]

    return Entity(title=f'{letters(4, 8).title()} {letters(2, 6)}',
                  verified=bool(randint(0, 1)),
                  addition=add_info,
                  important_numbers=imp_num).model_dump()


@pytest.fixture
def entity_object():
    def return_entity(input_data: dict):
        return Entity.model_validate(input_data)
    return return_entity


@pytest.fixture
def delete_data():
    def delete_test_data(input_id: int | str):
        try:
            requests.delete(urljoin('http://localhost:8080/api/delete/', str(input_id)))
        except Exception as exc:
            exc.add_note('Test data deletion failed')
            raise
    return delete_test_data
