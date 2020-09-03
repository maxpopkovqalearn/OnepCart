import os
import pytest
from selenium import webdriver


# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="firefox",
#                      choices=["chrome", "firefox", "opera", "yandex"])
#     parser.addoption("--executor", action="store", default="localhost")

@pytest.fixture
def ff_browser(request):
    options = webdriver.FirefoxOptions()
    options.add_argument("start-maximized")
    wd = webdriver.Firefox(options=options)
    request.addfinalizer(wd.quit)
    return wd

@pytest.fixture
def remote(request):
    # browser = request.config.getoption("--browser")
    # executor = request.config.getoption("--executor")
    capabilities = {
        "browserName": "firefox",
        "version": "79.0",
        "enableVNC": True,
        "enableVideo": False
    }

    wd = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub",
                          desired_capabilities=capabilities)  # "platform": "linux"
    wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd

def test_download(ff_browser):
    ff_browser.get('https://developer.mozilla.org/ru/docs/Web/HTML/Element/Input/file')
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'selenium.png')
    ff_browser.switch_to.frame('frame_file-example')
    input_manager = ff_browser.find_element_by_css_selector('input[name="myFile"]')
    input_manager.send_keys(filename)

def test_download_grid(remote):
    remote.get('https://developer.mozilla.org/ru/docs/Web/HTML/Element/Input/file')
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'selenium.png')
    remote.switch_to.frame('frame_file-example')
    input_manager = remote.find_element_by_css_selector('input[name="myFile"]')
    input_manager.send_keys(filename)
