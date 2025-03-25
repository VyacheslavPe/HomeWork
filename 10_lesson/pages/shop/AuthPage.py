from selenium.webdriver.common.by import By

class AuthPage:
    """
    Этот класс содержит методы для работы со страницей авторизации
    """
    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(4)

    def set_login(self, value : str):
        """
        Этот метод ищет на странице поле Login и вводит в него значение value
        """
        self._driver.find_element(By.ID, 'user-name').send_keys(value)

    def set_password(self, value : str):
        """
        Этот метод ищет на странице поле Password и вводит в него значение value
        """
        self._driver.find_element(By.ID, 'password').send_keys(value)

    def click_login_button(self):
        """
        Этот метод ищет на странице кнопку Login и кликает на неё
        """
        self._driver.find_element(By.ID, 'login-button').click()