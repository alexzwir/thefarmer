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


v.1
The first version will store data in a csv file. After that, it'll send an email to alex.zwir@cartaoelo.com.br


"""
import requests, bs4

uol = "https://economia.uol.com.br/cotacoes/bolsas/bvsp-bovespa/"
bmfbovespa = "http://www.bmfbovespa.com.br/pt_br/servicos/market-data/cotacoes/"
advfn = "https://br.advfn.com/bolsa-de-valores/bovespa/ibovespa-IBOV/cotacao"
sites_financeiros = [uol,bmfbovespa,advfn]


def naming_sites(site):
    partes = site.split(".")
    return(partes[1])

def conecting_site(site):
    response = requests.get(site)
    response_code = response.status_code
    name_of_the_site = naming_sites(site)
    if response_code == 200:
        print(name_of_the_site," --> is ready to go!")
    else:
        print(response_code.status_code)


for site in sites_financeiros:
     conecting_site(site)



# text_raw = bs4.BeautifulSoup(response.text, "html.parser")
# #print(text_raw)
# preco_da_acao = text_raw.select(".PriceTextDown")
# print(len(preco_da_acao))
# for i in preco_da_acao:
#     print(i)
#
# preco_da_acao2 = text_raw.select("#quoteElementPiece6")
# print(len(preco_da_acao2))
# print(preco_da_acao2[0].getText())
#
#

#rint(preco_da_acao)
#print(preco_da_acao[0].getText())
