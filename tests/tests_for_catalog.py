def test_element_catalog_page(browser):
    """Tests for catalog page"""
    browser.find_element_by_class_name('form-control input-lg')
    browser.find_element_by_xpath('//*[text()="My Account"]')
    browser.find_element_by_id('top-links')
    browser.find_element_by_css_selector(
        'img[src="http://localhost/Opencart/image/cache/catalog/demo/canon_eos_5d_1-228x228.jpg"]')
    browser.find_element_by_name('GBP')
