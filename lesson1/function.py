price = 100
discount = 5

price_with_discount = price - price * discount/ 100

print(price_with_discount)

def discounted(price, discount, max_discount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
#    if max_discount > 99:
#        raise ValueError('Max discount cant be more 99')
    if discount >= max_discount:
       price_with_discount=price
    else:
        price_with_discount = price - price * discount / 100
#   print(price_with_discount)
    return price_with_discount


print(discounted(200, 500, 100))
print(discounted(800, 80))
print(discounted(20, 10))

product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000}
product['price_discounted'] = discounted(product['price'], product['discount'])

print(product)

def get_summ(one, two, delimiter='&'):
    one1 = str(one)
    two1 = str(two)
    result = one1.upper() + delimiter + two1.upper()
    print(result)

get_summ('Learn', 'python', '@')
