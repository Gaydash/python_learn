phones = ["iPhone", "Samsung", 'Xiomi']

product = {
    'name': "iPhone",
    'stock': 5,
    'price': 15000.5
}

print(product)
product['stock']=10
product['memory']=64
print(product)
print(product['name'])
print(product.get('discount', 15))
print(product)
del product['stock']
print(product)

product['recomend'] = phones
print(product)
print(product['recomend'][1])
product['recomend'].append('LG')
print(product)

stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'recomended': ['Samsung Galaxy S10', 'iPhone Xs']},
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000.5},
]
print(stock)
print(stock[0]['name'])
stock[0]['price']=stock[0]['price']+3500
print(stock[0])
stock[0]['stock'] += 5
print(stock[0])
print(stock[0]['recomended'][1])

print('Home work about dictionaries: ')
wether = {"city": "Москва", "temperature": '20'}
print(wether['city'])
print(type(wether['temperature']))
wether['temperature'] = int(wether['temperature'])
print(type(wether['temperature']))
wether['temperature'] -= 5
print(wether['temperature'])
print(wether)
print(wether.get('country', 'Россия'))
wether['date']='27.05.2019'
print(wether)
print(len(wether))