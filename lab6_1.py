from abc import ABC, abstractmethod

class Human(ABC):

    def __init__(self, name, surname, patronymic, year_born):
        # Инициализация атрибутов
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.year_born = year_born

    @abstractmethod
    def print_info(self):
        pass

class Univer_lecturer(Human):

    def __init__(self, name, surname, patronymic, year_born, position, academ_degree, speciality, work_list):
        super().__init__(name, surname, patronymic, year_born)
        self.position = position
        self.academ_degree = academ_degree
        self.speciality = speciality
        self.work_list = work_list


    def print_info(self):
        print('\nФИО ' + self.name + ' ' + self.surname + ' ' + self.patronymic + ' ' + self.year_born + ' года рождения ' + \
              ' \nДолжность: ' + self.position + ' \nУченая степень: ' + self.academ_degree +' \nСпециальность: ' + self.speciality + \
              ' \nСписок научных трудов: ' + self.work_list)



class Commis_member(Human):
    def __init__(self, name, surname, patronymic, year_born, commis_name, commis_appoint_year, certificate_number, autobiogr):
        super().__init__(name, surname, patronymic, year_born)
        self.commis_name = commis_name
        self.commis_appoint_year = commis_appoint_year
        self.certificate_number = certificate_number
        self.autobiogr = autobiogr


    def print_info(self):
        print('\nФИО ' + self.name + ' ' + self.surname + ' ' + self.patronymic + ' ' + self.year_born + ' года рождения ' + \
              ' \nНазвание комиссии: ' + self.commis_name + ' \nГод назначения в комиссию: ' + self.commis_appoint_year +' \nСпециальность: ' + self.certificate_number + \
              ' \nСписок научных трудов: ' + self.autobiogr)


class Commis_and_lecturer(Univer_lecturer, Commis_member):
    pass

a = Univer_lecturer('Васильев', 'Василий', 'Васильевич', '1970', 'Лектор', 'Доцент', 'Математиеское моделирование', '1,2,3')
#print(a.print_info())
a.print_info()