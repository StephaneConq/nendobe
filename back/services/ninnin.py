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
        print("Container with results not found for ninnin")
        return []
    
    conversion_rate = get_conversion()

    products = container.find_all('li', {'class': 'general_block_card'})

    prices = []
    for p in products:
        price = p.find('span', {'class': 'price'})

        if price:
            price_value = float(price.text.replace('¥', '').replace(',', ''))
            
            if conversion_rate:
                price_value = price_value / conversion_rate
            
            prices.append(price_value)
    
    return prices