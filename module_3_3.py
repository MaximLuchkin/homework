def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


value_list = [5, 'список', 'True']
value_dict = {'a': 8, 'b': 'словарь', 'c': False}
value_list2 = [2.1, True]

print_params(4, 2,1,)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*value_list)
print_params(**value_dict)
print_params(*value_list2, 42)