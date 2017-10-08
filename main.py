"""
THE FARMER - GOOD SEEDING FOR A BETTER FUTURE

This application will consulte several indexes and returning their values. The data that will be store is:
- Date and time
- Name of the Index
- Font
- Valeu

The index that will be check is:
- Bovespa - ok
- Petr4 stock
- Netshoes stock
- Criptocurrencies (Etherium, Bitcoin)
- Dolar


v.1
The first version will store data in a csv file. After that, it'll send an email to alex.zwir@cartaoelo.com.br


"""
import requests, bs4
from datetime import datetime

uol = "https://economia.uol.com.br/cotacoes/bolsas/bvsp-bovespa/"
bmfbovespa = "http://www.bmfbovespa.com.br/pt_br/servicos/market-data/cotacoes/"
advfn = "https://br.advfn.com/bolsa-de-valores/bovespa/ibovespa-IBOV/cotacao"
sites_financeiros = [uol,bmfbovespa,advfn]

targets_sites = {"advfn":"#quoteElementPiece6"}


def naming_sites(site):
    partes = site.split(".")
    return(partes[1])

def conecting_site(site):
    response = requests.get(site)
    response_code = response.status_code
    name_of_the_site = naming_sites(site)
    if response_code == 200:
        print(name_of_the_site," --> is ready to go!")
        return(response)
    else:
        print(response_code.status_code)

def price_of_financial_asset(site):
    response = conecting_site(site)
    text_raw = bs4.BeautifulSoup(response.text, "html.parser")
    for site, target in targets_sites.items():
        asset_price = text_raw.select(target)
        site_price = [site,asset_price[0].getText()]
        return(site_price)

def storing_assets_value(asset,value,font):
    datet =
    return


def main():
    bovespa_index = price_of_financial_asset(sites_financeiros[2])
    print("A última cotação da bovespa é:", bovespa_index[1],".Fonte:",bovespa_index[0].upper())

main()
