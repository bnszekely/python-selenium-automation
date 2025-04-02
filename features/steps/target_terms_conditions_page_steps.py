from behave import given, when, then
from time import sleep


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()
    sleep(4)

@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.target_terms_conditions_page.verify_tc_opened()


@then('User can close new window')
def close_page(context):
    context.app.base_page.close()


@then('User can switch back to original window')
def switch_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)
