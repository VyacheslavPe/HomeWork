from selenium.webdriver.common.by import By

class CheckOut1Page:
    """
    Этот класс содержит методы для работы с первой страницей оформления заказа
    """
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(4)

    def set_first_name(self, value : str):
        """
        Этот метод ищет на странице поле "First name" и вводит в него значение value
        """
        self._driver.find_element(By.ID, 'first-name').send_keys(value)

    def set_last_name(self, value : str):
        """
        Этот метод ищет на странице поле "Last name" и вводит в него значение value
        """
        self._driver.find_element(By.ID, 'last-name').send_keys(value)

    def set_postal_code(self, value : str):
        """
        Этот метод ищет на странице поле "Postal code" и вводит в него значение value
        """
        self._driver.find_element(By.ID, 'postal-code').send_keys(value)

    def click_continue(self):
        """
        Этот метод ищет на странице кнопку "Continue" и кликает на неё
        """
        self._driver.find_element(By.ID, 'continue').click()