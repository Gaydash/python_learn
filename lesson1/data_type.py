a = 'Привет'
b = 'мир'
c = '{} {}!'.format(a, b)
print(c)

user = 'Оля'
e = f'Привет {user}'
print(e)

a1 = 'Hello'.upper()
print(a1)
b1 = ' Olga'.lower()
print(b1)
c1 = (a1 + b1).capitalize()
print(c, len(c1))

a2 = 'pr3v3t olga'
b2 = a2.strip()
c2 = a2.replace('3', 'e')
print(a2, b2, c2)

a3 = 'learn.python.ru'
print(a3.split('.'))
print(type(a3))

name = input('please input your name ')
age = input('how old are you ')
year = 2019 - int(age)
print(name, type(name), year)
