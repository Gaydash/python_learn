age = int(input('Введите свой возраст: '))

def define_age(age):
    if age < 6:
        return "Вы ходите в садик"
        # print("Вы ходите в садик")
    elif age < 16:
        return "Вы ходите в школу"
    elif age < 23:
        return "Вы ходите в институт"
    else:
        return  "Вы ходите на работу"

result = define_age(age)
print(result)