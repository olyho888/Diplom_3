import allure
from locators.recovery_password_page_locators import RecoveryPasswordLocators
from pages.base_page import BasePage
from data import Data


class RecoveryPasswordPage(BasePage):

    @allure.step('Открываем страницу восстановления пароля')
    def open_recovery_page(self):
        self.open_web_page(Data.URL_RECOVERY_PASSWORD_PAGE)
        self.find_element_with_wait(RecoveryPasswordLocators.TITLE_PAGE)

    @allure.step('Получаем текст подсказки поля ввода')
    def get_input_label_text(self):
        text = self.get_text_from_element(RecoveryPasswordLocators.INPUT_LABEL)
        return text

    @allure.step('Вводим почту')
    def input_email(self, email):
        self.find_element_with_wait(RecoveryPasswordLocators.EMAIL_INPUT)
        self.send_text_to_element(RecoveryPasswordLocators.EMAIL_INPUT, email)
        self.check_invisible_element(RecoveryPasswordLocators.MODAL_OVERLAY)
        self.click_to_element(RecoveryPasswordLocators.BUTTON_RESTORE)
        self.find_element_with_wait(RecoveryPasswordLocators.PASSWORD_INPUT)

    @allure.step('Кликаем по кнопке показать/скрыть')
    def click_eye(self):
        self.find_element_with_wait(RecoveryPasswordLocators.PASSWORD_ICON_EYE)
        self.check_invisible_element(RecoveryPasswordLocators.MODAL_OVERLAY)
        self.click_to_element(RecoveryPasswordLocators.PASSWORD_ICON_EYE)

    @allure.step('Получаем элемент для поля Пароль')
    def get_password_element(self):
        element = self.find_element_with_wait(RecoveryPasswordLocators.PASSWORD_FIELD)
        return element
