from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BENEFIT_CELLS = (By.CSS_SELECTOR, ".cell-item-content")


@then("Verify at least 10 benefit cells appear")
def ten_benefit_cells(context):
    actual_cells = context.driver.find_elements(*BENEFIT_CELLS)
    assert len(actual_cells) >= 10, f'Error. Expected at least 10 cells, got {len(actual_cells)}'