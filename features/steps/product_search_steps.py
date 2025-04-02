from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click add to cart button')
def click_add_to_cart(context):
    sleep(10)
    context.app.search_results_page.click_add_to_cart_btn()


@when('Confirm add to cart from side menu')
def confirm_add_to_cart_from_side_menu(context):
    sleep(6)
    context.app.search_results_page.confirm_add_to_cart_from_side_menu()


@when('Click View cart from Side Menu')
def click_view_cart_side_menu(context):
    sleep(6)
    context.app.search_results_page.click_view_cart_side_menu()


@then('Verify correct search results shown for {expected_text}')
def verify_found_results_text(context, expected_text):
    context.app.search_results_page.verify_search_results(expected_text)


@then('Verify {expected_text} in URL')
def verify_results_url(context, expected_text):
    context.app.search_results_page.verify_results_url(expected_text)