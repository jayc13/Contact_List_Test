from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback
import time
import random


class BasePage(object):

    def __init__(self, context):
        self.base_url = context.base_url
        self.browser = context.browser
        self.timeout = 30

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def find_elements(self, *loc):
        return self.browser.find_elements(*loc)

    def accept_alert(self):
        try:

            WebDriverWait(self.browser, self.timeout).until(EC.alert_is_present())

            alert = self.browser.switch_to.alert

            alert.accept()
        except TimeoutException:
            print("no alert")

    def dismiss_alert(self):
        Alert(self.browser).dismiss()

    def visit(self, url=None):
        if not url:
            url = self.base_url
        self.browser.get(url)

    def hover(self, element):
            ActionChains(self.browser).move_to_element(element).perform()
            # I don't like this but hover is sensitive and needs some sleep time
            time.sleep(5)

    def rand_x_digit_num(self, x, leading_zeroes=True):
        """Return an X digit number, leading_zeroes returns a string, otherwise int"""
        if not leading_zeroes:
            # wrap with str() for uniform results
            return random.randint(10**(x-1), 10**x-1)  
        else:
            if x > 6000:
                return ''.join([str(random.randint(0, 9)) for i in xrange(x)])
            else:
                return '{0:0{x}d}'.format(random.randint(0, 10**x-1), x=x)

    def __getattr__(self, what):
        try:
            if what in self.locator_dictionary.keys():
                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.presence_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException,StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.visibility_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()
                # I could have returned element, however because of lazy loading, I am seeking the element before return
                return self.find_element(*self.locator_dictionary[what])
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(what)

    def method_missing(self, what):
        print("No %s here!" % what)
