my_dict = {'Sergey': 1992, 'Anton': 1993, 'Maxim': 1995}
print(my_dict)
print(my_dict.get('Anton'))
print(my_dict.get('Masha'))
my_dict.update({'Vasay': 1990, 'Egor': 1994})
print(my_dict.pop('Sergey'))
print(my_dict)

my_set = [3, 6, 3, 3, 'pop', 6, True, 6, 'pop', 3, 6]
my_set = set(my_set)
print(my_set)
my_set.add('banana')
my_set.add(44.4)
my_set.discard(3)
print(my_set)
