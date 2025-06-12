from selenium.webdriver.common.by import By
from locators.general_locators import GeneralLocators


class PersonalAccountPageLocators(GeneralLocators):

    ACCOUNT_TEXT = (By.XPATH, "//*[contains(@class,'Account_text')]")
    BUTTON_HISTORY_OF_ORDERS = (By.XPATH, "//*[contains(@class,'text_type') and text()='История заказов']")
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")
