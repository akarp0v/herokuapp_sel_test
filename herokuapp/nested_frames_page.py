from selenium.webdriver.common.by import By
from .base_page import BasePage
from .const import Const


class Locators:
    FRAME_TOP = (By.XPATH, "//frame[@name='frame-top']")

    FRAME_LEFT = (By.XPATH, "//frame[@name='frame-left']")
    LEFT_BODY = (By.XPATH, f"//body[contains(text(), 'LEFT')]")
    LEFT_TEXT = (By.XPATH, f"//body[contains(text(), '{Const.LEFT_TEXT}')]")

    FRAME_MIDDLE = (By.XPATH, "//frame[@name='frame-middle']")
    MIDDLE_DIV = (By.CSS_SELECTOR, "#content")
    MIDDLE_TEXT = (By.XPATH, f"//div[contains(text(), '{Const.MIDDLE_TEXT}')]")

    FRAME_RIGHT = (By.XPATH, "//frame[@name='frame-right']")
    RIGHT_BODY = (By.XPATH, f"//body[contains(text(), 'RIGHT')]")
    RIGHT_TEXT = (By.XPATH, f"//body[contains(text(), '{Const.RIGHT_TEXT}')]")

    FRAME_BOTTOM = (By.XPATH, "//frame[@name='frame-bottom']")
    BOTTOM_BODY = (By.XPATH, f"//body[contains(text(), 'BOTTOM')]")
    BOTTOM_TEXT = (By.XPATH, f"//body[contains(text(), '{Const.BOTTOM_TEXT}')]")


class NestedFramesPage(BasePage):
    def should_be_nested_frames_url(self):
        assert 'nested_frames' in self.url

    def add_text_to_element(self, element, text):
        self.browser.execute_script("arguments[0].innerHTML = arguments[1];", element, text)

    def change_left_text(self):
        self.browser.switch_to.default_content()
        frame_top = self.browser.find_element(*Locators.FRAME_TOP)
        self.browser.switch_to.frame(frame_top)
        frame_left = self.browser.find_element(*Locators.FRAME_LEFT)
        self.browser.switch_to.frame(frame_left)
        left_body = self.browser.find_element(*Locators.LEFT_BODY)
        self.add_text_to_element(left_body, Const.LEFT_TEXT)

    def change_middle_text(self):
        self.browser.switch_to.default_content()
        frame_top = self.browser.find_element(*Locators.FRAME_TOP)
        self.browser.switch_to.frame(frame_top)
        frame_middle = self.browser.find_element(*Locators.FRAME_MIDDLE)
        self.browser.switch_to.frame(frame_middle)
        middle_div = self.browser.find_element(*Locators.MIDDLE_DIV)
        self.add_text_to_element(middle_div, Const.MIDDLE_TEXT)

    def change_right_text(self):
        self.browser.switch_to.default_content()
        frame_top = self.browser.find_element(*Locators.FRAME_TOP)
        self.browser.switch_to.frame(frame_top)
        frame_right = self.browser.find_element(*Locators.FRAME_RIGHT)
        self.browser.switch_to.frame(frame_right)
        right_body = self.browser.find_element(*Locators.RIGHT_BODY)
        self.add_text_to_element(right_body, Const.RIGHT_TEXT)

    def change_bottom_text(self):
        self.browser.switch_to.default_content()
        frame_bottom = self.browser.find_element(*Locators.FRAME_BOTTOM)
        self.browser.switch_to.frame(frame_bottom)
        bottom_body = self.browser.find_element(*Locators.BOTTOM_BODY)
        self.add_text_to_element(bottom_body, Const.BOTTOM_TEXT)

    def should_be_left_text(self):
        assert self.is_element_present(*Locators.LEFT_TEXT), \
            "Left text is not presented"

    def should_be_middle_text(self):
        assert self.is_element_present(*Locators.MIDDLE_TEXT), \
            "Middle text is not presented"

    def should_be_right_text(self):
        assert self.is_element_present(*Locators.RIGHT_TEXT), \
            "Right text is not presented"

    def should_be_bottom_text(self):
        assert self.is_element_present(*Locators.BOTTOM_TEXT), \
            "Bottom text is not presented"
