"""Test for page obj"""
from PageObj.AdminPage import AdminLoginPage
from conftest import wait_for_element
import pytest
import allure
from selenium.webdriver.common.alert import Alert


@allure.title('Test for Dashboard')
def test_login_page(browser, get_url, open_admin):
    with allure.step('Проверка title страницы'):
        assert 'Dashboard' == browser.title


@allure.title('Test for click Catalog')
def test_admin_catalog(browser, get_url, open_admin):
    with allure.step('Клик по элементу каталога'):
        AdminLoginPage(browser)._click_to_element(AdminLoginPage.CATALOG)


@allure.title('Test for Adding product without img')
@pytest.mark.parametrize('name, meta_tag, model', [('Test_Product', 'Test_Tag', 'Test_Model')])
def test_add_new_product(browser, get_url, open_admin, name, meta_tag, model):
    """Adding new product"""
    AdminLoginPage(browser) \
        .open_product_from_catalog() \
        .add_new_element() \
        .input_product_form_general_tab(prod_name=name, meta_tag=meta_tag) \
        .input_product_form_data_tab(model=model) \
        .save_element()

    # Check result
    wait_for_element(browser, AdminLoginPage.GeneralActions.SUCCESS_TEXT)
    success_text = browser.find_element(*AdminLoginPage.GeneralActions.SUCCESS_TEXT)

    assert success_text.is_displayed()


@allure.title('Test for Edit product')
@pytest.mark.parametrize('name, meta_tag, model', [('Edit_Product', 'Edit_Tag', 'Edit_Model')])
def test_edit_product(browser, get_url, open_admin, name, meta_tag, model):
    """Test for Edit one of product"""
    AdminLoginPage(browser) \
        .open_product_from_catalog() \
        .edit_element() \
        .input_product_form_general_tab(prod_name=name, meta_tag=meta_tag) \
        .input_product_form_data_tab(model=model) \
        .save_element()

    # Check result
    wait_for_element(browser, AdminLoginPage.GeneralActions.SUCCESS_TEXT)
    success_text = browser.find_element(*AdminLoginPage.GeneralActions.SUCCESS_TEXT)

    assert success_text.is_displayed()

@allure.title('Test for delete product')
@pytest.mark.parametrize('name, meta_tag, model', [('Test_123', '123_Tag', '123_model')])
def test_delete_product(browser, get_url, open_admin, name, meta_tag, model):
    """Test for delete test product"""
    # Adding new product
    AdminLoginPage(browser) \
        .open_product_from_catalog() \
        .add_new_element() \
        .input_product_form_general_tab(prod_name=name, meta_tag=meta_tag) \
        .input_product_form_data_tab(model=model) \
        .save_element()
    wait_for_element(browser, AdminLoginPage.GeneralActions.SUCCESS_TEXT)
    # Delete product
    AdminLoginPage(browser) \
        .open_product_from_catalog() \
        .remove_element()
    Alert(browser).accept()
    # Check result
    wait_for_element(browser, AdminLoginPage.GeneralActions.SUCCESS_TEXT)
    success_text = browser.find_element(*AdminLoginPage.GeneralActions.SUCCESS_TEXT)

    assert success_text.is_displayed()


@allure.title('Test for add new product with img')
@pytest.mark.parametrize('name, meta_tag, model', [('Test_Product', 'Test_Tag', 'Test_Model')])
def test_add_new_product_with_image(browser, get_url, open_admin, name, meta_tag, model):
    """Adding new product"""
    with allure.step('Добавление продукта'):
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
