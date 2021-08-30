import requests
from lxml import html

cookies = {
    'ASPSESSIONIDQSDQRASS': 'KKDHELFCMODKHMEJCJEGDGAA',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://www.sefaz.ba.gov.br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://www.sefaz.ba.gov.br/Sintegra/sintegra.asp?estado=BA',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = {
  'txt_CNPJ': '06859330000113',
  'txt_IE': '',
  'EstadoSelecionado': 'da Bahia',
  'SiglaEstadoSelecionado': 'BA'
}

response = requests.post('http://www.sefaz.ba.gov.br/Sintegra/Result.asp', headers=headers, cookies=cookies, data=data, verify=False)

resposta = response.text


page = html.fromstring(resposta)
lista = [atributo.text for atributo in page.xpath('//td//font')]



print(lista)