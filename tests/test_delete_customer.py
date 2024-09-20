import allure
from allure_commons.types import AttachmentType
from pytest import fixture



@allure.feature("Banking Project")
@allure.story("UI")
@allure.title("Delete the first Customer with the name length closest to the average")
@allure.description(
    """
    Task: Test Customers delete function
    
    SetUp:
        Open browser
    
    Steps:
        1. Open "Banking Project" url
        2. Open "Customers" tab
        3. Find the first Customer with the name length closest to the average
        4. Delete found Customer
        5. Check that the Customer was deleted
        
    Expected result:
        - Customer with a name length close to average was deleted""")
def test_sort_customers(browser: fixture, all_customers: fixture):
    with allure.step('Open "Banking Project" url'):
        pass

    with allure.step('Open "Customers" tab'):
        pass

    with allure.step('Find the first Customer with the name length closest to the average'):
        pass

    with allure.step('Delete found Customer'):
        pass
    with allure.step('Check that the Customer was deleted'):
        pass


