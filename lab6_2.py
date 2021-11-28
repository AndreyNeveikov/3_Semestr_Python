"""
4.  Реализовать класс «Человек», включающий в себя имя, фамилию, отчество,
год рождения и методы, позволяющие изменять/получать значения этих полей.
Реализовать производные классы:
    «Предприниматель» - содержит номер лицензии, адрес регистрации,
УНН, данные о налоговых платежах (массив пар вида <дата, сумма>).
    «Турист» - содержит данные паспорта(строка), данные о пересечении границы
в виде массива пар <дата, страна>.
    «Челнок» (производный от 2 и 3) – добавляется массив строк – список адресов,
по которым покупается товар. Классы должны содержать методы доступа и изменения всех полей.
"""

from abc import ABC, abstractmethod


class Human(ABC):
    """
    Kласс «Человек», включающий в себя имя, фамилию, отчество,
    год рождения и методы, позволяющие изменять/получать значения этих полей.
    """
    def __init__(self, name, surname, patronymic, year_born):
        """
        Инициализация класса «Человек»
        """
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.year_born = year_born

    @abstractmethod
    def print_info(self):
        """
        Получение информации об экземпляре класса
        """

    @abstractmethod
    def change_info(self):
        """
        Изменение информации об экземпляре класса
        """


class Entrepreneur(Human):
    """
    Kласс «Предприниматель» - содержит номер лицензии, адрес регистрации,
    УНН, данные о налоговых платежах (массив пар вида <дата, сумма>).
    """
    def __init__(
            self, name=None, surname=None, patronymic=None, year_born=None,
            license_number=None, registration_address=None, unn=None, data_on_tax_payments=None
            # unn - это (УНН)
    ):
        super().__init__(name, surname, patronymic, year_born)
        self.license_number = license_number
        self.registration_address = registration_address
        self.unn = unn   # unn (УНН) Учетный номер налогоплательщика
        self.data_on_tax_payments = data_on_tax_payments

    def print_info(self):
        print(
            f"""\n{self.name} {self.surname} {self.patronymic} {self.year_born} года рождения \
            \nНомер лицензии: {self.license_number} \
            \nАдрес регистрации: {self.registration_address}\
            \nУНН: {self.unn} \
            \nДанные о налоговых платежах: {str(self.data_on_tax_payments)}
        """
        )

    def change_info(self):
        self.name = input("Введите имя предпринимателя: ")
        self.surname = input("Введите фамилию предпринимателя: ")
        self.patronymic = input("Введите отчество предпринимателя: ")
        self.year_born = input("Введите дату рождния: ")
        self.license_number = input("Введите номер лицензии ")
        self.registration_address = input("Введите адрес регистрации: ")
        self.unn = input("Введите УНН: ")
        self.data_on_tax_payments = input("Введите данные о налоговых платежах: ")
        return self.print_info()


class Tourist(Human):
    """
    Kласс «Турист» - содержит данные паспорта(строка),
    данные о пересечении границы в виде массива пар <дата, страна>.
    """
    def __init__(
            self, name=None, surname=None, patronymic=None,
            year_born=None, passport_data=None, border_crossing_data=None
    ):
        super().__init__(name, surname, patronymic, year_born)
        self.passport_data = passport_data
        self.border_crossing_data = border_crossing_data

    def print_info(self):
        print(
            f"""\n{self.name} {self.surname} {self.patronymic} {self.year_born} года рождения \
            \nПаспортные данные: {self.passport_data} \
            \nДанные о пересечении границы: {self.border_crossing_data}
        """
        )

    def change_info(self):
        self.name = input("Введите имя туриста: ")
        self.surname = input("Введите фамилию туриста: ")
        self.patronymic = input("Введите отчество туриста: ")
        self.year_born = input("Введите дату рождния: ")
        self.passport_data = input("Введите паспортные данные: ")
        self.border_crossing_data = input("Введите данные о пересечении границы: ")
        return self.print_info()


class Shuttle(Tourist, Entrepreneur):
    """
    «Челнок» (производный от 2 и 3) – добавляется массив строк – список адресов,
    по которым покупается товар. Классы должны содержать методы доступа и изменения всех полей.
    """
    def __init__(
            self, name=None, surname=None, patronymic=None, year_born=None, license_number=None,
            registration_address=None, unn=None, data_on_tax_payments=None,
            passport_data=None, border_crossing_data=None, product_purchase_addresses=None
    ):
        super(Tourist, self).__init__(
            name, surname, patronymic, year_born,
            license_number, registration_address, unn, data_on_tax_payments
        )
        self.passport_data = passport_data
        self.border_crossing_data = border_crossing_data
        self.product_purchase_addresses = product_purchase_addresses

    def print_info(self):
        print(
            f"""\n{self.name} {self.surname} {self.patronymic} {self.year_born} года рождения \
            \nНомер лицензии: {self.license_number} \
            \nАдрес регистрации: {self.registration_address}\
            \nУНН: {self.unn} \
            \nДанные о налоговых платежах: {str(self.data_on_tax_payments)}\
            \nПаспортные данные: {self.passport_data} \
            \nДанные о пересечении границы: {self.border_crossing_data}
        """
        )

    def change_info(self):
        self.name = input("Введите имя преподавателя: ")
        self.surname = input("Введите фамилию преподавателя: ")
        self.patronymic = input("Введите отчество преподавателя: ")
        self.year_born = input("Введите дату рождния: ")
        self.license_number = input("Введите номер лицензии ")
        self.registration_address = input("Введите адрес регистрации: ")
        self.unn = input("Введите УНН: ")
        self.data_on_tax_payments = input("Введите данные о налоговых платежах: ")
        self.passport_data = input("Введите паспортные данные: ")
        self.border_crossing_data = input("Введите данные о пересечении границы: ")
        return self.print_info()


entrepreneur = Entrepreneur(
    'Васильев', 'Василий', 'Васильевич', '1970', '700500300', 'Минск, ул. Ленина, д. 1',
    '946134589', {'2018': 10000, '2019': 20000, '2020': 50000}
)
entrepreneur.print_info()
entrepreneur.change_info()

member = Tourist(
    'Васильев', 'Василий', 'Васильевич', '1970', '4FG6BF4HG61B6C4CV1B',
    {'12.08.2018': 'Польша', '22.01.2019': 'Германия', '5.010.2020': 'Австрия'}
)
member.print_info()

member_lecturer = Shuttle(
    'Васильев', 'Василий', 'Васильевич', '1970', '700500300', 'Минск, ул. Ленина, д. 1',
    '946134589', {'2018': 10000, '2019': 20000, '2020': 50000},
    {'12.08.2018': 'Польша', '22.01.2019': 'Германия', '5.010.2020': 'Австрия'},
    ['Ул. Ленина, 3', 'Ул. Пушкина, 14', 'Ул. Гоголя, 59']
)
member_lecturer.print_info()
member_lecturer.change_info()
member_lecturer.print_info()
