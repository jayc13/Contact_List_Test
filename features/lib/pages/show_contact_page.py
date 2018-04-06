from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class ShowPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)

    locator_dictionary = {
        "title_brand": (By.ID, 'title_brand'),
        "title_label": (By.CSS_SELECTOR, '.title')
    }

    def get_title_text(self):
        return self.find_element(*self.locator_dictionary['title_label']).text

    def back_to_index_page(self):
        return self.find_element(*self.locator_dictionary['title_brand']).click()