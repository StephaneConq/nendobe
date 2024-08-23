import requests
from bs4 import BeautifulSoup

def search_prices(doll_name: str):
    r = requests.post('https://www.play-asia.com/ajax/product_filter',
                  data={
                    "pf_s_q": doll_name,
                    "ppage": 36
                  }
                )

    soup = BeautifulSoup(r.text, features="html.parser")

    container = soup.find('div', {"id": "n_pf_holder"})

    if not container:
        return []

    results = container.find_all('div', {"class": "p_prev"})

    prices = []
    for result in results:
        price = result.find('span', {'class': 'jsd'})
        if price:
            prices.append(price.text)
        
    return prices