from selenium.webdriver.common.by import By
from .base_page import BasePage
from .const import Const


class Locators:
    START_BTN = (By.XPATH, "//button[contains(text(), 'Start')]")
    FINISH_TEXT = (By.CSS_SELECTOR, "#finish")


class DynamicPage(BasePage):
    def should_be_dynamic_url(self):
        assert 'dynamic_loading' in self.url

    def click_start_btn(self):
        start_btn = self.browser.find_element(*Locators.START_BTN)
        start_btn.click()

    def should_present_finish_text(self):
        assert self.is_element_visible(*Locators.FINISH_TEXT), \
            "Finish text is not presented"

    def print_finish_text(self):
        finish = self.browser.find_element(*Locators.FINISH_TEXT)
        print(f'\nDisplayed text: {Const.GREEN}{finish.text}{Const.DEFAULT}')
