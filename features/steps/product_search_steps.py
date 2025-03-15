from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


RESULTS_MSG = (By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
VIEW_CART = (By.XPATH, "//a[contains(text(),'View cart')]")


@when('Click add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(6)


@when('Click View cart from Side Menu')
def click_view_cart_side_menu(context):
    context.driver.find_element(*VIEW_CART).click()
    sleep(6)


@then('Verify correct search results shown for tea')
def verify_found_results_text(context):
    actual_text = context.driver.find_element(*RESULTS_MSG).text
    expected_text = 'tea'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'

