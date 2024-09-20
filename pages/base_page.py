from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'

    def open_url(self) -> None:
        self.browser.get(self.url)

    def wait_to_be_clickable(self, input_locator: tuple[str, str]) -> WebElement:
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(input_locator))

    def wait_for_visibility(self, input_locator: tuple[str, str]) -> WebElement:
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(input_locator))
