import allure
from allure_commons.types import AttachmentType
from pytest import fixture

from pages import AddCustomerPage, CustomersPage


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
        add_customer_page = AddCustomerPage(browser)
        add_customer_page.open_url()

    with allure.step('Open "Add Customer" form'):
        add_customer_page.go_to_form_page()

    with allure.step('Fill in "First Name" field'):
        add_customer_page.enter_first_name(form_data['first_name'])

    with allure.step('Fill in "Last Name" field'):
        add_customer_page.enter_last_name(form_data['last_name'])

    with allure.step('Fill in "Post Code" field'):
        add_customer_page.enter_post_code(form_data['post_code'])
        allure.attach(browser.get_screenshot_as_png(),
                      name="Add Customer page",
                      attachment_type=AttachmentType.PNG)

    with allure.step('Submit data'):
        add_customer_page.submit_data()

    with allure.step('Close information window'):
        browser.switch_to.alert.accept()

    with allure.step('Open "Customers" tab'):
        customers_page = CustomersPage(browser)
        customers_page.go_to_page()

    with allure.step('Find and check submitted data'):
        customers_page.search_customer(form_data['first_name'])
        allure.attach(browser.get_screenshot_as_png(),
                      name="Customers page",
                      attachment_type=AttachmentType.PNG)
        assert get_customer_data(browser, all_customers) == form_data

    with allure.step('Delete submitted data'):
        customers_page.delete_customer()


def get_customer_data(driver, get_all_customers: fixture) -> dict:
    """Returns customer data."""
    data = get_all_customers(driver).find('tr').find_all('td')
    return {'first_name': data[0].text,
            'last_name': data[1].text,
            'post_code': data[2].text}
