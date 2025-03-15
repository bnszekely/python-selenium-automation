from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_EMPTY_MSG = (By.XPATH, "//div[@data-test='boxEmptyMsg']")


@then('Verify correct message is shown')
def verify_correct_message(context):
    actual_text = context.driver.find_element(*CART_EMPTY_MSG).text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


@then('Verify notebook is in cart')
def verify_notebook_in_cart_text(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[contains(text(),'Notebook')]").text
    expected_text = 'notebook'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'