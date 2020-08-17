"""Fixtures for start different browsers"""
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from PageObj.AdminPage import AdminLoginPage
from selenium.webdriver.common.by import By

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
def browser(request):
    """Initializing and open browser"""
    browser = request.config.getoption("--browser_name")
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument('--ignore-certificate-errors')
        browser = webdriver.Chrome(desired_capabilities=d, options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        browser = webdriver.Firefox(options=options)
    yield browser
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
