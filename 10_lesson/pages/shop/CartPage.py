from selenium.webdriver.common.by import By

class CartPage:
    """
    Этот класс содержит методы для работы со страницей корзины
    """
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(4)

    def click_checkout_button(self):
        """
        Этот метод ищет на странице кнопку "Checkout" и кликает на неё
        """
        self._driver.find_element(By.ID, 'checkout').click()