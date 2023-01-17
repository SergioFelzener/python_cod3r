from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print('Iniciando Robo .....\n')

browser = webdriver.Firefox()
browser.get('https://qa-01.receiv.it/html/new/login')
time.sleep(1.5)




