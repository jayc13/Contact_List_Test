from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class EditPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser)

    locator_dictionary = {
        "title_label": (By.CSS_SELECTOR, '.title'),
        "first_name_input": (By.CSS_SELECTOR, '#contact_first_name'),
        "last_name_input": (By.CSS_SELECTOR, '#contact_last_name'),
        "email_input": (By.CSS_SELECTOR, '#contact_email'),
        "mobile_input": (By.CSS_SELECTOR, '#contact_mobile'),
        "save_button": (By.CSS_SELECTOR, '#save_contact'),
        "back_button": (By.CSS_SELECTOR, '#back')
    }