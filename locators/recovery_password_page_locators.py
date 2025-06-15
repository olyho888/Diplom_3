from selenium.webdriver.common.by import By
from locators.general_locators import GeneralLocators


class RecoveryPasswordLocators(GeneralLocators):

    BUTTON_RESTORE = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_ICON_EYE = (By.XPATH, "//*[contains(@class,'input__icon')]")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/parent::div")
    INPUT_LABEL = (By.XPATH, "//label[text()]")
