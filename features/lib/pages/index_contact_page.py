__author__ = 'Javier Caballero'
from selenium.webdriver.common.by import By
from .base_page_object import BasePage
from selenium.common.exceptions import NoSuchElementException
import time


class IndexPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)

    locator_dictionary = {
        "title_label": (By.CSS_SELECTOR, '.title'),
        "add_contact_button": (By.ID, 'add_contact'),
        "contact_rows": (By.CSS_SELECTOR, '#table_contacts tbody tr'),
        "contact_rows_delete_button": (By.CSS_SELECTOR, '#table_contacts tbody tr a.delete_contact'),
        "contact_rows_edit_button": (By.CSS_SELECTOR, '#table_contacts tbody tr a.edit_contact'),
        "no_contact_label": (By.XPATH, '//*[contains(text(), "No contacts")]')
        
    }

    def get_title_text(self):
        return self.find_element(*self.locator_dictionary['title_label']).text

    def go_to_create_contact(self):
        self.find_element(*self.locator_dictionary['add_contact_button']).click()

    def get_count_of_contact(self):
        try:
            return len(self.find_elements(*self.locator_dictionary['contact_rows']))
        except NoSuchElementException: 
            return 0

    def is_no_contact_label_present(self):
        try:
            return len(self.find_elements(*self.locator_dictionary['no_contact_label'])) == 1
        except NoSuchElementException: 
            return False

    def delete_contact_by_index(self, index):
        (self.find_elements(*self.locator_dictionary['contact_rows_delete_button'])[index]).click()
        time.sleep(5) 
        self.accept_alert()

    def edit_contact_by_index(self, index):
        (self.find_elements(*self.locator_dictionary['contact_rows_edit_button'])[index]).click()

    class HeaderPage(BasePage):
        def __init__(self, context):
            BasePage.__init__(self, context.browser)

        locator_dictionary = {}
