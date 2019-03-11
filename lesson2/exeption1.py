num_one = input('Please input first number: ')
num_two = input('Please input second number: ')

def get_summ(num_one, num_two):
    try:
        sum = int(num_one)+int(num_two)
        return sum
    except ValueError:
        return 'Input number'

result = get_summ(num_one, num_two)
print(result)