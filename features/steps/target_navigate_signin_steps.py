from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '.sc-43f80224-3').click()
sleep(6)


@when('Click Sign In from Right Side Menu')
def click_sign_in_from_right_side_menu(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(6)


@then('Verify Sign In Form Opens')
def verify_sign_in_form_opens(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '.styles_ndsHeading__HcGpD.jpudjh').text
    expected_text = 'Sign into your Target account'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'