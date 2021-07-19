"""Base Page in Page Object pattern"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
import logging
import allure


class BasePage:
    _logger_name = None

    def __init__(self, browser):
        """Initialize web driver"""
        self.driver: WebDriver = browser
        self.logger = logging.getLogger(self._logger_name)

    def _click_to_element(self, locator):
        """Click to web element"""
        with allure.step(f'Поиск и клик по элементу {locator}'):
            try:
                self.driver.implicitly_wait(3)
                WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(locator))
            except NoSuchElementException:
                print('Element is not found')
                allure.attach(body=self.driver.get_screenshot_as_png(),
                              name="screenshot_image",
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError(e.msg)
            finally:
                self.driver.find_element(*locator).click()

    def _send_keys(self, value, locator):
        """Send keys to specified locator"""
        with allure.step(f'Заполнен текст {value} в {locator}'):
            element = self.driver.find_element(*locator)
            element.clear()
            element.send_keys(value)

    def _get_element_text(self, locator):
        """Get text from web element"""
        with allure.step(f'Получение текста из элемента {locator}'):
            return self.driver.find_element(locator).text

    def _wait_for_visible(self, locator, time_wait=3):
        """Waiting for visibility"""
        with allure.step(f'Ожидание появления элемента {locator} в течении {time_wait}'):
            return WebDriverWait(self.driver, time_wait).until(ec.visibility_of(self.driver.find_element(*locator)))
