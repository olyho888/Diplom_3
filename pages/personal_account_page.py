import allure
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step('Получаем текст со страницы Личного кабинета')
    def get_text_from_personal_account(self):
        text = self.get_text_from_element(PersonalAccountPageLocators.ACCOUNT_TEXT)
        return text

    @allure.step('Кликаем на Историю заказов')
    def click_history_of_orders(self):
        self.check_invisible_element(PersonalAccountPageLocators.MODAL_OVERLAY)
        self.click_to_element(PersonalAccountPageLocators.BUTTON_HISTORY_OF_ORDERS)

    @allure.step('Получаем аттрибут для Истории заказов')
    def get_attribute_history_of_orders(self):
        element = self.find_element_with_wait(PersonalAccountPageLocators.BUTTON_HISTORY_OF_ORDERS)
        return element

    @allure.step('Кликаем на Выход')
    def click_logout(self):
        self.check_invisible_element(PersonalAccountPageLocators.MODAL_OVERLAY)
        self.click_to_element(PersonalAccountPageLocators.BUTTON_LOGOUT)

    @allure.step('Получаем номер заказа в Истории заказов')
    def get_number_in_history_orders(self):
        text = self.get_text_from_element(PersonalAccountPageLocators.NUMBER_ORDER_LIST)
        return text
