from selenium.webdriver.common.by import By
from .base_page import BasePage
from .const import Const


class Locators:
    FRAMES_LOCATOR = (By.XPATH, "//a[@href='/frames']")


class MainPage(BasePage):
    def should_be_main_url(self):
        assert Const.HEROKUAPP_URL == self.url

    def go_to_frames_page(self):
        link = self.browser.find_element(*Locators.FRAMES_LOCATOR)
        link.click()
