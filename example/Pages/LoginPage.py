from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import os
import json


class LoginPage(BasePage):
    os.chdir(os.path.dirname(__file__))
    user_path = os.path.abspath('users.json')
    print(user_path)

    with open(user_path) as user_file:
        json_data = json.load(user_file)

    user_name = json_data['login']
    user_password = json_data['password']

    name = user_name
    password = user_password
    TEXT_PAGE = (By.XPATH, "//*[text()='Test sign in']")
    LOGIN = (By.NAME, "login")
    PASSWORD = (By.NAME, "password")
    SIGN_IN = (By.CSS_SELECTOR, "input[value='Войти']")

    def sign_in(self):
        """Authentication"""
        self._wait_for_visible(self.TEXT_PAGE)
        self._send_keys(self.name, self.LOGIN)
        self._send_keys(self.password, self.PASSWORD)
        self._click_to_element(self.SIGN_IN)
