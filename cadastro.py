import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import json

# Pegar conteudo do HTML
url = "https://www.sefaz.ba.gov.br/scripts/cadastro/cadastroBa/consultaBa.asp"
consulta_cnpj = '06859330000113'

#funcão de adicionar os dados e consultar
def dados(navegador, cnpj):
    input = navegador.find_element_by_name("CGC")
    input.send_keys(cnpj)     
    consulta = navegador.find_element_by_name("B1")
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

#dados recebidos
element = driver.find_element_by_xpath("//body")
html_content = element.get_attribute("outerHTML")

#Tratar dados recebidos
soup = BeautifulSoup(html_content, 'html.parser')
#Tabela dos Dados da Empresa
table_dados_empresa = soup.find_all(id="Table6")
#Tabela das Informações Complementares
table_complementares = soup.find_all(id="Table7")
#estruturando conteudo recebido em um data frame
#1. consultando dados no cnpj
dados_empresa = pd.read_html(str(table_dados_empresa))[0].head(3)
#2. consultando dados no cnpj
dados_complementares = pd.read_html(str(table_complementares))[0].head(10)
#3. examinando dados 
salvar_01 = dados_empresa.to_dict('records')
salvar_02 = dados_complementares.to_dict('records')
#fecha o navegador 
driver.quit()

js = json.dumps(salvar_01, ensure_ascii=False)
fp = open('dadosempresa.json', 'w', encoding='utf-8')
fp.write(js)
fp.close()

js2 = json.dumps(salvar_02, ensure_ascii=False)
fp2 = open('dadoscomplementares.json', 'w', encoding='utf-8')
fp2.write(js2)
fp2.close()