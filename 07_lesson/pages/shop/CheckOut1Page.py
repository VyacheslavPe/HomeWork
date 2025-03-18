from selenium.webdriver.common.by import By

class CheckOut1Page:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(4)

    def set_first_name(self, value):
        self._driver.find_element(By.ID, 'first-name').send_keys(value)

    def set_last_name(self, value):
        self._driver.find_element(By.ID, 'last-name').send_keys(value)

    def set_postal_code(self, value):
        self._driver.find_element(By.ID, 'postal-code').send_keys(value)

    def click_continue(self):
        self._driver.find_element(By.ID, 'continue').click()