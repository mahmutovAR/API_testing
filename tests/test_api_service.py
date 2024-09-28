from http import HTTPStatus

import allure
from pytest import fixture
from service_api import ServiceAPI


API = ServiceAPI()


@allure.feature("Service API")
@allure.story("API")
@allure.title("Create a new entity")
@allure.description(
    """
    Task: Entity addition test

    Steps:
        1. Add entity
        2. Check status code
        
    TearDown:
        - delete added entity

    Expected result:
        - new entity added""")
def test_add_entity(test_data: fixture, delete_data: fixture):
    try:
        with allure.step('Add entity'):
            add_response = API.add(test_data)
            data_id = add_response.json()

        with allure.step('Check status code'):
            assert add_response.status_code == HTTPStatus.OK, (f'Entity not added\n'
                                                               f'{add_response.request.body}')
    except Exception:
        raise
    finally:
        delete_data(data_id)


@allure.feature("Service API")
@allure.story("API")
@allure.title("Delete entity")
@allure.description(
    """
    Task: Entity deletion test

    Steps:
        1. Add entity
        2. Delete added entity
        3. Check status code

    Expected result:
        - entity deleted by ID""")
def test_delete_entity(test_data: fixture):
    try:
        with allure.step('Add entity'):
            add_response = API.add(test_data)
            data_id = add_response.json()

        with allure.step('Delete added entity'):
            delete_response = API.delete(data_id)

        with allure.step('Check status code'):
            assert delete_response.status_code == HTTPStatus.NO_CONTENT, (f'Entity not deleted'
                                                                          f'\n{add_response.request.body}')
    except Exception:
        raise


@allure.feature("Service API")
@allure.story("API")
@allure.title("Get a single entity")
@allure.description(
    """
    Task: Entity retrieval test

    Steps:
        1. Add entity
        2. Get entity by ID
        3. Check status code
        4. Check data

    TearDown:
        - delete added entity

    Expected result:
        - entity retrieved by ID""")
def test_get_entity(test_data: fixture, entity_object: fixture, delete_data: fixture):
    try:
        data = test_data
        with allure.step('Add entity'):
            add_response = API.add(data)
            data_id = add_response.json()

        with allure.step('Get entity by ID'):
            get_response = API.get(data_id)

        with allure.step('Get status code'):
            assert get_response.status_code == HTTPStatus.OK, (f'Entity not retrieved by ID'
                                                               f'\n{add_response.request.body}')

        with allure.step('Check data'):
            assert entity_object(get_response.json()) == entity_object(data), (f'Entity data does not match'
                                                                               f'\n{add_response.request.body}')
    except Exception:
        raise
    finally:
        delete_data(data_id)


@allure.feature("Service API")
@allure.story("API")
@allure.title("Get a list of entities")
@allure.description(
    """
    Task: All entities retrieving test

    Steps:
        1. Add several entities
        2. Get all entities
        3. Check status code

    TearDown:
        - delete added entities

    Expected result:
        - all entities retrieved""")
def test_get_all_entities(test_data: fixture, delete_data: fixture):
    data_id = list()
    try:
        with allure.step('Add several entities'):
            for _ in range(10):
                add_response = API.add(test_data)
                data_id.append(add_response.json())

        with allure.step('Get all entities'):
            get_response = API.get_all()

        with allure.step('Check status code'):
            assert get_response.status_code == HTTPStatus.OK, (f'All entities not retrieved'
                                                               f'\n{add_response.request.body}')
    except Exception:
        raise
    finally:
        for data_to_delete in data_id:
            delete_data(data_to_delete)


@allure.feature("Service API")
@allure.story("API")
@allure.title("Patch an entity")
@allure.description(
    """
    Task: Entity patch test

    Steps:
        1. Add entity
        2. Patch added entity
        3. Check status code
        4. Check data

    TearDown:
        - delete added entity

    Expected result:
        - the entity patched""")
def test_patch_entity(test_data: fixture, entity_object: fixture, delete_data: fixture):
    try:
        with allure.step('Add entity'):
            add_response = API.add(test_data)
            data_id = add_response.json()

        with allure.step('Patch added entity'):
            new_data = test_data
            patch_response = API.patch(data_id, new_data)

        with allure.step('Check status code'):
            assert patch_response.status_code == HTTPStatus.NO_CONTENT, (f'Entity not patched\n'
                                                                         f'{add_response.request.body}')

        with allure.step('Check data'):
            assert entity_object(API.get(data_id).json()) == entity_object(new_data), (f'Entity data does not match\n'
                                                                                       f'{add_response.request.body}')
    except Exception:
        raise
    finally:
        delete_data(data_id)
