from selenium.webdriver.common.by import By

class CheckOut2Page:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(4)

    def get_total(self):
        return self._driver.find_element(By.CLASS_NAME, 'summary_total_label').text