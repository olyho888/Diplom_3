from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_web_page(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def check_invisible_element(self, locator):
        invisible = WebDriverWait(self.driver, 15).until(ec.invisibility_of_element(locator))
        return invisible

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(locator))
        self.find_element_with_wait(locator).click()

    def send_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @staticmethod
    def format_locators(locators_1, value):
        method, locator = locators_1
        locator = locator.format(value)
        return method, locator

    def drag_and_drop(self, locator_from, locator_to):
        element_from = self.find_element_with_wait(locator_from)
        element_to = self.find_element_with_wait(locator_to)
        if self.driver.browser_name == 'Chrome':
            action = ActionChains(self.driver)
            action.drag_and_drop(element_from, element_to).perform()
        else:
            self.driver.execute_script("""
                const [element_from, element_to] = arguments;
                const dataTransfer = new DataTransfer();
                ['dragstart', 'dragover', 'drop', 'dragend'].forEach(eventType => {
                const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
                (eventType === 'dragstart' ? element_from : element_to).dispatchEvent(event);
                });
            """, element_from, element_to)
