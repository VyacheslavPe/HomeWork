from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, 'user-name').clear()
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').clear()
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()

driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

driver.find_element(By.ID, 'checkout').click()

driver.find_element(By.ID, 'first-name').clear()
driver.find_element(By.ID, 'first-name').send_keys('Vyacheslav')
driver.find_element(By.ID, 'last-name').clear()
driver.find_element(By.ID, 'last-name').send_keys('Pereskokov')
driver.find_element(By.ID, 'postal-code').clear()
driver.find_element(By.ID, 'postal-code').send_keys('111000')

driver.find_element(By.ID, 'continue').click()

total = driver.find_element(By.CLASS_NAME, 'summary_total_label').text

print(total)

driver.quit()

def test_total():
    assert 'Total: $58.29' == total
