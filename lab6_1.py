#   3. Реализовать класс «Человек», включающий в себя имя, фамилию, отчество,
# год рождения и методы, позволяющие изменять/получать значения этих полей.
# Реализовать производные классы:
#   «Преподаватель университета» с полями: должность, ученая степень, специальность,
# список научных трудов (массив строк);
#   «Член комиссии» с полями: название комиссии, год назначения в комиссию,
# номер свидетельства, автобиография (массив строк);
#   «Преподаватели – члены комиссии» (производный от 2 и 3).
# Дополнительное поле – список работ выполненных в комиссии.
# Классы должны содержать методы доступа и изменения всех полей.

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
    def __init__(self, name, surname, patronymic, year_born, position, academ_degree, speciality, work_list, commis_name, commis_appoint_year, certificate_number,
                 autobiogr, works_in_comis):
        super().__init__(name, surname, patronymic, year_born, position, academ_degree, speciality, work_list, commis_name, commis_appoint_year, certificate_number,
                 autobiogr)
        self.works_in_comis = works_in_comis

a = Univer_lecturer('Васильев', 'Василий', 'Васильевич', '1970', 'Лектор', 'Доцент', 'Математиеское моделирование', '1,2,3')
#print(a.print_info())
a.print_info()


#########################
class Fakultet:

    def init(self, univer=None, fac=None):
        self.univer = univer
        self.fac = fac

class Student(Fakultet):

    def init(self, name=None, univer=None, fac=None, bday=None, results=None):
        super().init(univer, fac)
        self.name = name
        self.bday = bday
        self.results = results

    def input_1(self):
        name = input("Введите ФИО студента: ")
        univer = input("Введите университет: ")
        fac = input("Введите факультет: ")
        bday = input("Введите дату рождния: ")
        results = input("Введите результаты сессии: ")
        print(name + ' '+ univer + ' '+fac + ' '+bday+ ' '+results+ ' ')

stud=Student()
stud.input_1()