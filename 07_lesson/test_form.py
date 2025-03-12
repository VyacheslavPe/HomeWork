from pages.FormPage import FormPage
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_colors():
    browser = webdriver.Chrome()
    form_page = FormPage(browser)
    form_page.set_first_name('Иван')
    form_page.set_last_name('Иванов')
    form_page.set_address('Ленина, 55-3')
    form_page.set_email('test@skypro.com')
    form_page.set_phone_number('+7985899998787')
    form_page.set_zip_code('')
    form_page.set_city('Москва')
    form_page.set_country('Россия')
    form_page.set_job_position('QA')
    form_page.set_company('SkyPro')
    form_page.click_submit()
    assert 'alert-danger' in browser.find_element(By.ID, 'zip-code').get_attribute('class')
    assert 'alert-success' in browser.find_element(By.ID, 'first-name').get_attribute('class')
    assert 'alert-success' in browser.find_element(By.ID, 'last-name').get_attribute('class')
    assert 'alert-success' in browser.find_element(By.ID, 'address').get_attribute('class')
    assert 'alert-success' in browser.find_element(By.ID, 'city').get_attribute('class')
    assert 'alert-success' in browser.find_element(By.ID, 'country').get_attribute('class')
    assert 'alert-success' in browser.find_element(By.ID, 'e-mail').get_attribute('class')
    assert 'alert-success' in browser.find_element(By.ID, 'phone').get_attribute('class')
    assert 'alert-success' in browser.find_element(By.ID, 'job-position').get_attribute('class')
    assert 'alert-success' in browser.find_element(By.ID, 'company').get_attribute('class')
    browser.quit()