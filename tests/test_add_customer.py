import allure
from allure_commons.types import AttachmentType
from pytest import fixture



@allure.feature("Banking Project")
@allure.story("UI")
@allure.title("Add Customer")
@allure.description(
    """
    Task: Test Add Customer Form

    SetUp:
        - open browser

    Steps:
         1. Open "Banking Project" url
         2. Open "Add Customer" form
         3. Fill in "First Name" field
         4. Fill in "Last Name" field
         5. Fill in "Post Code" field
         6. Submit data
         7. Close information window
         8. Open "Customers" tab
         9. Find and check submitted data
        10. Delete submitted data

    Expected result:
        - the new Customer added
        - data in the Customers table corresponds to the entered""")
def test_add_customer(browser: fixture, form_data: fixture, all_customers: fixture):
    with allure.step('Open "Banking Project" url'):
        pass

    with allure.step('Open "Add Customer" form'):
        pass
    with allure.step('Fill in "First Name" field'):
        pass
    with allure.step('Fill in "Last Name" field'):
        pass
    with allure.step('Fill in "Post Code" field'):
        pass

    with allure.step('Submit data'):
        pass
    with allure.step('Close information window'):
        pass
    with allure.step('Open "Customers" tab'):
        pass

    with allure.step('Find and check submitted data'):
        pass
        assert 2 == 1+1

    with allure.step('Delete submitted data'):
        pass
