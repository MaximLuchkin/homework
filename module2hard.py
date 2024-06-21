number_left = list(range(3, 21))
number1 = list(range(1, 21))
number2 = list(range(1, 21))
number_right = []
for i in number_left:
    password_number = []
    for k in number1:
        if k >= i:
            break
        for j in number2:
            if j >= i:
                break
            elif j <= k:
                continue
            multiple_of_number = True
            summa_numbers = k + j
            if i % summa_numbers != 0:
                multiple_of_number = False
                continue
            elif multiple_of_number:
                next_password = str(k) + str(j)
                password_number.append(next_password)
    number_right.append(password_number)


def all_passwords():
    for i in number_right:
        print(*i)


all_passwords()
