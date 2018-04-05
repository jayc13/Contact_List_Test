from selenium.webdriver.common.by import By
from base_page_object import BasePage
import time

class CreatePage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://www.automationpractice.com')

    locator_dictionary = {
        "sign_in": (By.CSS_SELECTOR, '.login'),
        "contact_us": (By.LINK_TEXT, 'Contact us'),
        "sign_out": (By.LINK_TEXT, 'Sign out')
    }