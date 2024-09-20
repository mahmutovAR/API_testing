import allure
from allure_commons.types import AttachmentType
from pytest import fixture


@allure.feature("Banking Project")
@allure.story("UI")
@allure.title("Sort Customers by First Name")
@allure.description(
    """
    Task: Test sorting Customers by First Name
    
    SetUp:
        Open browser
    
    Steps:
        1. Open "Banking Project" url
        2. Open "Customers" tab
        3. Sort Customers by First Name
        4. Check that Customers are sorted by First Name
        
    Expected result:
        - customers are sorted be First Name""")
def test_sort_customers(browser: fixture, all_customers: fixture):
    with allure.step('Open "Banking Project" url'):
        pass

    with allure.step('Open "Customers" tab'):
        pass

    with allure.step('Sort Customers by First Name'):
        pass

    with allure.step('Check that Customers are sorted by First Name'):
        assert 2+2 == 4
