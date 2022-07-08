#SELENIUM
#pip install selenium

#GOOGLE CHROME - driver
#https://sites.google.com/chromium.org/driver/

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path='./chromedriver.exe')
browser.get('https://www.google.com')

#DIMINUIR TEMPO DE DIGITAÇÃO
def digitar(elemento, texto):
    for caracter in texto:
        elemento.send_key(caracter)
        time.sleep(0.5)

#REALIZANDO BUSCA
search = browser.find_element_by_name('q')
#search.send_keys('André')
digitar(search, "Anne Karoline")
#PRESSIONA O ENTER
search.send_keys(Keys.ENTER)