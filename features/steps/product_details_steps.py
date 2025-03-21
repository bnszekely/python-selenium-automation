from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product {product_id} page')
def open_target_product_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(10)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Charcoal Gray', 'Green', 'Light Gray', 'Navy Blue', 'Olive Green']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color', selected_color)

        selected_color = selected_color.split('\n') [1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match {actual_colors}'
