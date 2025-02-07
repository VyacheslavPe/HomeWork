from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

add_button = driver.find_element(By.CSS_SELECTOR, "button")
for i in range(0,5):
    add_button.click()

delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
print(len(delete_buttons))