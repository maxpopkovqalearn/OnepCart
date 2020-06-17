"""Fixtures for start different browsers"""
import pytest

from selenium import webdriver


def driver_factory(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Driver not supported")
    return driver


def pytest_addoption(parser):
    """Parser for command line parameters"""
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--url", action="store", default="http://127.0.0.1/opencart/", help="Сhoose your browser")


@pytest.fixture
def browser(request):
    """Initializing and open browser"""
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    driver = driver_factory(browser)
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)
    driver.get(url)
    return driver
