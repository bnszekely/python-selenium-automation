from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SIGN_IN_TEXT = (By.CSS_SELECTOR, '.styles_ndsHeading__HcGpD.jpudjh')
EMAIL_FIELD = (By.CSS_SELECTOR, '#username')
PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
SIGN_IN_BUTTON = (By.CSS_SELECTOR, '#login')


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    print('Original window:', context.original_window)


@when('Click on Target terms and conditions link')
def click_on_target_tc_link(context):
    context.app.sign_in_page.click_on_target_tc_link()

@when('Input {email} and {password} on SignIn Page')



@when('Click Sign In on SignIn Page')



@then('Verify Sign In Form Opens')
def verify_sign_in_form_opens(context):
    context.app.sign_in_page.verify_sign_in_form_opens()