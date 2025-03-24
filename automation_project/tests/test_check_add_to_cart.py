import logging
import unittest
from selenium import webdriver
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.search_page import SearchPage

class TestCheckAddToCart(unittest.TestCase):

    product = "Samsung"
    url = "https://www.amazon.com.tr/"
    page_number = 2
    product_index = 5

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        """logger settings"""
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        self.logger.addHandler(handler)

    """ 
        Test case is: 

        1. Go to https://www.amazon.com.tr/
        2. Verify that you are on the home page
        3. Type 'samsung' in the search field at the top of the screen and perform the search.
        4. Verify that there are results for Samsung on the page that opens.
        5. Click page 2 from the search results and verify that page 2 is currently displayed on the page that opens.
        6. Go to the product page 3 from the top.
        7. Verify that you are on the product page.
        8. Add the product to the cart.
        9. Verify that the product has been added to the cart.
        10. Go to the cart page.
        11. Verify that you are on the cart page and that the correct product has been added to the cart.
        12. Delete the product from the cart and verify that it has been deleted.
        13. Return to the home page and verify that it is on the home page.

    """

    def test_check_add_to_cart(self):

        """ This test aims to validate search, add to cart, and remove product actions on Amazon Turkey."""

        self.logger.info("1. Go to https://www.amazon.com.tr/")
        home_page = HomePage(self.driver)
        home_page.go_to_url(self.url)

        self.logger.info("2. Verify that you are on the home page")
        self.assertTrue(home_page.is_on_homepage(), "This is not homepage!")

        self.logger.info("3. Type 'samsung' in the search field at the top of the screen and perform the search.")
        self.assertTrue(home_page.is_search_text_box_displayed(), "Search results are not visible!")
        home_page.search_for_item(self.product)

        self.logger.info("4. Verify that there are results for Samsung on the page that opens.")
        search_page = SearchPage(self.driver)
        search_page.verify_product_titles_contain_keyword(self.product)

        self.logger.info("5. Click page 2 from the search results and verify that page 2 is currently displayed on the page that opens.")
        search_page.go_to_page_2()
        search_page.validate_page_number(self.page_number)

        self.logger.info("6. Go to the product page 3 from the top.")
        search_page.select_product_by_index(self.product_index)

        self.logger.info("7. Verify that you are on the product page.")
        product_page = ProductPage(self.driver)
        product_page.is_on_product_page()

        product_title = product_page.get_product_title()

        self.logger.info("8. Add the product to the cart.")
        product_page.add_product_to_cart()

        self.logger.info("9. Verify that the product has been added to the cart.")
        product_page.is_product_added_to_cart()

        self.logger.info("10. Go to the cart page.")
        product_page.go_to_cart_page()

        self.logger.info("11. Verify that you are on the cart page and that the correct product has been added to the cart.")
        cart_page = CartPage(self.driver)
        cart_page.is_on_cart_page()
        cart_page.is_correct_product_in_cart(product_title)

        self.logger.info("12. Delete the product from the cart and verify that it has been deleted.")
        cart_page.click_delete_button()
        cart_page.check_deleted_message()

        self.logger.info("13. Return to the home page and verify that it is on the home page.")
        home_page.click_to_amazon_logo()
        home_page.is_on_homepage()

    def tearDown(self):
        self.logger.info("Test end: Closing the browser.")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()