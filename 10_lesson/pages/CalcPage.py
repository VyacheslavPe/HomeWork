from selenium.webdriver.common.by import By

class CalcPage:
    """
    Этот класс содержит методы для работы с калькулятором на сайте
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)

    def set_delay(self, value : str):
        """
        Этот метод ищет на странице поле "Delay" и вводит в него значение value
        """
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(value)

    def click_seven(self):
        """
        Этот метод ищет на странице кнопку 7 и нажимает на неё
        """
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()

    def click_plus(self):
        """
        Этот метод ищет на странице кнопку + и нажимает на неё
        """
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()

    def click_eight(self):
        """
        Этот метод ищет на странице кнопку 8 и нажимает на неё
        """
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()

    def click_equals(self):
        """
        Этот метод ищет на странице кнопку = и нажимает на неё
        """
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()