from selenium.webdriver.common.by import By

def test_element_main_page(browser):
    """Tests for main page"""
    browser.find_element_by_class_name('navbar-header')
    browser.find_element_by_xpath('//*[text()="Wish List"]')
    browser.find_element_by_link_text('Shopping Cart')
    browser.find_element_by_css_selector('a[href="http://localhost/Opencart/index.php?route=product/category&path=57"]')
    browser.find_element_by_name('search')


def test_element_catalog_page(browser):
    """Tests for catalog page"""
    pass
    # browser.find_element_by_class_name('')
    # browser.find_element_by_xpath()
    # browser.find_element_by_id()
    # browser.find_element_by_css_selector()
    # browser.find_element_by_name()


def test_element_card_item_page(browser):
    """Tests for item page"""
    pass
    # browser.find_element_by_class_name('navbar-header')
    # browser.find_element_by_xpath()
    # browser.find_element_by_id()
    # browser.find_element_by_css_selector()
    # browser.find_element_by_name()


def test_element_login_page(browser):
    """Tests for login page"""
    pass
    # browser.find_element_by_class_name('navbar-header')
    # browser.find_element_by_xpath()
    # browser.find_element_by_id()
    # browser.find_element_by_css_selector()
    # browser.find_element_by_name()


def test_element_admin_login_page(browser):
    """Tests for admin login page"""
    pass
    # browser.find_element_by_class_name('navbar-header')
    # browser.find_element_by_xpath()
    # browser.find_element_by_id()
    # browser.find_element_by_css_selector()
    # browser.find_element_by_name()
