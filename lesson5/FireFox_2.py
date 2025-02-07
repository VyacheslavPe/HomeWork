from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import  sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('http://the-internet.herokuapp.com/inputs')

input_bar = driver.find_element(By.TAG_NAME , 'input')

input_bar.send_keys('1000')
sleep(1)
input_bar.clear()
sleep(1)
input_bar.send_keys('999')

