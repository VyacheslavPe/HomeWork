from selenium.webdriver.common.by import By

class CheckOut2Page:
    """
    Этот класс содержит методы для работы со второй страницей оформления заказа
    """
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(4)

    def get_total(self) -> str:
        """
        Этот метод ищет на странице строку с общей суммой заказа и возвращает её
        """
        return self._driver.find_element(By.CLASS_NAME, 'summary_total_label').text