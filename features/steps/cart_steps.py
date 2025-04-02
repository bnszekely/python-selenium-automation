from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify correct message is shown')
def verify_correct_message(context):
    context.app.cart_page.verify_correct_message()


@then('Verify notebook is in cart')
def verify_notebook_in_cart_text(context):
    context.app.cart_page.verify_notebook_in_cart_text()


@then('Verify cart page opens')
def verify_cart_page_opens(context):
    context.app.cart_page.verify_cart_page_opens()