from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = driver.find_element(By.CSS_SELECTOR, '[name=first-name]')

last_name = driver.find_element(By.CSS_SELECTOR, '[name=last-name]')

address = driver.find_element(By.CSS_SELECTOR, '[name=address]')

email = driver.find_element(By.CSS_SELECTOR, '[name=e-mail]')

phone_number = driver.find_element(By.CSS_SELECTOR, '[name=phone]')

zip_code = driver.find_element(By.CSS_SELECTOR, '[name=zip-code]')

city = driver.find_element(By.CSS_SELECTOR, '[name=city]')

country = driver.find_element(By.CSS_SELECTOR, '[name=country]')

job_position = driver.find_element(By.CSS_SELECTOR, '[name=job-position]')

company = driver.find_element(By.CSS_SELECTOR, '[name=company]')

first_name.send_keys('Иван')

last_name.send_keys('Петров')

address.send_keys('Ленина, 55-3')

email.send_keys('test@skypro.com')

phone_number.send_keys('+7985899998787')

city.send_keys('Москва')

country.send_keys('Россия')

job_position.send_keys('QA')

company.send_keys('SkyPro')

submit = driver.find_element(By.CSS_SELECTOR, '[type=submit]')

submit.click()

def test_zipcode_color():
    assert 'alert-danger' in driver.find_element(By.ID, 'zip-code').get_attribute('class')

def test_another_colors():
    assert 'alert-success' in driver.find_element(By.ID, 'first-name').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'last-name').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'address').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'city').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'country').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'e-mail').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'phone').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'job-position').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'company').get_attribute('class')
