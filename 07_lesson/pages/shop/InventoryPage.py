from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(4)

    def add_to_cart_backpacck(self):
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

    def add_to_cart_tshirt(self):
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()

    def add_to_cart_onesie(self):
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    def click_cart_button(self):
        self._driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()