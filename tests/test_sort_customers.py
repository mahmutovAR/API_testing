import allure
from allure_commons.types import AttachmentType
from pytest import fixture

from pages import CustomersPage


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
        customers_page = CustomersPage(browser)
        customers_page.open_url()

    with allure.step('Open "Customers" tab'):
        customers_page = CustomersPage(browser)
        customers_page.go_to_page()
        customers_page.table_is_visible()
        allure.attach(browser.get_screenshot_as_png(),
                      name="Customers page",
                      attachment_type=AttachmentType.PNG)

    with allure.step('Sort Customers by First Name'):
        customers_page.sort_customers_by_first_name()
        if not customers_are_sorted(browser, all_customers):
            allure.attach(browser.get_screenshot_as_png(),
                          name="Customers are sorted in reverse order",
                          attachment_type=AttachmentType.PNG)
            customers_page.sort_customers_by_first_name()

    with allure.step('Check that Customers are sorted by First Name'):
        assert customers_are_sorted(browser, all_customers)
        allure.attach(browser.get_screenshot_as_png(),
                      name="Customers are sorted",
                      attachment_type=AttachmentType.PNG)


def customers_are_sorted(driver, get_all_customers: fixture) -> bool:
    """Returns customer data from Customers list."""
    all_customers = get_all_customers(driver).find_all('tr')
    customer_1 = all_customers[0].find_all('td')
    customer_2 = all_customers[1].find_all('td')

    customer_1_data = f'{customer_1[0].text}{customer_1[1].text}{customer_1[2].text}'
    customer_2_data = f'{customer_2[0].text}{customer_2[1].text}{customer_2[2].text}'

    if customer_1_data < customer_2_data:
        return True
    return False
