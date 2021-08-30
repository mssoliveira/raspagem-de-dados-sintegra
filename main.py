import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import json

# Pegar conteudo do HTML

url = "http://www.sefaz.ba.gov.br/Sintegra/sintegra.asp?estado=BA"

# Instancia o Chorme e abre
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--lang=pr-BR')
chrome_options.add_argument('--disable-notifications')
driver = webdriver.Chrome(executable_path=os.getcwd() + os.sep + 'chromedriver.exe', options=chrome_options)
driver.get(url)
time.sleep(10)


driver.find_element_by_xpath(
    ""
)
element = driver.find_element_by_xpath("table")
html_content = element.get_attribute("outerHTML")

print(html_content)


#Tratar dados recebidos







driver.quit()

