L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))

a = 5
b = 3+2

print(id(a))
print(id(b))

string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(float, list_of_strings)) # cписок чисел

print(sum(list_of_numbers[::-1])) # sum() вычисляет сумму элементов списка

list_new = list_of_numbers.append(sum(list_of_numbers))

print(list_new)

print(list_new)