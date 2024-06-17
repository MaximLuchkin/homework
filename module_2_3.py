my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
for i, number in enumerate(my_list):
        my_list_int = my_list[i]
        if my_list_int < 0:
            break
        if my_list_int == int(my_list[-1]):
            print(my_list_int)
            break
        print(my_list_int)

