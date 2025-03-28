from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_NTBK_MSG = (By.XPATH, "//div[contains(text(),'Notebook')]")


@then('Verify correct message is shown')
def verify_correct_message(context):
    context.app.cart_page.verify_correct_message()


@then('Verify notebook is in cart')
def verify_notebook_in_cart_text(context):
    actual_text = context.driver.find_element(*CART_NTBK_MSG).text
    expected_text = 'notebook'
    assert expected_text in actual_text.lower(), f'Error. Text {expected_text} not in {actual_text}'