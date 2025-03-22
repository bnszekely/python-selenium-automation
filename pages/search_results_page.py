from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    RESULTS_MSG = (By.XPATH, "//div[@data-test='lp-resultsCount']")

    def verify_search_results(self, expected_text):
        actual_text = self.find_element(*self.RESULTS_MSG).text
        assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'