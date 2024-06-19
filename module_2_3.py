my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
for i, number in enumerate(my_list):
    if my_list[i] < 0:
        break
    elif my_list[i] == 0:
        continue
    elif my_list[i] == int(my_list[-1]):
        print(my_list[i])
        break
    print(my_list[i])
