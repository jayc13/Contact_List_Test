from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class ShowPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    locator_dictionary = {
        "title_label": (By.CSS_SELECTOR, '.title')
    }