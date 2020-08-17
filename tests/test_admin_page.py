from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_element_admin_login_page(browser):
    """Tests for admin login page"""
    browser.find_element_by_class_name('input-group-addon')
    browser.find_element_by_xpath('//*[text()="Forgotten Password"]')
    browser.find_element_by_id('input-password')
    browser.find_element_by_name('username')


def test_wait_admin_login_page(browser):
    """Test for admin login page with wait"""
    username = 'admin'
    password = 'admin'
    browser.find_element_by_id('input-username').send_keys(username)
    browser.find_element_by_id('input-password').send_keys(password)
    browser.find_element_by_xpath('//*[text()="Login"]').click()
    element = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'menu-dashboard')))
    assert element.text == "Dashboard"


def test_wait_admin_login_page_logout(browser):
    """Test for logout admin login page with wait"""
    username = 'admin'
    password = 'admin'
    browser.find_element_by_id('input-username').send_keys(username)
    browser.find_element_by_id('input-password').send_keys(password)
    browser.find_element_by_xpath('//*[text()="Login"]').click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Logout"]'))).click()
    element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[text()="Forgotten Password"]')))
    assert element.text == "Forgotten Password"


def test_wait_admin_login_page_catalog(browser, get_url):
    """Test for admin login page catalog with wait"""
    username = 'admin'
    password = 'admin'
    browser.find_element_by_id('input-username').send_keys(username)
    browser.find_element_by_id('input-password').send_keys(password)
    browser.find_element_by_xpath('//*[text()="Login"]').click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Catalog"]'))).click()
    browser.find_element_by_xpath('//*[text()="Products"]').click()
    element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[text()="Canon EOS 5D"]')))
    assert element.text == "Canon EOS 5D"


def test_for_product(browser):
    username = 'admin'
    password = 'admin'
    browser.find_element_by_id('input-username').send_keys(username)
    browser.find_element_by_id('input-password').send_keys(password)
    browser.find_element_by_xpath('//*[text()="Login"]').click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Catalog"]'))).click()
    browser.find_element_by_xpath('//*[text()="Products"]').click()
    browser.find_element_by_css_selector('a[data-original-title="Add New"]').click()
    browser.find_element_by_css_selector('input[id="input-name1"]').send_keys('product1')
    browser.find_element_by_css_selector('input[id="input-meta-title1"]').send_keys('meta-product1')
    browser.find_element_by_css_selector('a[href="#tab-data"]').click()
    browser.find_element_by_css_selector('input[id="input-model"]').send_keys('model-product1')
    browser.find_element_by_css_selector('button[data-original-title="Save"]').click()
    browser.find_element_by_xpath('//*[text()="product1"]/../td/input').click()
    browser.find_element_by_css_selector(
        'button[data-original-title="Delete"]').click()
    browser.switch_to_alert().accept()