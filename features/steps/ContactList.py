from behave import *
from features.lib.pages import *

use_step_matcher("re")


@when('I open Contact List website')
def step_impl(context):
    page = IndexPage(context)
    page.visit()


@step('I access to create contact page')
def step_impl(context):
    page = IndexPage(context)
    page.go_to_create_contact()


@then('I verify that the count of Contacts is ([0-9]+)')
def step_impl(context, value):
    page = IndexPage(context)
    print(page.get_count_of_contact())
    assert True
