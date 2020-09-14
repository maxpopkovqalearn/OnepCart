from PageObj.AdminPage import AdminLoginPage
from helpers.helper_for_database import getDBQuery
from conftest import wait_for_element
from selenium.webdriver.common.alert import Alert
import pytest


@pytest.mark.parametrize('name, meta_tag, model', [('Test_Product', 'Test_Tag', 'Test_Model')])
def test_add_new_product_and_check_db(browser, get_url, open_admin, name, meta_tag, model):
    """Adding new product with check DB"""
    AdminLoginPage(browser) \
        .open_product_from_catalog() \
        .add_new_element() \
        .input_product_form_general_tab(prod_name=name, meta_tag=meta_tag) \
        .input_product_form_data_tab(model=model) \
        .save_element()
    wait_for_element(browser, AdminLoginPage.GeneralActions.SUCCESS_TEXT)

    query_for_sql = 'SELECT * FROM oc_product WHERE model="Test_Model"'
    assert getDBQuery(query_for_sql)


@pytest.mark.parametrize('name, meta_tag, model', [('Editable_Product', 'Tag', 'Editable')])
def test_edit_product_and_check_db(browser, get_url, open_admin, name, meta_tag, model):
    """Test for Edit one of product and check BD"""
    AdminLoginPage(browser) \
        .open_product_from_catalog() \
        .edit_element() \
        .input_product_form_general_tab(prod_name=name, meta_tag=meta_tag) \
        .input_product_form_data_tab(model=model) \
        .save_element()
    wait_for_element(browser, AdminLoginPage.GeneralActions.SUCCESS_TEXT)
    query_for_sql = 'SELECT * FROM oc_product WHERE model="Editable"'

    assert getDBQuery(query_for_sql)


@pytest.mark.parametrize('name, meta_tag, model', [('Database_prod', 'DB_Tag', 'database_model')])
def test_delete_product_from_db(browser, get_url, open_admin, name, meta_tag, model):
    """Test for delete test product and check BD"""
    # Create new product
    AdminLoginPage(browser) \
        .open_product_from_catalog() \
        .add_new_element() \
        .input_product_form_general_tab(prod_name=name, meta_tag=meta_tag) \
        .input_product_form_data_tab(model=model) \
        .save_element()
    wait_for_element(browser, AdminLoginPage.GeneralActions.SUCCESS_TEXT)

    # Delete new product
    AdminLoginPage(browser) \
        .open_product_from_catalog() \
        .remove_element()
    Alert(browser).accept()
    wait_for_element(browser, AdminLoginPage.GeneralActions.SUCCESS_TEXT)

    query_for_sql = 'SELECT * FROM oc_product WHERE model="database_model"'

    assert not getDBQuery(query_for_sql)
