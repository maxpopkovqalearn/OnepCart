"""Test for page obj"""

def test_main_page_add(main_page):
    main_page.add_to_card_button()


def test_main_page_elem(main_page):
    main_page._wait_for_visible(main_page.PRODUCT_HEADER)


def test_login_page(adminpage):
    adminpage._login(name="admin", password="admin")

def test_admin_catalog(adminpage):
    adminpage._login(name="admin", password="admin")
    adminpage._click_to_element(locator=adminpage.CATALOG)
