from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.drawer import Drawer
from pages.sign_in_page import SignInPage
from pages.target_app_page import TargetAppPage
from pages.target_terms_conditions_page import TargetTermsConditions

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.drawer = Drawer(driver)
        self.sign_in_page = SignInPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.target_terms_conditions_page = TargetTermsConditions(driver)