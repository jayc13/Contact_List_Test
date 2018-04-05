from behave import *
from features.lib.pages import *
import time

use_step_matcher("re")


@when("I open Contact List website")
def step_impl(context):
    page = CreatePage(context)
    page.visit()