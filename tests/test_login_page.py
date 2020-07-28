def test_element_login_page(browser):
    """Tests for login page"""
    browser.find_element_by_class_name('btn btn-primary')
    browser.find_element_by_xpath('//*[text()="Cameras"]')
    browser.find_element_by_id('input-email')
    browser.find_element_by_css_selector('a[href="http://localhost/Opencart/index.php?route=account/login"]')
    browser.find_element_by_name('password')
