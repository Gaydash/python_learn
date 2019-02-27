# first_name = 'Olga'
# last_name = "Gaydash"
user_info = {'first_name': 'Olga', 'last_name': "Gaydash"}
print(user_info)
print(user_info['first_name'])

# lists
phones = ["iPhone", "Samsung", 'Xiomi']
print(phones)
print(len(phones))
phones.append('iPhone 6')
print(phones)
print(phones.count('iPhone 6'))
print(phones[1])

print(phones[1:3])
print(phones[-1])
print(phones[:2])
print(phones.index("Samsung"))
phones.sort()
print(phones)
print("Samsung" in phones)

print(phones)
del phones[2]
print(phones)
phones.remove('Xiomi')
print(phones)

print ('Home work: ')
list = [3, 5, 7, 9, 10.5]
print(list)
list.append('Python')
print(list)
print(len(list))
#print('first element: ' + list[0], 'last element: ' + list[-1],
#      'elements from 2 to 2: ' + list[1:4])
print(list[0], list[-1], list[1:4])
list.remove('Python')
print(list)

# dictionaries
