import logging
import os
import shutil
import time

from selenium import webdriver


def before_all(context):
    # print("Executing before all")
    print("")

def before_feature(context, feature):
    # print("Before feature\n")
    # Create logger
    # TODO - http://stackoverflow.com/questions/6386698/using-the-logging-python-class-to-write-to-a-file
    context.logger = logging.getLogger('seleniumframework_tests')
    hdlr = logging.FileHandler('./seleniumframework_tests.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    context.logger.addHandler(hdlr)
    context.logger.setLevel(logging.DEBUG)

# Scenario level objects are popped off context when scenario exits

def before_scenario(context, scenario):
    # print("User data:", context.config.userdata)

    # behave -D ENV=test

    if 'ENV' in context.config.userdata.keys():
        if context.config.userdata['ENV'] is None:
            BROWSER = 'dev'
        else:
            BROWSER = context.config.userdata['ENV']
    else:
        BROWSER = 'dev'

    if BROWSER == 'dev':
        context.base_url = "http://localhost:3000"
        webdriver_url = "http://127.0.0.1:4444/wd/hub"
    elif BROWSER == 'test':
        context.base_url = "http://contact_list_app:3000"
        webdriver_url = "http://selenium_hub:4444/wd/hub"
    elif BROWSER == 'prod':
        context.base_url = "http://167.99.137.138:3000"
        webdriver_url = "http://selenium_hub:4444/wd/hub"

    # behave -D BROWSER=chrome
    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is None:
            BROWSER = 'chrome'
        else:
            BROWSER = context.config.userdata['BROWSER']
    else:
        BROWSER = 'chrome'
    # For some reason, python doesn't have switch case -
    # http://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
    if BROWSER == 'chrome':
        #context.browser = webdriver.Chrome()
        context.browser = webdriver.Remote(
            command_executor=webdriver_url,
            desired_capabilities={
                'browserName': 'chrome',
                'chromeOptions': {
                    'args': [
                        "--start-maximized",
                        "disable-extensions",
                        "test-type"
                    ]
                }
            }
        )
    elif BROWSER == 'firefox':
        #context.browser = webdriver.Firefox()
        context.browser = webdriver.Remote(
            command_executor=webdriver_url,
            desired_capabilities={
                'browserName': 'firefox'
            }
        )
    else:
        print("Browser you entered:", BROWSER, "is invalid value")

    context.browser.maximize_window()
    # print("Before scenario\n")


def after_scenario(context, scenario):
    # print("scenario status" + scenario.status)
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")
    context.browser.quit()

def after_feature(context, feature):
    # print("\nAfter Feature")
    print("")

def after_all(context):
    # print("User data:", context.config.userdata)
    # behave -D ARCHIVE=Yes
    if 'ARCHIVE' in context.config.userdata.keys():
        if os.path.exists("failed_scenarios_screenshots"):
            os.rmdir("failed_scenarios_screenshots")
            os.makedirs("failed_scenarios_screenshots")
        if context.config.userdata['ARCHIVE'] == "Yes":
            shutil.make_archive(
                time.strftime("%d_%m_%Y"),
                'zip',
                "failed_scenarios_screenshots")
            #os.rmdir("failed_scenarios_screenshots")
            print("Executing after all")


