from locators import CustomersLocators
from . import BasePage


class CustomersPage(BasePage):
    def go_to_page(self) -> None:
        self.wait_to_be_clickable(CustomersLocators.tab).click()

    def table_is_visible(self) -> None:
        self.wait_for_visibility(CustomersLocators.table)

    def search_customer(self, input_data: str) -> None:
        self.wait_to_be_clickable(CustomersLocators.search).send_keys(input_data)

    def sort_customers_by_first_name(self) -> None:
        self.wait_to_be_clickable(CustomersLocators.first_name_button).click()

    def delete_customer(self) -> None:
        self.wait_to_be_clickable(CustomersLocators.delete_button).click()
