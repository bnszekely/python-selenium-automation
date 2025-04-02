from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_TEXT = (By.CSS_SELECTOR, '.styles_ndsHeading__HcGpD.jpudjh')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#username')
    TC_LINK = (By.XPATH, "//a[@aria-label='terms & conditions - opens in a new window']")


    def verify_sign_in_form_opens(self):
        self.verify_partial_text('Sign into', *self.SIGN_IN_TEXT)

    #def input_email(self, text):
   #     print(f'Entering email {text}')
     #   self.input_text(text: 'sandroezxjh@jeremytunnell.net', *self.EMAIL_FIELD)

    def click_on_target_tc_link(self):
        self.click(*self.TC_LINK)