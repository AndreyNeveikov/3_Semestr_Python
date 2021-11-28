"""
4. Создать базовый класс «транспортное средство» и
производные классы «Автомобиль», «Велосипед», «Повозка».
Подсчитать время и стоимость перевозки пассажиров
и грузов каждым транспортным средством.
"""

class Vehicle():
    # Класс по созданию транспортного средства
    def __init__(self, make, speed, space, cost_per_km, cargo):
        # Инициализация атрибутов транспорта
        self.make = make
        self.speed = speed
        self.space = space
        self.cost_per_km = cost_per_km
        self.cargo = cargo

    def Veh_description(self):
        # Возвращаем описание транспорта
        V_desc = 'Производитель: ' + str(self.make) + ' \nМаксимальная скорость: ' \
        + str(self.speed) + ' км/ч \nПосадочных мест: ' + str(self.space) + ' \nЦена киломера пути: ' \
        + str(self.cost_per_km) + ' копеек' + ' \nВместимость груза: ' + str(self.cargo) + ' кг\n'
        return V_desc.lower()

class Car(Vehicle):
    #Аспекты для автомобиля
    def __init__(self, make, speed, space, cost_per_km, cargo):
        # Инициализация атрибутов класса родителя
        super().__init__(make, speed, space, cost_per_km, cargo)
        self.fatigue = 9 # Часов без отдыха можно проехать
        self.trailer = 1500
        self.gas_tank = 75

    def fuel_calculator(self, gas_per_km):
        # Считает сколько километров можно проехать без дозаправки
        length = self.gas_tank / gas_per_km * 100
        return length

    def way(self, car, length, people, cargo):
        if (cargo % (car.cargo + car.trailer)) == 0:
            way = (cargo // (car.cargo + car.trailer))
        else:
            way = (cargo // (car.cargo + car.trailer)) + 1

        if way <= people / car.space:
            if (people % car.space) == 0:
                way = (people // car.space)
            else:
                way = (people // car.space) + 1

        if way == 1:
            S = length
        else:
            S = 2 * (length * way) - length
        return S

class ElecrticCar(Car):
    #Аспекты для электрического автомобиля
    def __init__(self, make, speed, space, cost_per_km, cargo):
        # Инициализация атрибутов класса родителя
        super().__init__(make, speed, space, cost_per_km, cargo)
        self.fatigue = Car.fuel_calculator(self, 1) / self.speed
        self.trailer = 1500
        self.gas_tank = 75

    def autopilot(self, gas_per_km):
        print ('С автопилотом можно ехать без перерыва ' + self.fatigue +' часов')

class Bicycle(Vehicle):
    # Аспекты для велосипеда
    def __init__(self, make, speed, space = 1, cost_per_km = 0, cargo = 15):
        # Инициализация атрибутов класса родителя
        super().__init__(make, speed, space, cost_per_km, cargo)
        self.fatigue = 5

    # Переопределение родительского метода
    def Veh_description(self):
        # Возвращаем описание транспорта
        V_desc = 'Производитель: ' + str(self.make) + ' \nМаксимальная скорость: ' + str(self.speed) \
        + ' \nВместимость груза: ' + str(self.cargo) + ' кг\n'
        print('На данном виде транспорта доступно одно место, а цена одного километра - 0 копеек')
        return V_desc.lower()

    def way(self, bicycle, length, people, cargo):
        if (cargo % bicycle.cargo) == 0:
            way = (cargo // bicycle.cargo)
        else:
            way = (cargo // bicycle.cargo) + 1

        if way <= people / bicycle.space:
            if (people % bicycle.space) == 0:
                way = (people // bicycle.space)
            else:
                way = (people // bicycle.space) + 1

        if way == 1:
            S = length
        else:
            S = 2 * (length * way) - length
        return S

class Carriage(Vehicle):
    # Аспекты для повозки
    def __init__(self, make, speed, space, cost_per_km, cargo):
        # Инициализация атрибутов класса родителя
        super().__init__(make, speed, space, cost_per_km, cargo)
        self.fatigue = 7
        self.outside_sead = 1

    def way(self, carriage, length, people, cargo):
        if (cargo % carriage.cargo) == 0:
            way = (cargo // carriage.cargo)
        else:
            way = (cargo // carriage.cargo) + 1

        if way <= people / carriage.space + carriage.outside_sead:
            if (people % (carriage.space + carriage.outside_sead)) == 0:
                way = (people // (carriage.space + carriage.outside_sead))
            else:
                way = (people // (carriage.space + carriage.outside_sead)) + 1

        if way == 1:
            S = length
        else:
            S = 2 * (length * way) - length
        return S

def calculate_car(Type, S, cost_per_km, fuel_calculator, speed, fatigue):
    cost = cost_per_km * S
    breaks = int(S / fuel_calculator) + int((S / speed) / fatigue)
    print('\n' + Type + 'потребуется проехать ' + str(S) + ' км \nЭто будет стоить ' + str(cost) +
          ' копеек \nНадо сделать ' + str(breaks) + ' перерывов на отдых')

def calculate_notcar(Type, S, cost_per_km, speed, fatigue):
    cost = cost_per_km * S
    breaks = int((S / speed) / fatigue)
    print('\n' + Type + ' потребуется проехать ' + str(S) + ' км \nЭто будет стоить ' + str(cost) +
          ' копеек \nНадо сделать ' + str(breaks) + ' перерывов на отдых')


car = Car('BMW', 270, 7, 20, 1000)
ecar = ElecrticCar('Tesla X', 300, 7, 5, 1500)
bicycle = Bicycle('LTD', 30, 1, 0, 15)
carriage = Carriage('Roga and Kopita', 40, 4, 5, 700)

length = int(input('Введи растояние которое нужно проехать: '))
people = int(input('Введи сколько человек надо перевезти: '))
cargo = int(input('Введи сколько груза надо перевезти: '))



calculate_car('Машине', car.way(car, length, people, cargo), car.cost_per_km, car.fuel_calculator(5), car.speed, car.fatigue)

calculate_car('Электромобилю', car.way(ecar, length, people, cargo), ecar.cost_per_km, ecar.fuel_calculator(5), ecar.speed, ecar.fatigue)

calculate_notcar('Повозке', carriage.way(carriage, length, people, cargo), carriage.cost_per_km, carriage.speed, carriage.fatigue)

calculate_notcar('Велосипеду', bicycle.way(bicycle, length, people, cargo), bicycle.cost_per_km, bicycle.speed, bicycle.fatigue)