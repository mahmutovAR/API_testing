from random import randint

import pytest
from pydantic import BaseModel
from rstr import letters


class Addition(BaseModel):
    additional_info: str
    additional_number: int


class Entity(BaseModel):
    title: str
    verified: bool
    addition: Addition
    important_numbers: list[int]


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
