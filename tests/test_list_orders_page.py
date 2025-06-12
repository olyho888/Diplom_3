import allure
from pages.main_page import MainPage
from pages.list_orders_page import ListOrdersPage
from pages.personal_account_page import PersonalAccountPage


class TestListOrdersPage:

    @allure.title('Проверка клика на заказ')
    def test_list_orders_page_click_order(self, driver):
        list_orders_page = ListOrdersPage(driver)
        list_orders_page.open_orders_page()
        list_orders_page.click_order_in_list()
        assert list_orders_page.get_title_in_order_details() == 'Cостав'

    @allure.title('Проверка наличия заказа из История заказов в Ленте заказов')
    def test_list_orders_page_check_order_from_history_in_list_orders(self, driver, user_auth, order_create_fixture):
        main_page = MainPage(driver)
        main_page.click_personal_account()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_history_of_orders()
        order_number = personal_account_page.get_number_in_history_orders()
        main_page.click_list_of_orders()
        list_order_page = ListOrdersPage(driver)
        element = list_order_page.get_order_in_list_orders(order_number)
        assert element.is_displayed()

    @allure.title('Проверка увеличения счетчика Выполнено за все время при создании заказа')
    def test_list_orders_page_check_counter_completed_for_all_time(self, driver, user_auth):
        main_page = MainPage(driver)
        main_page.click_list_of_orders()
        list_order_page = ListOrdersPage(driver)
        counter_1 = list_order_page.get_counter_orders_all_time()
        main_page.click_constructor()
        number = '#0' + main_page.create_order()
        main_page.click_list_of_orders()
        list_order_page.get_order_in_list_orders(number)
        counter_2 = list_order_page.get_counter_orders_all_time()
        assert counter_2 > counter_1

    @allure.title('Проверка увеличения счетчика Выполнено за сегодня при создании заказа')
    def test_list_orders_page_check_counter_completed_for_today(self, driver, user_auth):
        main_page = MainPage(driver)
        main_page.click_list_of_orders()
        list_order_page = ListOrdersPage(driver)
        counter_1 = list_order_page.get_counter_orders_today()
        main_page.click_constructor()
        number = '#0' + main_page.create_order()
        main_page.click_list_of_orders()
        list_order_page.get_order_in_list_orders(number)
        counter_2 = list_order_page.get_counter_orders_today()
        assert counter_2 > counter_1

    @allure.title('Проверка появления созданного заказа в разделе В работе')
    def test_list_orders_page_check_order_in_work(self, driver, user_auth, order_create_fixture):
        list_order_page = ListOrdersPage(driver)
        element = list_order_page.get_order_in_work(order_create_fixture)
        assert element.is_displayed()
