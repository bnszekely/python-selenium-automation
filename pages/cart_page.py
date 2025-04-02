from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
   CART_EMPTY_MSG = (By.XPATH, "//div[@data-test='boxEmptyMsg']")
   CART_NTBK_MSG = (By.XPATH, "//div[contains(text(),'Notebook')]")

   def verify_correct_message(self):
       self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

   def verify_cart_page_opens(self):
       self.verify_url(f'{self.base_url}cart')

   def verify_notebook_in_cart_text(self):
        self.verify_partial_text('Notebook', *self.CART_NTBK_MSG)