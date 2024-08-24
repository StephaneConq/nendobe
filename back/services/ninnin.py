import requests
from bs4 import BeautifulSoup
from services.conversion import get_conversion

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"

def search_prices(name: str):
    r = requests.get(
        f"https://www.nin-nin-game.com/en/search?orderway=desc&search_query={name}",
        headers={
            "User-Agent": user_agent
        }
    )
    soup = BeautifulSoup(r.text, 'html.parser')
    container = soup.find('ul', {'class': 'product-grid'})

    if not container:
        print(f"Container with results not found for ninnin for nendoroid {name}")
        return []
    
    conversion_rate = get_conversion('JPY')

    products = container.find_all('li', {'class': 'general_block_card'})

    prices = []
    for p in products:
        prices.append(create_item(p, conversion_rate))
    
    return prices

def create_item(product, conversion_rate):
    price = product.find('span', {'class': 'price'})
    price_value = None

    if price:
        price_value = float(price.text.replace('¥', '').replace(',', ''))
        
        if conversion_rate:
            price_value = price_value / conversion_rate

    link =  product.find('a', {'class': 'product-name'})

    image = product.find('div', {'class': 'product_image'}).find('img')

    return {
        "name": link.text.strip(),
        "url": link.attrs.get('href'),
        "image": image.attrs.get('src'),
        "price": price_value
    }