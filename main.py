"""
THE FARMER - GOOD SEEDING FOR A BETTER FUTURE

This application will consulte several indexes and returning their values. The data that will be store is:
- Date and time
- Name of the Index
- Font
- Valeu

The index that will be check is:
- Bovespa
- Petr4 stock
- Netshoes stock
- Criptocurrencies (Etherium, Bitcoin)
- Dolar
-

v.1
The first version will store data in a csv file. After that, it'll send an email to alex.zwir@cartaoelo.com.br


"""

import requests, bs4

url = "https://economia.uol.com.br/cotacoes/bolsas/bvsp-bovespa/"
response = requests.get(url)
#print(response.text[250:2000])

text_raw = bs4.BeautifulSoup(response.text,"html.parser")
#print(type(text_raw))
# print(text_raw)
preco_da_acao = text_raw.select("#price")
print(preco_da_acao)
#print(preco_da_acao[0].getText())
