import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import Data


class MainPage(BasePage):

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.open_web_page(Data.BASE_URL)
        self.find_element_with_wait(MainPageLocators.HEADER_LOGO)

    @allure.step('Кликаем на ссылку Личный кабинет')
    def click_personal_account(self):
        self.check_invisible_element(MainPageLocators.MODAL_OVERLAY)
        self.click_to_element(MainPageLocators.LINK_PERSONAL_ACCOUNT)

    @allure.step('Кликаем на ссылку Конструктор')
    def click_constructor(self):
        self.check_invisible_element(MainPageLocators.MODAL_OVERLAY)
        self.click_to_element(MainPageLocators.LINK_CONSTRUCTOR)
        self.find_element_with_wait(MainPageLocators.TITLE_ASSEMBLE_BURGER)

    @allure.step('Кликаем на ссылку Лента заказов')
    def click_list_of_orders(self):
        self.check_invisible_element(MainPageLocators.MODAL_OVERLAY)
        self.click_to_element(MainPageLocators.LINK_LIST_OF_ORDERS)
        self.find_element_with_wait(MainPageLocators.TITLE_LIST_OF_ORDERS)

    @allure.step('Получаем текст заголовка Конструктор')
    def get_title_text_constructor(self):
        text = self.get_text_from_element(MainPageLocators.TITLE_ASSEMBLE_BURGER)
        return text

    @allure.step('Получаем текст заголовка Лента заказов')
    def get_title_text_list_of_orders(self):
        text = self.get_text_from_element(MainPageLocators.TITLE_LIST_OF_ORDERS)
        return text

    @allure.step('Кликаем на Ингредиент')
    def click_ingredient(self, name):
        self.check_invisible_element(MainPageLocators.MODAL_OVERLAY)
        ingredient_locator = self.format_locators(MainPageLocators.INGREDIENT, name)
        self.click_to_element(ingredient_locator)
        self.find_element_with_wait(MainPageLocators.TITLE_INGREDIENT_DETAILS)

    @allure.step('Получаем текст из заголовка Ингредиента')
    def get_title_text_ingredient(self):
        text = self.get_text_from_element(MainPageLocators.TITLE_INGREDIENT_DETAILS)
        return text

    @allure.step('Получаем счетчик ингредиента')
    def get_ingredient_counter(self, name):
        counter_locator = self.format_locators(MainPageLocators.COUNTER_INGREDIENT, name)
        counter = self.get_text_from_element(counter_locator)
        return int(counter)

    @allure.step('Кликаем на крестик')
    def click_button_close(self):
        self.check_invisible_element(MainPageLocators.MODAL_OVERLAY)
        self.click_to_element(MainPageLocators.BUTTON_CLOSE)
        self.check_invisible_element(MainPageLocators.BUTTON_CLOSE)

    @allure.step('Проверяем что Детали ингредиента становятся невидимые')
    def check_invisible_ingredient_details(self):
        invisible = self.check_invisible_element(MainPageLocators.TITLE_INGREDIENT_DETAILS)
        return invisible

    @allure.step('Добавляем ингредиент в корзину')
    def add_ingredient_to_basket(self, name):
        ingredient_locator = self.format_locators(MainPageLocators.INGREDIENT, name)
        self.drag_and_drop(ingredient_locator, MainPageLocators.BURGER_BASKET)
        ingredient_locator = self.format_locators(MainPageLocators.BASKET_INGREDIENT, name)
        self.find_element_with_wait(ingredient_locator)

    @allure.step('Кликаем на кнопку Оформить заказ')
    def click_button_make_order(self):
        self.check_invisible_element(MainPageLocators.MODAL_OVERLAY)
        self.click_to_element(MainPageLocators.BUTTON_MAKE_ORDER)

    @allure.step('Получаем номер созданного заказа')
    def get_order_number(self):
        text = "9999"
        while text == '9999':
            self.check_invisible_element(MainPageLocators.ORDER_NUMBER_DEFAULT)
            text = self.get_text_from_element(MainPageLocators.ORDER_NUMBER)
        return text

    @allure.step('Создаем новый заказ')
    def create_order(self):
        for ingredient in Data.ingredients_list:
            self.add_ingredient_to_basket(ingredient)
        self.click_button_make_order()
        number_order = self.get_order_number()
        self.click_button_close()
        return number_order
