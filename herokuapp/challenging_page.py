from selenium.webdriver.common.by import By
from .base_page import BasePage
from .const import Const


class Locators:
    DICERET_CLM_LIST = (By.XPATH, "//thead//th[contains(text(), 'Diceret')]/preceding-sibling::*")
    APEIRIAN7_DELETE_LINK = (By.XPATH, "//tbody//td[contains(text(), 'Apeirian7')]/parent::tr//a[@href='#delete']")
    APEIRIAN2_EDIT_LINK = (By.XPATH, "//tbody//td[contains(text(), 'Apeirian2')]/parent::tr//a[@href='#edit']")
    DEFINIEBAS7 = (By.XPATH, "//tbody//td[contains(text(), 'Definiebas7')]")
    IUVARET7 = (By.XPATH, "//tbody//td[contains(text(), 'Iuvaret7')]")
    GREEN_BTN = (By.CSS_SELECTOR, ".button.success")


class ChallengingPage(BasePage):
    def should_be_challenging_url(self):
        assert 'challenging_dom' in self.url

    def highlight_third_row(self, delay=Const.DELAY):
        clm_index = len(self.browser.find_elements(*Locators.DICERET_CLM_LIST)) + 1
        third_row = self.browser.find_element(By.XPATH, f"//tbody//tr[3]//td[{clm_index}]")
        self.highlight_elem(third_row, delay)

    def highlight_delete_link(self, delay=Const.DELAY):
        delete_link = self.browser.find_element(*Locators.APEIRIAN7_DELETE_LINK)
        self.highlight_elem(delete_link, delay)

    def highlight_edit_link(self, delay=Const.DELAY):
        edit_link = self.browser.find_element(*Locators.APEIRIAN2_EDIT_LINK)
        self.highlight_elem(edit_link, delay)

    def highlight_definiebas(self, delay=Const.DELAY):
        definiebas = self.browser.find_element(*Locators.DEFINIEBAS7)
        self.highlight_elem(definiebas, delay)

    def highlight_iuvaret(self, delay=Const.DELAY):
        iuvaret = self.browser.find_element(*Locators.IUVARET7)
        self.highlight_elem(iuvaret, delay)

    def click_green_btn(self):
        green_btn = self.browser.find_element(*Locators.GREEN_BTN)
        green_btn.click()
