from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


TARGET_CIRCLE = (By.XPATH, "//a[@data-test='@web/GlobalHeader/UtilityHeader/TargetCircle']")
TARGET_HELP = (By.XPATH, "//div[@aria-label='Target Help']")


@given('Open Target main page')
def open_target_main_page(context):
    context.app.main_page.open_main_page()


@when('Click on Cart Icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()


@when('Click Sign In')
def click_sign_in(context):
    context.app.header.click_sign_in_button()


@when('Click Sign In from Drawer')
def click_sign_in_drawer(context):
    sleep(2)
    context.app.drawer.click_sign_in_drawer()


@when('Search for {search_word}')
def search_product(context, search_word):
    sleep(2)
    context.app.header.search(search_word)


@when('Click on Target Circle')
def click_target_circle(context):
    context.driver.find_element(*TARGET_CIRCLE).click()


@when('Click Target Help')
def click_target_help(context):
    context.driver.wait.until(EC.visibility_of_element_located(TARGET_HELP))
    context.driver.find_element(*TARGET_HELP).click()



