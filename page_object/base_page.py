from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def element_is_visible(self, locator, timeout: int = 5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout: int = 6):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def elements_are_visible(self, locator: tuple[str, str], timeout: int = 6):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_all_elements_located(locator))

    def fill_input(self, input_data: str, locator: tuple[str, str], timeout=5):
        self.element_is_visible(locator, timeout)
        return self.driver.find_element(locator[0], locator[1]).send_keys(input_data)

    def click_button(self, locator, timeout=10):
        self.element_is_clickable(locator, timeout)
        el = self.driver.find_element(locator[0], locator[1])
        return el.click()

    def get_texts(self, locator, timeout=3) -> [str]:
        self.element_is_visible(locator, timeout)
        return [k.text for k in self.driver.find_elements(by=locator[0], value=locator[1])]

    def get_element_by_number(self, locator, number, timeout=5) -> [WebElement]:
        els = self.elements_are_visible(locator, timeout)
        if number <= len(els):
            return els[number - 1]
        else:
            raise AttributeError(f'There are ony {len(els)} elements. You\'ve tried to get {number}')

    def get_current_url(self):
        return self.driver.current_url
