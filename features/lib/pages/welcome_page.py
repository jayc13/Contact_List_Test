from selenium.webdriver.common.by import By
from lib.pages.base_page_object import BasePage


class WelcomePage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='http://www.practiceselenium.com')

    locator_dictionary = {
        "sign_in": (By.LINK_TEXT, 'Sign in'),
        "contact_us": (By.LINK_TEXT, 'Contact us'),
        "sign_out": (By.LINK_TEXT, 'Sign out')
    }

    class HeaderPage(BasePage):
        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser,
                base_url='http://www.practiceselenium.com')
        locator_dictionary = {
            "menu_women": (By.XPATH, "//*[@title='Women']"),
            "menu_dresses": (By.XPATH, "//*[@title='Dresses']"),
            "menu_tshirts": (By.XPATH, "//*[@title='T-shirts']")
        }

        class DressesPage(BasePage):
            def __init__(self, context):
                BasePage.__init__(
                    self,
                    context.browser,
                    base_url='http://www.practiceselenium.com')
            locator_dictionary = {
                "summer_dresses": (By.XPATH, "//*[@title='Summer Dresses']")
            }
