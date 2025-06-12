# Diplom_3

Автотесты для сервиса Stellar Burgers(https://stellarburgers.nomoreparties.site/)

Основа для написания автотестов — фреймворк pytest, Selenium и requests
Автотесты запускаются в браузере Chrome и Firefox

Проект состоит из:

директории Api_methods - содержит методы API

директории Locators - содержит описание локаторов на страницах
general_locators - описаны локаторы 
list_orders_page_locators - описаны локаторы страницы list_orders_page
login_page_locators - описаны локаторы страницы login_page
main_page_locators - описаны локаторы страницы main_page
personal_account_page_locators - описаны локаторы страницы persona_account_page
recovery_password_page_locators - описаны локаторы страницы recovervy_password__page

директории Pages - содержит описание методов на страницах
base_page - описание базовых методов 
list_orders_page - описание выполняемых методов на странице list_orders
login_page - описаны выполняемых методов на странице login_page
main_page - описание выполняемых методов на странице main_page
personal_account_page - описание выполняемых методов на странице personal_account_page
recovery_password_page - описание выполняемых методов на странице recovery_password_page

директория tests - содержит описание тестов на страницах

test_list_orders_page - содержит тесты:
- test_list_orders_page_click_order - тест на проверку клика на заказ
- test_list_orders_page_check_order_from_history_in_list_orders - тест на проверку наличия заказа из История заказов в Ленте заказов
- test_list_orders_page_check_counter_completed_for_all_time - тест на проверку увеличение счетчика Выполнено за все время при создании зааза
- test_list_orders_page_check_counter_completed_for_today - тест на проверку увеличения счетчика Выполнено за сегодня при создании заказа

test_main_page - содержит тесты:
- test_main_page_go_to_constructor - тест на проверку перехода по клику на Конструктор
- test_main_page_go_to_list_of_orders - тест на проверку перехода по клику на Ленту заказов
- test_main_page_click_ingredient - тест на проверку клика на ингредиент
- test_main_page_button_close - тест на проверку клика на крестик, закрытие окна с ингредиентами
- test_main_page_counter_ingredient - тест на проверку увеличения счетчика ингредиента при добавлении в корзину
- test_main_page_auth_user_create_order - тест на проверку что залогиненный пользователь может оформить заказ

test_personal_account_page - содержит тесты:
- test_personal_account_page_go_to - тест на проверку перехода по клику на Личный кабинет
- test_personal_account_page_go_to_history_of_orders - тест на проверку перехода в раздел История заказов
- test_personal_account_page_logout - тест на проверку выхода из Личного кабинета

test_recovery_password_page - содержит тесты:
- test_recovery_password_page_go_to - тест на проверку перехода на страницу Восстановления пароля
- test_recovery_password_page_input_email_click_button - тест на проверку ввода почты и клик по кнопке Восстановить
- test_recovery_password_page_click_button_eye - тест на проверку клика по кнопке показать/скрыть пароль делает поле активным

директория allure-report - содержит отчет о результатах выполнения тестов, сгенерированный с посмощью фреймворк Allure
