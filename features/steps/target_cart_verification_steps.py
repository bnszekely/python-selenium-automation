from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when('Click on Cart Icon')
def click_cart_icon(context):
    context.driver.find_element(By.XPATH, ("//a[@data-test='@web/CartLink']")).click()


@then('Verify correct message is shown')
def verify_correct_message(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'