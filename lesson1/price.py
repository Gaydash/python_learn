def format_price (price):
    price = int(price)
    return f'Цена: {price} руб.'

p = format_price(56.24)
print(p)

def get_summ(one, two, delimiter='&'):
    one1 = str(one)
    two1 = str(two)
    result = one1.upper() + delimiter + two1.upper()
    print(result)

get_summ('Learn', 'python', '@')



