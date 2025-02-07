from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import  sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('http://the-internet.herokuapp.com/login')

input_username = driver.find_element(By.ID , 'username')
input_password = driver.find_element(By.ID , 'password')
button_login = driver.find_element(By.CLASS_NAME, 'fa-sign-in')

input_username.send_keys('tomsmith')
input_password.send_keys('SuperSecretPassword!')
button_login.click()

