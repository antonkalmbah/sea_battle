string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(float, list_of_strings)) # cписок чисел

print(sum(list_of_numbers[::-1])) # sum() вычисляет сумму элементов списка

list_new = list_of_numbers.append(sum(list_of_numbers))

print(list_new)