from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


RESULTS_MSG = (By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_TO_CART_BTN = (By.XPATH, "//button[@data-test='chooseOptionsButton']")
SIDE_MENU_ADD_TO_CART_BTN = (By.XPATH, "//button[@data-test='shippingButton']")
VIEW_CART = (By.XPATH, "//a[@href='/cart']")


@when('Click add to cart button')
def click_add_to_cart(context):
    sleep(10)
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when('Confirm add to cart from side menu')
def confirm_add_to_cart_from_side_menu(context):
    sleep(6)
    context.driver.find_element(*SIDE_MENU_ADD_TO_CART_BTN).click()


@when('Click View cart from Side Menu')
def click_view_cart_side_menu(context):
    sleep(6)
    context.driver.find_element(*VIEW_CART).click()


@then('Verify correct search results shown for tea')
def verify_found_results_text(context):
    actual_text = context.driver.find_element(*RESULTS_MSG).text
    expected_text = 'tea'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


