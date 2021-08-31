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
consulta_cnpj = '06859330000113'

#funcão de adicionar os dados e consultar
def dados(navegador, cnpj):
    input = navegador.find_element_by_xpath("//html//body//form//table//tbody//tr//td//input")
    input.send_keys(cnpj) 
    consulta = navegador.find_element_by_name("Submit")
    consulta.click()  

# Instancia o Chorme e abre
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--lang=pr-BR')
chrome_options.add_argument('--disable-notifications')
driver = webdriver.Chrome(executable_path=os.getcwd() + os.sep + 'chromedriver.exe', options=chrome_options)
driver.get(url)
#fazendo consulta dos dados
dados(driver, consulta_cnpj)

element = driver.find_element_by_xpath("//body")
html_content = element.get_attribute("outerHTML")

#Tratar dados recebidos
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

#estruturando conteudo recebido em um data frame
df_full = pd.read_html( str(table) )[0].head(10)

print(df_full)








#fecha o navegador 
driver.quit()