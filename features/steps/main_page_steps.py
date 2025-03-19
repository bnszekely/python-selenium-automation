from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")
SIGN_IN_BUTTON = (By.CSS_SELECTOR, '.sc-43f80224-3')
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
TARGET_CIRCLE = (By.XPATH, "//a[@data-test='@web/GlobalHeader/UtilityHeader/TargetCircle']")
TARGET_HELP = (By.XPATH, "//div[@aria-label='Target Help']")

@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when('Click on Cart Icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN_BUTTON).click()
    sleep(6)


@when('Search for {search_word}')
def search_product(context, search_word):
    sleep(2)
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()


@when('Click on Target Circle')
def click_target_circle(context):
    context.driver.find_element(*TARGET_CIRCLE).click()


@when('Click Target Help')
def click_target_help(context):
    sleep(6)
    context.driver.find_element(*TARGET_HELP).click()



