def test_element_admin_login_page(browser):
    """Tests for admin login page"""
    browser.find_element_by_class_name('input-group-addon')
    browser.find_element_by_xpath('//*[text()="Forgotten Password"]')
    browser.find_element_by_id('input-password')
    browser.find_element_by_name('username')
