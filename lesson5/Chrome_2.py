from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

button = driver.find_element(By.CLASS_NAME, 'btn-primary')

sleep(1)

button.click()

sleep(2)