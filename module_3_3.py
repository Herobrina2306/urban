def print_params(a=1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(1, 5)
print_params('Я', 'люблю', 'отпуск')
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [True, 5, 'Urban']
values_dict = {'a': 'Bob', 'b': True, 'c': 15}

print_params(*values_list)
print_params(**values_dict)

values_list2 = [23, 'пара-па-парам']
print_params(*values_list2, 42)