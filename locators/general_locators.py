from selenium.webdriver.common.by import By


class GeneralLocators:

    MODAL_OVERLAY = (By.XPATH, "//*[contains(@class,'Modal_modal__loading')]/"
                               "following::div[contains(@class,'Modal_modal_overlay')]")
    TITLE_PAGE = (By.XPATH, "//div[contains(@class, 'Auth_login')]/h2[text()]")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    TITLE_LIST_OF_ORDERS = (By.XPATH, "//h1[text()='Лента заказов']")
    LINK_PERSONAL_ACCOUNT = (By.XPATH, "//a[contains(@class, 'header__link')]/p[text()='Личный Кабинет']")
    NUMBER_ORDER_LIST = (By.XPATH, "//*[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'type_digits')]")
    NUMBER_ORDER_LIST_WITH_TEXT = (By.XPATH, "//*[contains(@class, 'OrderHistory_textBox')]/"
                                             "p[contains(@class, 'type_digits') and text()='{}']")
