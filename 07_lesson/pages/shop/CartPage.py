from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(4)

    def click_checkout_button(self):
        self._driver.find_element(By.ID, 'checkout').click()