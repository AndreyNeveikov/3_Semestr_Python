"""
4. Создать базовый класс «транспортное средство» и
производные классы «Автомобиль», «Велосипед», «Повозка».
Подсчитать время и стоимость перевозки пассажиров
и грузов каждым транспортным средством.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
    Базовый класс «транспортное средство»
    """

    def __init__(self, make, speed, space, cost_per_km, lifting_capacity):
        """Инициализация атрибутов транспортного средства"""
        self.make = make
        self.speed = speed
        self.space = space
        self.cost_per_km = cost_per_km
        self.lifting_capacity = lifting_capacity

    @abstractmethod
    def veh_description(self):
        """Возвращаем описание транспорта"""

    @abstractmethod
    def calculated_distance(self, *args):
        """Считает расстояние, которое проедет транспорт"""


class Car(Vehicle):
    """Производный класс «Автомобиль»"""

    def __init__(self, make, speed, space, cost_per_km, lifting_capacity):
        super().__init__(make, speed, space, cost_per_km, lifting_capacity)
        self.fatigue = 9  # Столько часов без отдыха можно проехать
        self.trailer = 1500  # увеличивает максимальную грузоподъемность на константу
        self.gas_tank = 75  # Емкость бензобака

    def veh_description(self):
        print(
            f"""\nАвтомобиль производства: {self.make} \
            \nМаксимальная скорость: {self.speed} \
            \nКоличество мест {self.space} \
            \nЦена одного километра: {self.cost_per_km} копеек \
            \nГрузоподъемность: {self.lifting_capacity}\
            \nГрузоподъемность прицепа: {self.trailer} \
            \nЕмкость бензобака: {self.gas_tank}\
            \nЧасов подряд можно проехать: {self.fatigue}
        """
        )

    def fuel_calculator(self, gas_per_km):
        """Считает сколько километров можно проехать без дозаправки"""
        length = self.gas_tank / gas_per_km * 100
        return length

    def calculated_distance(self, length, people, lifting_capacity):
        if (lifting_capacity % (self.lifting_capacity + self.trailer)) == 0:
            way = (lifting_capacity // (self.lifting_capacity + self.trailer))
        else:
            way = (lifting_capacity // (self.lifting_capacity + self.trailer)) + 1

        if way <= people / self.space:
            if (people % self.space) == 0:
                way = (people // self.space)
            else:
                way = (people // self.space) + 1

        if way == 1:
            S = length
        else:
            S = 2 * (length * way) - length
        return S


class Bicycle(Vehicle):
    """Производный класс «Велосипед»"""

    def __init__(self, make, speed, space=1, cost_per_km=0, lifting_capacity=15):
        # Инициализация атрибутов класса родителя
        super().__init__(make, speed, space, cost_per_km, lifting_capacity)
        self.fatigue = 5

    # Переопределение родительского метода
    def veh_description(self):
        print(
            f"""\nВелосипед производства: {self.make} \
            \nМаксимальная скорость: {self.speed} \
            \nКоличество мест {self.space} \
            \nЦена одного километра: {self.cost_per_km} копеек \
            \nГрузоподъемность: {self.lifting_capacity}\
            \nЧасов подряд можно проехать: {self.fatigue}
        """
        )

    def calculated_distance(self, length, people, lifting_capacity):
        if (lifting_capacity % self.lifting_capacity) == 0:
            way = (lifting_capacity // self.lifting_capacity)
        else:
            way = (lifting_capacity // self.lifting_capacity) + 1

        if way <= people / self.space:
            if (people % self.space) == 0:
                way = (people // self.space)
            else:
                way = (people // self.space) + 1

        if way == 1:
            S = length
        else:
            S = 2 * (length * way) - length
        return S


class Carriage(Vehicle):
    """Производный класс «Повозка»"""

    def __init__(self, make, speed, space, cost_per_km, lifting_capacity):
        # Инициализация атрибутов класса родителя
        super().__init__(make, speed, space, cost_per_km, lifting_capacity)
        self.fatigue = 7
        self.outside_sead = 1

    def calculated_distance(self, length, people, lifting_capacity):
        if (lifting_capacity % self.lifting_capacity) == 0:
            way = (lifting_capacity // self.lifting_capacity)
        else:
            way = (lifting_capacity // self.lifting_capacity) + 1

        if way <= people / self.space + self.outside_sead:
            if (people % (self.space + self.outside_sead)) == 0:
                way = (people // (self.space + self.outside_sead))
            else:
                way = (people // (self.space + self.outside_sead)) + 1

        if way == 1:
            S = length
        else:
            S = 2 * (length * way) - length
        return S

    def veh_description(self):
        print(
            f"""\nПовозка производства: {self.make} \
            \nМаксимальная скорость: {self.speed} \
            \nКоличество мест {self.space} \
            \nЦена одного километра: {self.cost_per_km} копеек \
            \nГрузоподъемность: {self.lifting_capacity}\
            \nДополнительных мест снаружи {self.outside_sead} \
            \nЧасов подряд можно проехать: {self.fatigue}
        """
        )


class ElecrticCar(Car, Carriage):
    """Класс «Электромобиль»"""
    def __init__(self, make, speed, space, cost_per_km, lifting_capacity):
        # Инициализация атрибутов класса родителя
        super().__init__(make, speed, space, cost_per_km, lifting_capacity)
        self.fatigue = Car.fuel_calculator(self, 1) / self.speed
        self.outside_sead = 1
        self.trailer = 1500
        self.gas_tank = 75

    def autopilot(self, gas_per_km):
        print(f'С автопилотом можно ехать без перерыва {self.fatigue} часов')

    def calculated_distance(self, length, people, lifting_capacity):
        if (lifting_capacity % (self.lifting_capacity + self.trailer)) == 0:
            way = (lifting_capacity // (self.lifting_capacity + self.trailer))
        else:
            way = (lifting_capacity // (self.lifting_capacity + self.trailer)) + 1

        if way <= people / self.space + self.outside_sead:
            if (people % (self.space + self.outside_sead)) == 0:
                way = (people // (self.space + self.outside_sead))
            else:
                way = (people // (self.space + self.outside_sead)) + 1

        if way == 1:
            S = length
        else:
            S = 2 * (length * way) - length
        return S


def calculate_car(Type, S, cost_per_km, fuel_calculator, speed, fatigue):
    cost = cost_per_km * S
    breaks = int(S / fuel_calculator) + int((S / speed) / fatigue)
    print(
        f"""\n{Type} потребуется проехать {str(S)} км \
        \nЭто будет стоить  {str(cost)} копеек \
        \nНадо сделать {str(breaks)} перерывов на отдых"""
    )


def calculate_not_car(Type, S, cost_per_km, speed, fatigue):
    cost = cost_per_km * S
    breaks = int((S / speed) / fatigue)
    print(
        f"""\n{Type} потребуется проехать {str(S)} км \
            \nЭто будет стоить  {str(cost)} копеек \
            \nНадо сделать {str(breaks)} перерывов на отдых"""
    )


car = Car('BMW', 270, 7, 20, 1000)
ecar = ElecrticCar('Tesla X', 300, 7, 5, 1500)
bicycle = Bicycle('LTD', 30, 1, 0, 15)
carriage = Carriage('Roga and Kopita', 40, 4, 5, 700)

length = int(input('Введи растояние которое нужно проехать: '))
people = int(input('Введи сколько человек надо перевезти: '))
lifting_capacity = int(input('Введи сколько груза надо перевезти: '))

calculate_car(
    'Машине', car.calculated_distance(length, people, lifting_capacity),
    car.cost_per_km, car.fuel_calculator(5), car.speed, car.fatigue
)

calculate_car(
    'Электромобилю', car.calculated_distance(length, people, lifting_capacity),
    ecar.cost_per_km, ecar.fuel_calculator(5), ecar.speed, ecar.fatigue
)

calculate_not_car(
    'Повозке', carriage.calculated_distance(length, people, lifting_capacity),
    carriage.cost_per_km, carriage.speed, carriage.fatigue
)

calculate_not_car(
    'Велосипеду', bicycle.calculated_distance(length, people, lifting_capacity),
    bicycle.cost_per_km, bicycle.speed, bicycle.fatigue
)
