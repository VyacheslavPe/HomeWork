from selenium import webdriver
from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self,driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)

    def set_first_name(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '[name=first-name]').send_keys(value)

    def set_last_name(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '[name=last-name]').send_keys(value)

    def set_address(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '[name=address]').send_keys(value)

    def set_email(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '[name=e-mail]').send_keys(value)

    def set_phone_number(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '[name=phone]').send_keys(value)

    def set_zip_code(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '[name=zip-code]').send_keys(value)

    def set_city(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '[name=city]').send_keys(value)

    def set_country(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '[name=country]').send_keys(value)

    def set_job_position(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '[name=job-position]').send_keys(value)

    def set_company(self, value):
        self._driver.find_element(By.CSS_SELECTOR, '[name=company]').send_keys(value)

    def click_submit(self):
        self._driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()
