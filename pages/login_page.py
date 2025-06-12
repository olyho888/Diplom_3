import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from data import Data


class LoginPage(BasePage):

    @allure.step('Открываем страницу входа в личный кабинет')
    def open_login_page(self):
        self.open_web_page(Data.URL_LOGIN_PAGE)
        self.find_element_with_wait(LoginPageLocators.TITLE_ENTRANCE)

    @allure.step('Кликаем на ссылку восстановления пароля')
    def click_recovery_password(self):
        self.check_invisible_element(LoginPageLocators.MODAL_OVERLAY)
        self.click_to_element(LoginPageLocators.LINK_PASSWORD_RECOVERY)
        self.check_invisible_element(LoginPageLocators.TITLE_ENTRANCE)

    @allure.step('Входим в аккаунт пользователя')
    def login_user_account(self, user):
        self.send_text_to_element(LoginPageLocators.EMAIL_INPUT, user['email'])
        self.send_text_to_element(LoginPageLocators.PASSWORD_INPUT, user['password'])
        self.check_invisible_element(LoginPageLocators.MODAL_OVERLAY)
        self.click_to_element(LoginPageLocators.BUTTON_SIGN_IN)
        self.check_invisible_element(LoginPageLocators.TITLE_ENTRANCE)

    @allure.step('Получаем текст заголовка страницы')
    def get_title_text(self):
        text = self.get_text_from_element(LoginPageLocators.TITLE_PAGE)
        return text
