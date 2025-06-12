from selenium.webdriver.common.by import By
from locators.general_locators import GeneralLocators


class LoginPageLocators(GeneralLocators):

    TITLE_ENTRANCE = (By.XPATH, "//h2[text()='Вход']")
    LINK_PASSWORD_RECOVERY = (By.XPATH, "//p[2]/a[text()='Восстановить пароль']")
    BUTTON_SIGN_IN = (By.XPATH, "//*[contains(@class,'button') and text()='Войти']")
