from selenium.webdriver.common.by import By

class InventoryPage:
    """
    Этот класс содержит методы для работы со страницей товаров
    """
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(4)

    def add_to_cart_backpacck(self):
        """
        Этот метод ищет на странице кнопку "Add to cart" для товара "Backpack" и кликает на неё
        """
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

    def add_to_cart_tshirt(self):
        """
        Этот метод ищет на странице кнопку "Add to cart" для товара "T-shirt" и кликает на неё
        """
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()

    def add_to_cart_onesie(self):
        """
        Этот метод ищет на странице кнопку "Add to cart" для товара "Onesie" и кликает на неё
        """
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    def click_cart_button(self):
        """
        Этот метод ищет на странице кнопку корзины и кликает на неё
        """
        self._driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()