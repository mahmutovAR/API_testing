import allure
from pytest import fixture

from service_api import (StatusCodes, add_entity, get_all_entities,
                         get_entity, delete_entity, patch_entity)


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
        - new entity was added""")
def test_add_entity(service_api: fixture, test_data: fixture, delete_data: fixture):
    data = test_data
    with allure.step('Add entity'):
        add_response = add_entity(data)
        data_id = add_response.json()

    with allure.step('Check status code'):
        assert add_response.status_code == StatusCodes.create

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
        - entity was deleted by ID""")
def test_delete_entity(service_api: fixture, test_data: fixture):
    with allure.step('Add entity'):
        add_response = add_entity(test_data)
        data_id = add_response.json()

    with allure.step('Delete added entity'):
        delete_response = delete_entity(data_id)

    with allure.step('Check status code'):
        assert delete_response.status_code == StatusCodes.delete


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
        - entity was retrieved by ID""")
def test_get_entity(service_api: fixture, test_data: fixture,
                    entity_object: fixture, delete_data: fixture):
    data = test_data
    with allure.step('Add entity'):
        add_response = add_entity(data)
        data_id = add_response.json()

    with allure.step('Get entity by ID'):
        get_response = get_entity(data_id)

    with allure.step('Get status code'):
        assert get_response.status_code == StatusCodes.get

    with allure.step('Check data'):
        assert entity_object(get_response.json()) == entity_object(data)

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
        - all entities were retrieved""")
def test_get_all_entities(service_api: fixture, test_data: fixture, delete_data: fixture):
    data_id = list()
    with allure.step('Add several entities'):
        for _ in range(10):
            add_response = add_entity(test_data)
            data_id.append(add_response.json())

    with allure.step('Get all entities'):
        get_response = get_all_entities()

    with allure.step('Check status code'):
        assert get_response.status_code == StatusCodes.get_all

    for data_to_delete in data_id:
        delete_data(data_to_delete)


@allure.feature("Service API")
@allure.story("API")
@allure.title("Partially update an entity")
@allure.description(
    """
    Task: Entity deleting test

    Steps:
        1. Add entity
        2. Patch added entity
        3. Check status code
        4. Check data

    TearDown:
        - delete added entity

    Expected result:
        - the entity was deleted""")
def test_patch_entity(service_api: fixture, test_data: fixture,
                      entity_object: fixture, delete_data: fixture):
    ini_data = test_data
    with allure.step('Add entity'):
        add_response = add_entity(ini_data)
        data_id = add_response.json()

    with allure.step('Patch added entity'):
        new_data = test_data
        patch_response = patch_entity(data_id, new_data)

    with allure.step('Check status code'):
        assert patch_response.status_code == StatusCodes.patch

    with allure.step('Check data'):
        assert entity_object(get_entity(data_id).json()) == entity_object(new_data)

    delete_data(data_id)
