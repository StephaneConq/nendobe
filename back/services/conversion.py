import requests
import os

def get_conversion(currency = None):
    r = requests.get(f'https://api.exchangeratesapi.io/v1/latest?access_key={os.environ.get("CONVERSION_API")}&base=EUR&symbols=JPY,USD')
    res = r.json()

    if currency:
        return res.get('rates').get(currency)

    return res.get('rates')