"""Selectors for different elements in the Opencart main page """
from selenium.webdriver.common.by import By
from PageObj.BasePage import BasePage


class MainPage(BasePage):
    WISH_LIST = (By.XPATH, '//*[text()="Wish List"]')
    PRODUCT_HEADER = (By.XPATH, '//h3[text()="Featured"]')
    ADD_TO_CARD_BUTTON = (By.XPATH, '//span[text()="Add to Cart"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def add_to_card_button(self):
        self.driver.find_element(self.ADD_TO_CARD_BUTTON).is_enabled()
