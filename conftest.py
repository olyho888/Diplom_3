import pytest
from selenium import webdriver
from api_methods.user_methods import UserMethods
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(params=["Chrome", "Firefox"])
def driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.browser_name = request.param
    yield driver
    driver.quit()

@pytest.fixture
def user_auth(driver):
    user_methods = UserMethods()
    user, token = user_methods.create_user()
    del user['name']
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login_user_account(user)
    yield
    user_methods.delete_user(token)

@pytest.fixture
def order_create_fixture(driver):
    main_page = MainPage(driver)
    order = main_page.create_order()
    main_page.click_list_of_orders()
    return order
