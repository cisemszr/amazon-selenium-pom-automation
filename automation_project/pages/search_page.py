from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(BasePage):

    PAGE_2_BOX = (By.CSS_SELECTOR, "a.s-pagination-item[aria-label='2 sayfasına git']")
    SEARCHED_PRODUCT_ELEMENT = (By.XPATH, "//div[@data-component-type='s-search-result' and not(contains(@class, 'AdHolder'))]")

    def verify_product_titles_contain_keyword(self, keyword):
        """
        Verify that each real product contains the given keyword.
        :param keyword: Keyword to check in each product title.
        :return: None
        """
        products = self.driver.find_elements(*self.SEARCHED_PRODUCT_ELEMENT)
        for product in products:
            assert keyword.lower() in product.text.lower(), f"Error: Expected product '{keyword}', but found '{product.text}'!"

    def go_to_page_2(self):
        """
        Navigates to the second page by clicking on the page 2 button
        :return:None
        """
        self.wait.until(EC.visibility_of_element_located(self.PAGE_2_BOX))
        self.click(*self.PAGE_2_BOX)

    def validate_page_number(self, page):
        """
        Validates whether the current page number matches the expected page
        :param page: The expected page number 2
        :return: None
        """
        current_url = self.driver.current_url
        expected_page_number = f"page={page}"
        assert expected_page_number in current_url, f"Not on page {page}."

    def select_product_by_index(self, index):
        """
        Selects the product in the specified order and clicks on it
        :param index: The order of the product to be selected in the list
        :return: None
        """
        selected_product_locator = (By.XPATH, f"//div[@data-index='{index}']")
        self.click(*selected_product_locator)