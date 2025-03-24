from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=20)
        self.action = ActionChains(driver)

    def go_to_url(self, url):
        """
        Navigates to the specified URL and handles cookie popups if necessary
        """
        self.driver.get(url)
        self.driver.refresh()
        self.accept_cookie_popup()

    def get_title(self):
        """
        Returns the title of the current page
        """
        return self.driver.title

    def accept_cookie_popup(self):
        """
        Accepts the cookie popup if it appears on the page
        """
        try:
            cookie_buttons = self.driver.find_element(By.ID, "sp-cc-accept")
            if cookie_buttons.is_displayed():
                cookie_buttons.click()
        except TimeoutException:
            print("The cookie pop-up could not be found.")

    def wait_for_clickable(self, by, locator, timeout=20):
        """
        Waits for an element to be clickable
        :param by: The locating strategy
        :param locator: locator of the element to find
        :param timeout: Maximum time you want to wait for the element
        :return: The WebElement if it becomes clickable within the timeout period
        """
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by,locator)))

    def click(self, by, locator):
        """
        Waits for an element to be clickable, moves to it and clicks on it
        :param by: The locating strategy
        :param locator: The locator string used to find the element
        :return: None
        """
        element = self.wait_for_clickable(by, locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()

    def wait_for_visible(self, by, locator, timeout=20):
        """
        Waits for an element to be visible
        :param by: The locating strategy
        :param locator: locator of the element to find
        :param timeout: Maximum time you want to wait for the element
        :return: The WebElement if it becomes visible within the timeout period
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by,locator)))