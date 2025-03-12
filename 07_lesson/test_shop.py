from selenium import webdriver
from pages.shop.AuthPage import AuthPage
from pages.shop.InventoryPage import InventoryPage
from pages.shop.CartPage import CartPage
from pages.shop.CheckOut1Page import CheckOut1Page
from pages.shop.CheckOut2Page import CheckOut2Page

def test_shop():
    browser = webdriver.Chrome()
    auth_page = AuthPage(browser)
    auth_page.set_login('standard_user')
    auth_page.set_password('secret_sauce')
    auth_page.click_login_button()
    inventory_page = InventoryPage(browser)
    inventory_page.add_to_cart_onesie()
    inventory_page.add_to_cart_tshirt()
    inventory_page.add_to_cart_backpacck()
    inventory_page.click_cart_button()
    cart_page = CartPage(browser)
    cart_page.click_checkout_button()
    check_out_1_page = CheckOut1Page(browser)
    check_out_1_page.set_first_name('Vyacheslav')
    check_out_1_page.set_last_name('Pereskokov')
    check_out_1_page.set_postal_code('111000')
    check_out_1_page.click_continue()
    check_out_2_page = CheckOut2Page(browser)
    total = check_out_2_page.get_total()
    assert 'Total: $58.29' == total
    browser.quit()

