from pages.FormPage import FormPage
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@allure.title('Проверка смены цвета выделения на красный при пустом поле')
@allure.description("Проверяем что поле 'Zip-code' становится красным если не заполнено и была нажата кнопка 'Submit'")
@allure.feature('Подсветка ошибки при заполнении')
@allure.severity('S4')
def test_colors():
    with allure.step("Открываем страницу https://bonigarcia.dev/selenium-webdriver-java/data-types.html в новом браузере"):
        browser = webdriver.Chrome()
        form_page = FormPage(browser)
    with allure.step("Вводим в поле 'First name' значение Иван"):
        form_page.set_first_name('Иван')
    with allure.step("Вводим в поле 'Last name' значение Иванов"):
        form_page.set_last_name('Иванов')
    with allure.step("Вводим в поле 'Address' значение 'Ленина, 55-3'"):
        form_page.set_address('Ленина, 55-3')
    with allure.step("Вводим в поле 'E-mail' значение 'test@skypro.com'"):
        form_page.set_email('test@skypro.com')
    with allure.step("Вводим в поле 'Phone number' значение '+7985899998787"):
        form_page.set_phone_number('+7985899998787')
    with allure.step("Оставляем поле Zip-code пустым"):
        form_page.set_zip_code('')
    with allure.step("Вводим в поле 'City' значение 'Москва'"):
        form_page.set_city('Москва')
    with allure.step("Вводим в поле 'Country' значение 'Россия'"):
        form_page.set_country('Россия')
    with allure.step("Вводим в поле 'Job-position' значение 'QA'"):
        form_page.set_job_position('QA')
    with allure.step("Вводим в поле 'Company' значение 'SkyPro'"):
        form_page.set_company('SkyPro')
    with allure.step("Нажимаем кнопку 'Submit'"):
        form_page.click_submit()

    with allure.step("Проверяем что поле Zip-code стало красным"):
        assert 'alert-danger' in browser.find_element(By.ID, 'zip-code').get_attribute('class')

    with allure.step("Проверяем что остальные поля стали зелёными"):
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