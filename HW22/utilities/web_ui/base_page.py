from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 10)

    def _wait_until_element_located(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def _wait_until_element_not_located(self, locator):
        return self.__wait.until_not(EC.presence_of_element_located(locator))

    def _wait_until_element_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def _wait_until_element_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def _send_keys(self, locator, value, is_clear=True):
        element = self._wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def _click(self, locator):
        element = self._wait_until_element_clickable(locator)
        element.click()

    def _is_displayed(self, locator):
        try:
            self._wait_until_element_visible(locator)
            return True
        except TimeoutException:
            return False

    def _is_located(self, locator):
        try:
            self._wait_until_element_located(locator)
            return True
        except TimeoutException:
            return False

    def _is_not_located(self, locator):
        try:
            self._wait_until_element_not_located(locator)
            return True
        except TimeoutException:
            return False

    def _get_attribute_value(self, locator, attribute):
        element = self._wait_until_element_visible(locator)
        result = element.get_attribute(attribute)
        return result

    def _is_located_for_scroller(self, locator):
        wait = WebDriverWait(self._driver, 0.1)
        try:
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def _scroller(self, locator):
        scroll_down = 0
        for _ in range(20):
            if self._is_located_for_scroller(locator) is True:
                break
            else:
                scroll_down += 300
                self._driver.execute_script(f'window.scrollTo(0, {scroll_down})')

    def _scroll_to_bottom(self):
        self._driver.execute_script('window.scrollTo(0, document. body. scrollHeight)')
