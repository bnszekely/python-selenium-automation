from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")
    SIGN_IN_BUTTON = (By.XPATH, "//a[@id='account-sign-in']")


    def search(self, text):
        print(f'Searching for {text}')
        self.input_text(text, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def click_sign_in_button(self):
        self.click(*self.SIGN_IN_BUTTON)