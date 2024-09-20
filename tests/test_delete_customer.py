import allure
from allure_commons.types import AttachmentType
from pytest import fixture

from pages import CustomersPage


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
        customers_page = CustomersPage(browser)
        customers_page.open_url()

    with allure.step('Open "Customers" tab'):
        customers_page = CustomersPage(browser)
        customers_page.go_to_page()
        customers_page.table_is_visible()
        allure.attach(browser.get_screenshot_as_png(),
                      name="Customers page",
                      attachment_type=AttachmentType.PNG)

    with allure.step('Find the first Customer with the name length closest to the average'):
        customer_to_delete = determine_customer_to_delete(browser, all_customers)
        customers_page.search_customer(customer_to_delete)
        allure.attach(browser.get_screenshot_as_png(),
                      name="Customer to delete",
                      attachment_type=AttachmentType.PNG)

    with allure.step('Delete found Customer'):
        customers_page.delete_customer()

    with allure.step('Check that the Customer was deleted'):
        allure.attach(browser.get_screenshot_as_png(),
                      name="Customer was deleted",
                      attachment_type=AttachmentType.PNG)


def determine_customer_to_delete(driver, get_all_customers: fixture) -> str:
    """Returns the first Customer with the name length closest to average."""
    all_names = [row.find_all('td')[0].text
                 for row in get_all_customers(driver).find_all('tr')]
    sum_ = 0
    for name in all_names:
        sum_ += len(name)
    average = sum_ / len(all_names)

    name_to_delete = all_names[-1]
    for name in reversed(all_names):
        if abs(average - len(name)) <= abs(average - len(name_to_delete)):
            name_to_delete = name
    return name_to_delete


