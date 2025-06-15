import allure
from locators.list_orders_page_locators import ListOrdersPageLocators
from pages.base_page import BasePage
from data import Data


class ListOrdersPage(BasePage):

    @allure.step('Открываем страницу Лента заказов')
    def open_orders_page(self):
        self.open_web_page(Data.URL_ORDER_PAGE)
        self.find_element_with_wait(ListOrdersPageLocators.TITLE_LIST_OF_ORDERS)

    @allure.step('Кликаем на заказ в Ленте заказов')
    def click_order_in_list(self):
        self.check_invisible_element(ListOrdersPageLocators.MODAL_OVERLAY)
        self.click_to_element(ListOrdersPageLocators.NUMBER_ORDER_LIST)
        self.find_element_with_wait(ListOrdersPageLocators.NUMBER_ORDER_DETAILS)

    @allure.step('Получаем текст заголовка в деталях заказа')
    def get_title_in_order_details(self):
        text = self.get_text_from_element(ListOrdersPageLocators.ORDER_CONSIST)
        return text

    @allure.step('Получаем заказ в Ленте заказов')
    def get_order_in_list_orders(self, number):
        locator = self.format_locators(ListOrdersPageLocators.NUMBER_ORDER_LIST_WITH_TEXT, number)
        element = self.find_element_with_wait(locator)
        return element

    @allure.step('Получаем заказ В работе')
    def get_order_in_work(self, number):
        locator = self.format_locators(ListOrdersPageLocators.ORDER_IN_WORK, number)
        element = self.find_element_with_wait(locator)
        return element

    @allure.step('Получаем счетчик заказов Выполнено за все время')
    def get_counter_orders_all_time(self):
        counter = self.get_text_from_element(ListOrdersPageLocators.COUNTER_ORDERS_ALL_TIME)
        return int(counter)

    @allure.step('Получаем счетчик заказов Выполнено за сегодня')
    def get_counter_orders_today(self):
        counter = self.get_text_from_element(ListOrdersPageLocators.COUNTER_ORDERS_TODAY)
        return int(counter)
