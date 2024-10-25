import json


def load_categories():
    with open('data/categories.json', encoding='utf-8') as f:
        return json.load(f)


def load_products(q=None):
    with open('data/products.json', encoding='utf-8') as p:
        products = json.load(p)

        if q:
            products = [p for p in products if p['name'].find(q) >= 0]

        return products
