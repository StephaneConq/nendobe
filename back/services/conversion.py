import requests
import os

def get_conversion():
    r = requests.get(f'https://api.exchangeratesapi.io/v1/latest?access_key={os.environ.get("CONVERSION_API")}&base=EUR&symbols=JPY')
    res = r.json()
    return res.get('rates').get('JPY')