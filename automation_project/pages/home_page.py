from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HomePage(BasePage):

    LOGO = (By.XPATH, "//a[@id='nav-logo-sprites']")
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    EXPECTED_TITLE = ("Amazon.com.tr: Elektronik, bilgisayar, akıllı telefon, kitap, oyuncak, yapı market, ev,"
                      " mutfak, oyun konsolları ürünleri ve daha fazlası için internet alışveriş sitesi")

    def is_on_homepage(self):
        """
        Checks if the current page title matches the homepage title
        :return: If the current page title matches the expected title, it returns True; otherwise, it returns False
        """
        return self.EXPECTED_TITLE == self.get_title()

    def is_search_text_box_displayed(self):
        """
        Checks if the search text box is displayed on the page
        :return: True if the search text box is visible, otherwise False
        """
        try:
            search_text_box = self.wait_for_visible(*self.SEARCH_BOX)
            return search_text_box.is_displayed()
        except TimeoutException:
            return False

    def search_for_item(self, product_name):
        """
        Searches for a product in the inventory
        :param str product_name: The name of the product to search for
        :return: None
        """
        search_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_BOX))
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.ENTER)

    def click_to_amazon_logo(self):
        """
        Clicks on the Amazon logo to navigate to the homepage
        """
        self.driver.find_element(*self.LOGO).click()