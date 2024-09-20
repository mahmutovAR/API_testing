from selenium.webdriver.common.by import By


class CustomersLocators:
    tab = (By.XPATH, "//button[@ng-class='btnClass3']")
    table = (By.XPATH, "//table")
    first_name_button = (By.XPATH, "//a[contains(@ng-click, 'sortType')]")
    search = (By.XPATH, "//input[@ng-model='searchCustomer']")
    delete_button = (By.XPATH, "//button[@ng-click='deleteCust(cust)']")
