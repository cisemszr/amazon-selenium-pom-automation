from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    CART_TITLE = (By.XPATH, "//h2[@id='sc-active-items-header']")
    CART_PRODUCT_TITLE = (By.CSS_SELECTOR, "span.a-truncate-cut")
    DELETE_BUTTON = (By.XPATH, "//span[@class='a-icon a-icon-small-trash']")
    DELETED_MESSAGE =(By.XPATH, "(//div[@class='a-padding-medium'])[1]")

    def is_on_cart_page(self):
        """
        Verifies whether the user is on the cart page.
        :return: None
        """
        cart_title_element = self.wait.until(EC.presence_of_element_located(self.CART_TITLE))
        assert cart_title_element, "You are not on the cart page!"

    def is_correct_product_in_cart(self, expected_product_title):
        """
        Verifies whether the correct product is in the cart.
        :param expected_product_title: The title of the expected product.
        :return: None
        """
        cart_product_title_element = self.wait.until(EC.visibility_of_element_located(self.CART_PRODUCT_TITLE))
        cart_product_title = cart_product_title_element.text.strip()
        assert expected_product_title in cart_product_title, f"Error: Expected product '{expected_product_title}', but found '{cart_product_title}' in the cart!"

    def click_delete_button(self):
        """
        Clicks the delete button to remove the product from the cart
        :return: None
        """
        self.wait.until(EC.presence_of_element_located(self.DELETE_BUTTON)).click()

    def check_deleted_message(self):
        """
        Verifies if the success message is displayed after the product is deleted
        :return:None
        """
        message = self.wait.until(EC.presence_of_element_located(self.DELETED_MESSAGE))
        message.is_displayed()