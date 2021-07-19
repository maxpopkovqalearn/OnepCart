import allure
from Pages.LoginPage import LoginPage

@allure.title("Тест проверки формы авторизации")
def test_for_get_url(browser, get_url):
    LoginPage(browser) \
        .sign_in()
    assert browser.current_url == "http://localhost:8003/"

