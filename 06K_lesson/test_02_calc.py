from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

delay = driver.find_element(By.CSS_SELECTOR, '#delay')
delay.clear()
delay.send_keys('45')

seven = driver.find_element(By.XPATH, '//span[text()="7"]')
plus = driver.find_element(By.XPATH, '//span[text()="+"]')
eight = driver.find_element(By.XPATH, '//span[text()="8"]')
equals = driver.find_element(By.XPATH, '//span[text()="="]')

seven.click()
plus.click()
eight.click()
equals.click()

def test_time():
    assert WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15')
    )
