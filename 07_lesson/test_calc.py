from pages.CalcPage import CalcPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calc():
    browser = webdriver.Chrome()
    calc_page = CalcPage(browser)
    calc_page.set_delay(45)
    calc_page.click_seven()
    calc_page.click_plus()
    calc_page.click_eight()
    calc_page.click_equals()

    assert WebDriverWait(browser, 45).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15')
    )

    browser.quit()
