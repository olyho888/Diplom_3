import allure
from pages.recovery_password_page import RecoveryPasswordPage
from pages.login_page import LoginPage
from data import Data


class TestRecoveryPasswordPage:

    @allure.title('Проверка перехода на страницу Восстановления пароля')
    def test_recovery_password_page_go_to(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_recovery_password()
        recovery_password_page = RecoveryPasswordPage(driver)
        assert recovery_password_page.get_input_label_text() == "Email"

    @allure.title('Проверка ввода почты и клик по кнопке Восстановить')
    def test_recovery_password_page_input_email_click_button(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.open_recovery_page()
        recovery_password_page.input_email(Data.email)
        assert recovery_password_page.get_input_label_text() == "Пароль"

    @allure.title('Проверка клика по кнопке показать/скрыть пароль делает поле активным')
    def test_recovery_password_page_click_button_eye(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.open_recovery_page()
        recovery_password_page.input_email(Data.email)
        recovery_password_page.click_eye()
        element = recovery_password_page.get_password_element()
        assert 'input_status_active' in element.get_attribute('class')
