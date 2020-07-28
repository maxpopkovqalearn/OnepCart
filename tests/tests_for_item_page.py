def test_element_card_item_page(browser):
    """Tests for item page"""
    browser.find_element_by_class_name('form-control')
    browser.find_element_by_xpath('//*[text()="Description"]')
    browser.find_element_by_id('button-cart')
    browser.find_element_by_css_selector(
        '[src="http://localhost/Opencart/image/cache/catalog/demo/samsung_tab_7-74x74.jpg"]')
    browser.find_element_by_name()
