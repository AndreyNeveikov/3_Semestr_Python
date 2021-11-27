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
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.year_born = year_born

    @abstractmethod
    def print_info(self):
        pass

    @abstractmethod
    def change_info(self):
        pass

class Univer_lecturer(Human):

    def __init__(self, name = None, surname = None, patronymic = None, year_born = None, position = None, academ_degree = None, speciality = None, work_list = None):
        super().__init__(name, surname, patronymic, year_born)
        self.position = position
        self.academ_degree = academ_degree
        self.speciality = speciality
        self.work_list = work_list


    def print_info(self):
        print('\n' + self.name + ' ' + self.surname + ' ' + self.patronymic + ' ' + self.year_born + ' года рождения ' + \
              ' \nДолжность: ' + self.position + ' \nУченая степень: ' + self.academ_degree + \
              ' \nСпециальность: ' + self.speciality + ' \nСписок научных трудов: ' + str(self.work_list))

    def change_info(self):
        self.name = input("Введите имя преподавателя: ")
        self.surname = input("Введите фамилию преподавателя: ")
        self.patronymic = input("Введите отчество преподавателя: ")
        self.year_born = input("Введите дату рождния: ")
        self.position = input("Введите должность: ")
        self.academ_degree = input("Введите ученую степень: ")
        self.speciality = input("Введите специальность: ")
        self.work_list = input("Введите список научных работ: ")
        return self.print_info()

class Commis_member(Human):
    def __init__(self, name = None, surname = None, patronymic = None, year_born = None, commis_name = None, commis_appoint_year = None, certificate_number = None, autobiogr = None):
        super().__init__(name, surname, patronymic, year_born)
        self.commis_name = commis_name
        self.commis_appoint_year = commis_appoint_year
        self.certificate_number = certificate_number
        self.autobiogr = autobiogr


    def print_info(self):
        print('\n' + self.name + ' ' + self.surname + ' ' + self.patronymic + ' ' + self.year_born + ' года рождения ' + \
              ' \nНазвание комиссии: ' + self.commis_name + ' \nГод назначения в комиссию: ' + self.commis_appoint_year +' \nНомер свдельства: ' + self.certificate_number + \
              ' \nАвтобиография: ' + str(self.autobiogr))

    def change_info(self):
        self.name = input("Введите имя преподавателя: ")
        self.surname = input("Введите фамилию преподавателя: ")
        self.patronymic = input("Введите отчество преподавателя: ")
        self.year_born = input("Введите дату рождния: ")
        self.commis_name = input("Введите название комиссии: ")
        self.commis_appoint_year = input("Введите год назначения в комиссию: ")
        self.certificate_number = input("Введите номер свидетельства: ")
        self.autobiogr = input("Введите автобиографию: ")
        return self.print_info()

class Commis_and_lecturer(Commis_member, Univer_lecturer):
    def __init__(self, name = None, surname = None, patronymic = None, year_born = None, position = None, academ_degree = None, speciality = None, work_list = None, commis_name = None, commis_appoint_year = None, certificate_number = None,
                 autobiogr = None, works_in_comis = None):
        super(Commis_member, self).__init__(name, surname, patronymic, year_born, position, academ_degree, speciality, work_list)
        self.commis_name = commis_name
        self.commis_appoint_year = commis_appoint_year
        self.certificate_number = certificate_number
        self.autobiogr = autobiogr
        self.works_in_comis = works_in_comis

    def print_info(self):
        print(
            '\n' + self.name + ' ' + self.surname + ' ' + self.patronymic + ' ' + self.year_born + ' года рождения ' + \
            ' \nДолжность: ' + self.position + ' \nУченая степень: ' + self.academ_degree + ' \nСпециальность: ' + self.speciality + \
            ' \nСписок научных трудов: ' + str(self.work_list) + \
            ' \nНазвание комиссии: ' + self.commis_name + ' \nГод назначения в комиссию: ' + self.commis_appoint_year + ' \nНомер свдельства: ' + self.certificate_number + \
            ' \nАвтобиография: ' + str(self.autobiogr) + ' \nСписок работ в комисии: ' + str(self.works_in_comis))

    def change_info(self):
        self.name = input("Введите имя преподавателя: ")
        self.surname = input("Введите фамилию преподавателя: ")
        self.patronymic = input("Введите отчество преподавателя: ")
        self.year_born = input("Введите дату рождния: ")
        self.position = input("Введите должность: ")
        self.academ_degree = input("Введите ученую степень: ")
        self.speciality = input("Введите специальность: ")
        self.work_list = input("Введите список научных работ: ")
        self.commis_name = input("Введите название комиссии: ")
        self.commis_appoint_year = input("Введите год назначения в комиссию: ")
        self.certificate_number = input("Введите номер свидетельства: ")
        self.autobiogr = input("Введите автобиографию: ")
        self.works_in_comis = input("Введите список работ в комиссии: ")
        return self.print_info()




lecturer = Univer_lecturer('Васильев', 'Василий', 'Васильевич', '1970', 'Лектор', 'Доцент', 'Математиеское моделирование', ['Математика', 'Cложная математика', 'Cложная математика 2'])
lecturer.print_info()
lecturer.change_info()

member = Commis_member('Васильев', 'Василий', 'Васильевич', '1970', '"Комиссия экзаменационная"', '2000', '70055036', ['Оценка энакзамена', 'Формирование другой комиссии'])
member.print_info()

member_lecturer = Commis_and_lecturer('Васильев', 'Василий', 'Васильевич', '1970', '"Комиссия экзаменационная"', '2000', '70055036', ['Физика', 'Cложная физика', 'Cложная физика 2'], 'Лектор', 'Доцент', 'Математиеское моделирование', ['Оценка зачета', 'Формирование третьей комиссии'], 'Родился, учился, преподает')
member_lecturer.print_info()
