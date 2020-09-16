"""Fixtures for start different browsers"""
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from PageObj.AdminPage import AdminLoginPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.events import EventFiringWebDriver
import logging
from helpers.log_listener import Listener
import sys


def pytest_addoption(parser):
    """Parser for command line parameters"""
    parser.addoption('--url',
                     action='store',
                     default='http://127.0.0.1/opencart/admin/',
                     help='Main link for Opencart')
    parser.addoption('--browser_name',
                     action='store',
                     default='firefox',
                     help='Choose browser: ie, firefox, chrome')
    parser.addoption('--timeout',
                     action='store',
                     default=40,
                     help='Timeout for wait WebDriver')
    parser.addoption('--file',
                     action='store',
                     default=None,
                     help='Filename with log report')


@pytest.fixture()
def my_logger(request):
    """Custom logger"""
    filename = request.config.getoption('--file')
    logging.basicConfig(level=logging.INFO, filename=filename)
    logger = logging.getLogger('Web Driver')
    if filename == None:
        stdout_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stdout_handler)
    else:
        file_handler = logging.FileHandler(filename)
        logger.addHandler(file_handler)

    return logger


@pytest.fixture()
def browser(request, my_logger):
    """Initializing and open browser"""
    browser = request.config.getoption("--browser_name")
    if browser == 'chrome':
        my_logger.info('\nStart Chrome browser for test...')
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        options.add_argument('--ignore-certificate-errors')
        browser = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        my_logger.info('\nStart Firefox browser for test...')
        options = webdriver.FirefoxOptions()
        # options.add_argument("-headless")
        browser = EventFiringWebDriver(webdriver.Firefox(options=options), Listener())
    yield browser
    my_logger.info('\nClose browser...')
    browser.quit()


@pytest.fixture()
def get_url(request, browser):
    """Fixture for get link from parameter"""
    url = request.config.getoption("--url")
    timeout = request.config.getoption('--timeout')
    open_link = browser.get(url)
    browser.implicitly_wait(timeout)
    return open_link


@pytest.fixture()
def open_admin(browser):
    """Fixture for login to Admin panel"""
    username_input = browser.find_element(*AdminLoginPage.LOGIN)
    username_input.send_keys(AdminLoginPage.name)
    password_input = browser.find_element(*AdminLoginPage.PASSWORD)
    password_input.send_keys(AdminLoginPage.password)
    browser.find_element(By.XPATH, '//*[text()="Login"]').click()


def wait_for_element(browser, locator):
    """Custom waitter different web elements"""
    try:
        WebDriverWait(browser, 5).until(ec.presence_of_element_located(locator))
        browser.implicitly_wait(5)
    except NoSuchElementException:
        print('Web element not found!')
    browser.find_element(*locator)
