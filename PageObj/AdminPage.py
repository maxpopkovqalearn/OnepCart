"""Selectors for different elements in the Opencart Admin Login page """
from selenium.webdriver.common.by import By
from PageObj.BasePage import BasePage

class AdminLoginPage(BasePage):

    LOGIN=(By.ID, "input-username")
    PASSWORD=(By.ID, "input-password")
    LOG_ENTER=(By.XPATH, '//*[text()="Login"]')
    CATALOG=(By.XPATH, '//*[text()="Catalog"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base_url = "http://127.0.0.1/opencart/admin/"

    def _login(self, name, password):
        self._send_keys(name, self.LOGIN)
        self._send_keys(password, self.PASSWORD)
        self._click_to_element(self.LOG_ENTER)



