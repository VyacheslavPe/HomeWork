from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

text_box = driver.find_element(By.ID, 'newButtonName')

text_box.clear()

text_box.send_keys('SkyPro')

button = driver.find_element(By.ID, 'updatingButton')

button.click()

print(button.text)