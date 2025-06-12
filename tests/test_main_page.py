import allure
import pytest
from pages.main_page import MainPage
from data import Data


class TestMainPage:

    @allure.title('Проверка перехода  по клику на Конструктор')
    def test_main_page_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_personal_account()
        main_page.click_constructor()
        assert 'Соберите бургер' == main_page.get_title_text_constructor()

    @allure.title('Проверка перехода  по клику на Ленту заказов')
    def test_main_page_go_to_list_of_orders(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_personal_account()
        main_page.click_list_of_orders()
        assert 'Лента заказов' == main_page.get_title_text_list_of_orders()

    @allure.title('Проверка клика на ингредиент')
    @pytest.mark.parametrize('name', Data.ingredients_list)
    def test_main_page_click_ingredient(self, driver, name):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredient(name)
        assert 'Детали ингредиента' == main_page.get_title_text_ingredient()

    @allure.title('Проверка клика на крестик, закрытие окна с ингредиентами')
    def test_main_page_button_close(self, driver):
        name = Data.ingredients_list[0]
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredient(name)
        main_page.click_button_close()
        assert main_page.check_invisible_ingredient_details()

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении в корзину')
    def test_main_page_counter_ingredient(self, driver):
        name = Data.ingredients_list[1]
        main_page = MainPage(driver)
        main_page.open_main_page()
        counter_1 = main_page.get_ingredient_counter(name)
        main_page.add_ingredient_to_basket(name)
        counter_2 = main_page.get_ingredient_counter(name)
        assert 1 <= counter_2 - counter_1 <= 2

    @allure.title('Проверка что залогиненный пользователь может оформить заказ')
    def test_main_page_auth_user_create_order(self, driver, user_auth):
        main_page = MainPage(driver)
        order = main_page.create_order()
        assert order != '9999'
