from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

    PRODUCT_TITLE= (By.ID, "productTitle")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    CART_ICON_LOCATOR = (By.XPATH, "//a[@id='nav-cart']")
    CART_COUNT_LOCATOR = (By.CSS_SELECTOR, ".nav-cart-count")

    def is_on_product_page(self):
        """
        Validates if the current page is a product page by checking the page title
        or the presence of a specific element.
        :return: None
        """
        product_title_element = self.wait.until(EC.presence_of_element_located(self.PRODUCT_TITLE))
        assert product_title_element.text.lower().strip() in self.get_title().lower().strip(), "The product name could not be found in the page title!"

    def add_product_to_cart(self):
        """
        Clicks the 'Add to Cart' button to add a product to the cart.
        :return: None
        """
        self.click(*self.ADD_TO_CART_BUTTON)

    def is_product_added_to_cart(self):
        """
        Verifies that a product has been successfully
        added to the cart by checking the product
        count in the cart icon.
        :return: None
        """
        cart_count_element = self.wait.until(EC.presence_of_element_located(self.CART_COUNT_LOCATOR))
        while int(cart_count_element.text) == 0:
            self.wait.until(EC.presence_of_element_located(self.CART_COUNT_LOCATOR))
        assert int(cart_count_element.text) > 0, "Product was not added to the cart!"

    def go_to_cart_page(self):
        """
        Clicks on the cart icon to navigate to the cart page
        :return: None
        """
        self.click(*self.CART_ICON_LOCATOR)

    def get_product_title(self):
         """
         Retrieves the product title from the product page
         :return: The product title as a string
         """
         product_title_element = self.wait.until(EC.presence_of_element_located(self.PRODUCT_TITLE)).text
         return product_title_element