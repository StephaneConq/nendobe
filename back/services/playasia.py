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


def create_item(result):
    price = result.find('span', {'class': 'jsd'})
    image = result.find('img', {'class': 'unvl'})
    name = result.find('div', {'class': 'p_prev_n'})
    link = result.find('a')

    return {
        "name": name.text,
        "url": f"https://www.play-asia.com/{link.attrs.get('href')}",
        "image": f"https:{image.attrs.get('data-src').strip()}",
        "price": price.text
    }