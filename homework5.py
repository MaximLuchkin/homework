immutable_var = 'Coconut', 11, True, 22.2
print(immutable_var)

#immutable_var[0] = orange
print(type(immutable_var))
#Переменная immutable_var принадлежит к неизменяемому типу данных 'tuple'
#Tак же, в кортеже нет изменяемых типов данных, по типу 'list'

mutable_list = ['Coconut', 11, True, 22.2]
print(mutable_list)
mutable_list[0:4] = ['Orange', 22, False, 11.1]
print(mutable_list)