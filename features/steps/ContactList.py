from behave import *
from features.lib.pages import *
import time

use_step_matcher("re")


@given('I open Contact List website')
def step_impl(context):
    page = IndexPage(context)
    page.visit()
    assert page.get_title_text() == "Contact List"


@step('I access to create contact page')
def step_impl(context):
    page = IndexPage(context)
    page.go_to_create_contact()
    assert page.get_title_text() == "New Contact"


@step('I delete one contact')
def step_impl(context):
    page = IndexPage(context)
    page.delete_contact_by_index(0)
    time.sleep() 


@step('I go to edit one contact')
def step_impl(context):
    page = IndexPage(context)
    page.edit_contact_by_index(0)


@step('I create a new Contact with random values')
def step_impl(context):
    page = CreatePage(context)
    five_digits = str(page.rand_x_digit_num(5, False))
    first_name = "Javier_%s" % five_digits
    last_name = "Caballero_%s" % five_digits
    mobile = "+54 %s" % str(page.rand_x_digit_num(10, False))
    email = "javier_%s@caballero.com" % five_digits
    page.fill_contact_form(first_name, last_name, mobile, email)
    page.save_contact_form()
    page = ShowPage(context)
    assert page.get_title_text() == "View Contact"


@step('I edit a current Contact with random values')
def step_impl(context):
    page = EditPage(context)
    five_digits = str(page.rand_x_digit_num(5, False))
    first_name = "Javier_%s" % five_digits
    last_name = "Caballero_%s" % five_digits
    mobile = "+54 %s" % str(page.rand_x_digit_num(10, False))
    email = "javier_%s@caballero.com" % five_digits
    page.fill_contact_form(first_name, last_name, mobile, email)
    page.save_contact_form()
    page = ShowPage(context)
    assert page.get_title_text() == "View Contact"


@step('I back to home page from a show contact page')
def step_impl(context):
    page = ShowPage(context)
    assert page.get_title_text() == "View Contact"
    page.back_to_index_page()
    page = IndexPage(context)
    assert page.get_title_text() == "Contact List"


@step('I verify that exist a least 1 contact')
def step_impl(context):
	page = IndexPage(context)
	assert page.get_count_of_contact() > 0


@step('I verify that the count of Contacts is ([0-9]+)')
def step_impl(context, value):
	value = int(value)
	page = IndexPage(context)
	assert page.get_count_of_contact() == value
	if value == 0:
		assert page.is_no_contact_label_present()
