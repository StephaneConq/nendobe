import requests
import os
from services.conversion import get_conversion


_client_id = os.environ.get('EBAY_CLIENT_ID')
_client_secret = os.environ.get('EBAY_CLIENT_SECRET')
_conversion_rate_usd = None


def auth():
    url = 'https://api.ebay.com/identity/v1/oauth2/token'
    r = requests.post(url,
                        headers={
                            'Content-Type': 'application/x-www-form-urlencoded',
                        },
                        data={
                            "grant_type":  "client_credentials",
                            "scope": "https://api.ebay.com/oauth/api_scope"
                        },
                        auth=(_client_id, _client_secret)
                    )
    res = r.json()
    return res.get('access_token')

def search_prices(name: str):
    access_token = auth()

    r = requests.get(f'https://api.ebay.com/buy/browse/v1/item_summary/search?q={name}&limit=50&offset=0',
                    headers={
                        "Authorization": f"Bearer {access_token}"
                    })
    
    res = r.json()

    conversion_rate_usd = get_conversion('USD')

    all_items = []

    for item in res.get('itemSummaries'):
        all_items.append(
            _create_item(item, conversion_rate_usd)
        )

    return all_items

def _create_item(ebay_item, conversion_rate_usd):
    return {
        "name": ebay_item.get('title'),
        "url": ebay_item.get('itemHref'),
        "image": ebay_item.get('image', {}).get('imageUrl'),
        "price": float(ebay_item.get('price').get('value')) / conversion_rate_usd
    }