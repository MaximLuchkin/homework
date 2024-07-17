class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        start_floor = 0
        while True:
            start_floor += 1
            if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует')
                break
            elif start_floor == new_floor:
                print(start_floor)
                break
            else:
                print(start_floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors
        else:
           return 'Ошибка'

    def __lt__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors
        else:
            return 'Ошибка'

    def __le__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors
        else:
            return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors
        else:
            return 'Ошибка'

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors
        else:
            return 'Ошибка'

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors
        else:
            return 'Ошибка'

    def __add__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors = value + self.number_of_floors
        return self

    def __iadd__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors = value + self.number_of_floors
        return self

    def __sub__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors = self.number_of_floors - value
        return self

    def __rsub__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors = value - self.number_of_floors
        return self

    def __mul__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors = self.number_of_floors * value
        return self

    def __floordiv__(self, value):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors = self.number_of_floors // value
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2)  # __eq__
h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)
h1 += 10  # __iadd__
print(h1)
h2 = 10 + h2  # __radd__
print(h2)
print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
h1 = h1 - 5  # __sub__
print(h1)
h1 = 45 - h1  # __rsub__
print(h1)
h1 = h1 * 2  # __mul__
print(h1)
h1 = h1 // 2  # __floordiv__
print(h1)
