def test_element_main_page(browser):
    """Tests for main page"""
    browser.find_element_by_class_name('navbar-header')
    browser.find_element_by_xpath('//*[text()="Wish List"]')
    browser.find_element_by_link_text('Shopping Cart')
    browser.find_element_by_css_selector('a[href="http://localhost/Opencart/index.php?route=product/category&path=57"]')
    browser.find_element_by_name('search')