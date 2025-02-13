from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

driver.implicitly_wait(20)

button = driver.find_element(By.CLASS_NAME, 'btn-primary')

button.click()

success = driver.find_element(By.CLASS_NAME, 'bg-success')

print(success.text)



