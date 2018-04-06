__author__ = 'Javier Caballero'
from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class IndexPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "sign_in": (By.CSS_SELECTOR, '.login'),
        "add_contact_button": (By.CSS_SELECTOR, '#add_contact')
    }

    def go_to_create_contact(self):
        self.find_element(*self.locator_dictionary['add_contact_button']).click()

    class HeaderPage(BasePage):
        def __init__(self, context):
            BasePage.__init__(self, context.browser)

        locator_dictionary = {}
