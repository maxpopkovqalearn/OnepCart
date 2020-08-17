"""Selectors for different elements in the Opencart Admin Login page """
from selenium.webdriver.common.by import By
from PageObj.BasePage import BasePage

class AdminLoginPage(BasePage):

    name="admin"
    password="admin"
    LOGIN=(By.ID, "input-username")
    PASSWORD=(By.ID, "input-password")
    LOG_ENTER=(By.XPATH, '//*[text()="Login"]')
    CATALOG=(By.XPATH, '//*[text()="Catalog"]')




