from pages.CalcPage import CalcPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.title('Проверка корректной работы задержки калькулятора')
@allure.description('Складываем два числа и проверяем что сумма выводится через время указанное в поле задержки')
@allure.feature("Задержка")
@allure.severity('S3')
def test_calc():
    with allure.step("Открываем страницу https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html в новом браузере"):
        browser = webdriver.Chrome()
        calc_page = CalcPage(browser)
    with allure.step("Вводим в поле 'Delay' значение 45"):
        calc_page.set_delay('45')
    with allure.step("Нажимаем кнопку 7 на калькуляторе"):
        calc_page.click_seven()
    with allure.step("Нажимаем кнопку + на калькуляторе"):
        calc_page.click_plus()
    with allure.step("Нажимаем кнопку 8 на калькуляторе"):
        calc_page.click_eight()
    with allure.step("Нажимаем кнопку = на калькуляторе"):
        calc_page.click_equals()

    with allure.step("Проверяем что калькулятор выдал правильное значение 15"):
        assert WebDriverWait(browser, 45).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15')
        )

    browser.quit()
