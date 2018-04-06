from selenium.webdriver.common.by import By
from .base_page_object import BasePage
from selenium.webdriver.common.keys import Keys


class CreatePage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)

    locator_dictionary = {
        "title_label": (By.CSS_SELECTOR, '.title'),
        "first_name_input": (By.ID, 'contact_first_name'),
        "last_name_input": (By.ID, 'contact_last_name'),
        "email_input": (By.ID, 'contact_email'),
        "mobile_input": (By.ID, 'contact_mobile'),
        "save_button": (By.ID, 'save_contact'),
        "back_button": (By.ID, 'back')

    }

    def get_title_text(self):
        return self.find_element(*self.locator_dictionary['title_label']).text

    def fill_contact_form(self, first_name, last_name, email, mobile):
        self.find_element(*self.locator_dictionary['first_name_input']).clear()
        self.find_element(*self.locator_dictionary['first_name_input']).send_keys(first_name)
        self.find_element(*self.locator_dictionary['last_name_input']).clear()
        self.find_element(*self.locator_dictionary['last_name_input']).send_keys(last_name)
        self.find_element(*self.locator_dictionary['email_input']).clear()
        self.find_element(*self.locator_dictionary['email_input']).send_keys(email)
        self.find_element(*self.locator_dictionary['mobile_input']).clear()
        self.find_element(*self.locator_dictionary['mobile_input']).send_keys(mobile)

    def save_contact_form(self):
        self.find_element(*self.locator_dictionary['save_button']).click()