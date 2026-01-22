import requests

api_url = 'https://fakestoreapi.com/products'

response = requests.get(api_url)

Products = []
Total_products = 0
Average_price = 0

if response.status_code == 200:
    data = response.json()
    for product in data:
        Products.append({
            "title": product["title"],
            "category": product["category"],
            "price": product["price"]
        })
    Total_products = len(Products)
    Average_price = sum(product["price"] for product in Products) / len(Products)
else:
    print(f"Error: {response.status_code}")
    

print(
    '''Products: %s
    Total products: %s
    Average price: %s''' % (Products, Total_products, Average_price)
    )

