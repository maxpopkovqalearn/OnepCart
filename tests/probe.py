import os
import pytest
from selenium import webdriver


@pytest.fixture
def ff_browser(request):
    options = webdriver.FirefoxOptions()
    options.add_argument("start-maximized")
    wd = webdriver.Firefox(options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_download(ff_browser):
    ff_browser.get('https://developer.mozilla.org/ru/docs/Web/HTML/Element/Input/file')
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'selenium.png')
    ff_browser.switch_to.frame('frame_file-example')
    input_manager = ff_browser.find_element_by_css_selector('input[name="myFile"]')
    input_manager.send_keys(filename)
