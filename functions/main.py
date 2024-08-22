import functions_framework
from bs4 import BeautifulSoup
import requests
import time
import re
from firebase_admin import firestore, initialize_app
from utils import camel_case


@functions_framework.http
def run_sync(request=None):
    page = 1
    initialize_app()
    db = firestore.client()
    start = time.time()

    while True:

        print(f"looking for page {page}")
        url = f'https://www.goodsmile.info/en/products/category/nendoroid_series/page/{page}'
        response = requests.get(url, timeout=30)

        if "Sorry! This page doesn't exist!" in response.text:
            print("page not found, stopping")
            break

        print("creating soup")
        soup = BeautifulSoup(response.text, features="html.parser")

        print("soup created, fetching items")
        items = soup.find_all('div', {"class": ["nendoroid", "nendoroiddoll"]})

        print(f"found {len(items)} items")

        for i in items:
            nendoroid = {
                "link": i.find('a').attrs.get("href"),
                "img": i.find('img').attrs.get("data-original").replace('//', 'https://'),
                "name": i.find('span', {'class': 'hitTtl'}).text.replace('\n', '').replace(':', ''),
                "update_time": firestore.SERVER_TIMESTAMP
            }
            
            try:
                nendoroid['id'] = i.find('span', {'class': 'hitNum'}).text.replace('\n', '')
                match_number = re.search("[0-9][0-9]*", nendoroid['id'])

                if match_number:
                    nendoroid['int_id'] = int(match_number.group())
                else:
                    nendoroid['int_id'] = 999_999

            except AttributeError:
                if '/' in nendoroid.get('name'):
                    print(f"SKIPPING {nendoroid.get('name')}")
                    continue
                nendoroid['id'] = camel_case(nendoroid['name'])

            db.collection("nendoroids_v2").document(nendoroid['id']).set(nendoroid)
            print(f"pushed {nendoroid.get('name')} in firestore")
        
        page += 1

    print(f"all done in {time.time() - start}")
    return "all done"
