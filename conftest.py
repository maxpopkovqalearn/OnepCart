import pytest
import os

from selenium import webdriver


def driver_factory(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "yandex":
        driver = webdriver.Chrome()
    else:
        raise Exception("Driver not supported")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--url", action="store", default="http://127.0.0.1/opencart/", help="choose your browser")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    driver = driver_factory(browser)
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)
    driver.get(url)
    return driver
