from selenium.webdriver.common.by import By
from pages.base_page import Page

class Drawer(Page):
    SIGN_IN = (By.XPATH, "//button[@data-test='accountNav-signIn']")

    def click_sign_in_drawer(self):
        self.click(*self.SIGN_IN)