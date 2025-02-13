from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
WebDriverWait(driver, 60).until(
    EC.presence_of_all_elements_located((By.ID, 'landscape'))
)
image_container = driver.find_element(By.ID, 'image-container')
images = image_container.find_elements(By.TAG_NAME, 'img')
print(images[2].get_attribute('src'))
