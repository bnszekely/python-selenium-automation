from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SIGN_IN_BUTTON_RSM = (By.XPATH, "//button[@data-test='accountNav-signIn']")
SIGN_IN_TEXT = (By.CSS_SELECTOR, '.styles_ndsHeading__HcGpD.jpudjh')


@when('Click Sign In from Right Side Menu')
def click_sign_in_from_right_side_menu(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON_RSM))
    context.driver.find_element(*SIGN_IN_BUTTON_RSM).click()


@then('Verify Sign In Form Opens')
def verify_sign_in_form_opens(context):
    actual_text = context.driver.find_element(*SIGN_IN_TEXT).text
    expected_text = 'Sign into your Target account'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'