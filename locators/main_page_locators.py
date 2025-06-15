from selenium.webdriver.common.by import By
from locators.general_locators import GeneralLocators


class MainPageLocators(GeneralLocators):

    HEADER_LOGO = (By.XPATH, "//div[contains(@class, 'header__logo')]/a")
    TITLE_ASSEMBLE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")
    LINK_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    LINK_LIST_OF_ORDERS = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    INGREDIENT = (By.XPATH, "//*[contains(@class,'BurgerIngredient') and text()='{}']")
    BASKET_INGREDIENT = (By.XPATH, "//*[contains(@class,'constructor-element__text') and contains(text(), '{}')]")
    TITLE_INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    BUTTON_CLOSE = (By.XPATH, "//*[contains(@class,'Modal_modal__close')]")
    COUNTER_INGREDIENT = (By.XPATH, "//*[contains(@class,'BurgerIngredient') and text()='{}']/.."
                                    "//p[contains(@class, 'counter_counter')]")
    BURGER_BASKET = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket__list')]")
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER = (By.XPATH, "//*[contains(@class,'Modal_modal__title_shadow')]")
    ORDER_NUMBER_DEFAULT = (By.XPATH, "//*[contains(@class,'Modal_modal__title_shadow') and text()='9999']")
