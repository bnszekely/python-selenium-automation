from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    RESULTS_MSG = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_TO_CART_BTN = (By.XPATH, "//button[@data-test='chooseOptionsButton']")
    SIDE_MENU_ADD_TO_CART_BTN = (By.XPATH, "//button[@data-test='shippingButton']")
    VIEW_CART = (By.XPATH, "//a[@href='/cart']")

    def verify_search_results(self, expected_text):
        self.verify_partial_text(expected_text, *self.RESULTS_MSG)

    def verify_results_url(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)

    def click_add_to_cart_btn(self):
        self.click(*self.ADD_TO_CART_BTN)

    def confirm_add_to_cart_from_side_menu(self):
        self.click(*self.SIDE_MENU_ADD_TO_CART_BTN)

    def click_view_cart_side_menu(self):
        self.click(*self.VIEW_CART)