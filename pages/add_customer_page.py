from locators import AddCustomerLocators
from . import BasePage


class AddCustomerPage(BasePage):
    def go_to_form_page(self) -> None:
        self.wait_to_be_clickable(AddCustomerLocators.tab).click()

    def enter_first_name(self, input_data: str) -> None:
        self.wait_to_be_clickable(AddCustomerLocators.first_name).send_keys(input_data)

    def enter_last_name(self, input_data: str) -> None:
        self.wait_to_be_clickable(AddCustomerLocators.last_name).send_keys(input_data)

    def enter_post_code(self, input_data: str) -> None:
        self.wait_to_be_clickable(AddCustomerLocators.post_code).send_keys(input_data)

    def submit_data(self) -> None:
        self.wait_to_be_clickable(AddCustomerLocators.submit_button).submit()
