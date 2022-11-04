from typing import List, Dict
import requests

def post_products_to_store(
    products_list: List[Dict[str, str]],
    store: str
    ):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    payload = { "store": store, "products_list": products_list }
    print(payload)
    url = 'https://backend-gpti.herokuapp.com/api/v1/update-products'
    response = requests.post(url, json=payload, headers=headers)
    print(response)
