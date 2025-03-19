from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


then@('Verify UI elements are present')
def verify_ui_elements(context):

