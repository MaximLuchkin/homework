class Vehicle:
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__modele = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return print(f'Модель: {self.__modele}')

    def get_horsepower(self):
        return print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        return print(f'Цвет: {self.__color}')

    def print_info(self):
        return self.get_model(), self.get_horsepower(), self.get_color(), print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        for i in self._COLOR_VARIANTS:
            if new_color.lower() == i.lower():
                self.__color = new_color
                return
            else:
                continue
        return print(f'"Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()