from selenium.webdriver.common.by import By
from locators.general_locators import GeneralLocators


class ListOrdersPageLocators(GeneralLocators):

    NUMBER_ORDER_DETAILS = (By.XPATH, "//*[contains(@class, 'Modal_orderBox')]/p[contains(@class, 'type_digits')]")
    ORDER_CONSIST = (By.XPATH, "//*[contains(@class, 'Modal_orderBox')]//p[3]")
    COUNTER_ORDERS_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following::p[1]")
    COUNTER_ORDERS_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following::p[1]")
    ORDER_IN_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li[text()[2]='{}']")
