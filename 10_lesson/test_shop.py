from selenium import webdriver
from pages.shop.AuthPage import AuthPage
from pages.shop.InventoryPage import InventoryPage
from pages.shop.CartPage import CartPage
from pages.shop.CheckOut1Page import CheckOut1Page
from pages.shop.CheckOut2Page import CheckOut2Page
import allure

@allure.title('Smoke тест-кейс магазина')
@allure.description('Проверяем авторизацию, добавление в корзину, оформление заказ, подсчёт общей сумма заказа')
@allure.feature('Авторизация, Корзина, Оформление заказа')
@allure.severity('S2')
def test_shop():
    with allure.step("Открываем страницу https://www.saucedemo.com/"):
        browser = webdriver.Chrome()
        auth_page = AuthPage(browser)
    with allure.step("В поле Login вводим 'standard_user'"):
        auth_page.set_login('standard_user')
    with allure.step("В поле Password вводим 'secret_sauce'"):
        auth_page.set_password('secret_sauce')
    with allure.step("Нажимаем кнопку 'Login'"):
        auth_page.click_login_button()

    inventory_page = InventoryPage(browser)

    with allure.step("Добавляем в корзину 'Onesie'"):
        inventory_page.add_to_cart_onesie()
    with allure.step("Добавляем в корзину 'T-shirt'"):
        inventory_page.add_to_cart_tshirt()
    with allure.step("Добавляем в корзину 'Backpack'"):
        inventory_page.add_to_cart_backpacck()
    with allure.step("Нажимаем кнопку перехода в корзину"):
        inventory_page.click_cart_button()

    cart_page = CartPage(browser)

    with allure.step("Нажимаем кнопку перехода на первую страницу оформления заказа"):
        cart_page.click_checkout_button()

    check_out_1_page = CheckOut1Page(browser)

    with allure.step("В поле First name вводим 'Vyacheslav'"):
        check_out_1_page.set_first_name('Vyacheslav')
    with allure.step("В поле Last name вводим 'Pereskokov'"):
        check_out_1_page.set_last_name('Pereskokov')
    with allure.step("В поле Postal code вводим '111000'"):
        check_out_1_page.set_postal_code('111000')
    with allure.step("Нажимаем кнопку перехода на вторую страницу оформления заказа"):
        check_out_1_page.click_continue()

    check_out_2_page = CheckOut2Page(browser)

    with allure.step("Получаем значение общей суммы заказа"):
        total = check_out_2_page.get_total()

    with allure.step("Проверяем что общая сумма заказа рассчитана правильно"):
        assert 'Total: $58.29' == total

    browser.quit()

