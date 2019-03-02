string1 = input('Введите строку1: ')
string2 = input('Введите вторую строку: ')

def comperisong_string(str1, str2):
    if (type(str1) is not str) and (type(str2) is not str):
        return '0'
    elif str1==str2:
        return '1'
    elif len(str1) > len(str2):
        return '2'
    elif str2 == 'learn':
        return '3'
    else:
        return 'Вы ввели значение не предусмотренное заданием'

result = comperisong_string(string1, string2)
print(result)

result = comperisong_string(int(input('Введите строку1: ')), int(input('Введите вторую строку: ')))
print(result)

result = comperisong_string(input('Введите строку1: '), input('Введите вторую строку: '))
print(result)

result = comperisong_string(input('Введите строку1: '), input('Введите вторую строку: '))
print(result)

