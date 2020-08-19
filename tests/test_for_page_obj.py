"""Test for page obj"""
from PageObj.AdminPage import AdminLoginPage
from conftest import wait_for_element
import pytest

def test_login_page(browser, get_url, open_admin):
    assert 'Dashboard' == browser.title

def test_admin_catalog(browser, get_url, open_admin):
    AdminLoginPage(browser)._click_to_element(AdminLoginPage.CATALOG)

@pytest.mark.parametrize('name, meta_tag, model', [('Test_Product', 'Test_Tag', 'Test_Model')])
def test_add_new_product_with_image(browser, get_url, open_admin, name, meta_tag, model):
    """Adding new product"""
    AdminLoginPage(browser) \
        .open_product_from_catalog() \
        .add_new_element() \
        .input_product_form_general_tab(prod_name=name, meta_tag=meta_tag) \
        .input_product_form_data_tab(model=model) \
        .upload_new_image() \
        .select_image_from_explorer() \
        .close_upload_window() \
        .save_element()

    # Check result
    wait_for_element(browser, AdminLoginPage.GeneralActions.SUCCESS_TEXT)
    success_text = browser.find_element(*AdminLoginPage.GeneralActions.SUCCESS_TEXT)

    assert success_text.is_displayed()
