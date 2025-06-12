import allure
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from pages.main_page import MainPage


class TestPersonalAccountPage:

    @allure.title('Проверка перехода по клику на Личный кабинет')
    def test_personal_account_page_go_to(self, driver, user_auth):
        main_page = MainPage(driver)
        main_page.click_personal_account()
        personal_account_page = PersonalAccountPage(driver)
        assert 'свои персональные данные' in personal_account_page.get_text_from_personal_account()

    @allure.title('Проверка перехода в раздел История заказов')
    def test_personal_account_page_go_to_history_of_orders(self, driver, user_auth):
        main_page = MainPage(driver)
        main_page.click_personal_account()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_history_of_orders()
        element = personal_account_page.get_attribute_history_of_orders()
        assert 'Account_link_active' in element.get_attribute('class')

    @allure.title('Проверка выхода из Личного кабинета')
    def test_personal_account_page_logout(self, driver, user_auth):
        main_page = MainPage(driver)
        main_page.click_personal_account()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_logout()
        login_page = LoginPage(driver)
        assert login_page.get_title_text() == 'Вход'
