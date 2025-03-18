from selenium.webdriver.common.by import By

class CalcPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)

    def set_delay(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('1')

    def click_seven(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()

    def click_plus(self):
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()

    def click_eight(self):
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()

    def click_equals(self):
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()