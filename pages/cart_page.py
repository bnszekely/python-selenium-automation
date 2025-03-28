from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
   CART_EMPTY_MSG = (By.XPATH, "//div[@data-test='boxEmptyMsg']")


   def verify_correct_message(self):
       self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)