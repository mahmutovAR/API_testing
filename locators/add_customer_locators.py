from selenium.webdriver.common.by import By


class AddCustomerLocators:
    tab = (By.XPATH, "//button[@ng-class='btnClass1']")
    first_name = (By.XPATH, "//input[@ng-model='fName']")
    last_name = (By.XPATH, "//input[@ng-model='lName']")
    post_code = (By.XPATH, "//input[@ng-model='postCd']")
    submit_button = (By.XPATH, "//button[@type='submit']")
