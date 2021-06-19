from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_visible(self, how, what, timeout=60):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def highlight_elem(self, element, delay):
        def apply_style(style):
            self.browser.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                        element, style)

        original_style = element.get_attribute('style')
        apply_style("background: yellow;")
        sleep(delay)
        apply_style(original_style)
