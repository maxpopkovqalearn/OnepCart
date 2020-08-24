"""Test for page obj"""
from PageObj.AdminPage import AdminLoginPage
from conftest import wait_for_element
import pytest

def test_login_page(browser, get_url, open_admin):
    assert 'Dashboard' == browser.title

def test_admin_catalog(browser, get_url, open_admin):
    AdminLoginPage(browser)._click_to_element(AdminLoginPage.CATALOG)
