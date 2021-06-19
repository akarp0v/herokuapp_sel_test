from selenium.webdriver.common.by import By
from .base_page import BasePage


class Locators:
    NESTED_FRAMES = (By.XPATH, "//a[@href='/nested_frames']")


class FramesPage(BasePage):
    def should_be_frames_url(self):
        assert 'frames' in self.url

    def go_to_nested_frames_page(self):
        link = self.browser.find_element(*Locators.NESTED_FRAMES)
        link.click()
