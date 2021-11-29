"""
1. Разработать класс Fakultet, порождающим класс Student.
Класс Fakultet включает компоненты данные: наименование ВУЗа и факультета.
Класс Student, включает компоненты данные:
Ф.И.О. студента, год рождения, результаты сдачи последней сессии.
"""

from abc import ABC, abstractmethod


class Fakultet(ABC):
    """
    Класс Fakultet включает компоненты данные:
    наименование ВУЗа и факультета
    """
    def __init__(self, university, fakultet, country):
        """ Инициализация атрибутов """
        self.university = university
        self.fakultet = fakultet
        self.country = country

    @abstractmethod
    def print_object_info(self):
        """
        Выводит информацию об объекте класса
        """
    def return_fakultet(self):
        """
        Выводит информацию о факультете
        """


class Student(Fakultet):
    """
    Класс Student включает компоненты данные:
    Ф.И.О. студента, год рождения, результаты сдачи последней сессии
    """
    def __init__(
            self, university=None, fakultet=None, country=None,
            fio=None, year_born=None, session_results=None
    ):

        super().__init__(university, fakultet, country)
        self.fio = fio
        self.year_born = year_born
        self.session_results = session_results

    def print_object_info(self):
        print(
            f"""\n\nСтудент университета: {self.university} факультета: {self.fakultet} \
            \nСтраны {self.country} \
            \nФИО: {self.fio} \
            \nГод рождения: {self.year_born}\
            \nРезультаты сессии: {self.session_results}
        """
        )

    def set_mark(self):
        """Позволяет ввести отметку за сессию"""
        print('Введите отметки за сессию')
        mark = input()
        print(f'\nУчащийся {self.fio} за сессию получил {mark}')


class UniverLecturer(Fakultet):
    """
    Kласс «Преподаватель университета» с полями:
    должность, ученая степень, специальность,
    список научных трудов
    """
    def __init__(
            self, university=None, fakultet=None, country=None, fio=None,
            year_born=None, academ_degree=None, speciality=None, work_list=None
    ):

        super().__init__(university, fakultet, country)
        self.fio = fio
        self.year_born = year_born
        self.academ_degree = academ_degree
        self.speciality = speciality
        self.work_list = work_list

    def print_object_info(self):
        print(
            f"""\nПреподаватель университета: {self.university} факультета: {self.fakultet} \
            \nСтраны {self.country} \
            \nФИО: {self.fio} \
            \nГод рождения: {self.year_born}\
            \nУченая степень: {self.academ_degree}\
            \nCпециальность: {self.speciality}\
            \nCписок научных трудов: {self.work_list}
        """
        )

    def return_fakultet(self):
        print(
            f"""\nПреподает на факультете: {self.fakultet}"""
        )


class Magistrant(UniverLecturer, Student):
    """
    Kласс «Магистрант» с общими полями класса Student,
    класса UniverLecturer и дополнительным полем "курс"
    """
    def __init__(
            self, university=None, fakultet=None, country=None, fio=None,
            year_born=None, academ_degree=None, speciality=None,
            work_list=None, session_results=None, course=None):

        super().__init__(
            university, fakultet, country, fio,
            year_born, academ_degree, speciality, work_list
        )
        self.session_results = session_results
        self.course = course

    def print_object_info(self):
        print(
            f"""\nМагистрант университета: {self.university} факультета: {self.fakultet} \
            \nСтраны {self.country} \
            \nФИО: {self.fio} \
            \nГод рождения: {self.year_born}\
            \nРезультаты сессии: {self.session_results}\
            \nУченая степень: {self.academ_degree}\
            \nCпециальность: {self.speciality}\
            \nCписок научных трудов: {self.work_list}\
            \nКурс: {self.course}
        """
        )

    def print_magistrant(self):
        """Выводит информацию без привязки к университету"""
        print(
            f"""\nФИО: {self.fio} \
            \nГод рождения: {self.year_born}\
            \nРезультаты сессии: {self.session_results}\
            \nУченая степень: {self.academ_degree}\
            \nCпециальность: {self.speciality}\
            \nCписок научных трудов: {self.work_list}\
            \nКурс: {self.course}
        """
        )


student = Student('BSUIR', 'FKP', 'Belarus', 'Neveikov Andrey Sergeevich', '200', '10 10 10 10 10')
student.print_object_info()

lecturer = UniverLecturer(
    'BSUIR', 'FKP', 'Belarus', 'Павлов Павел Павлович', '1970', 'Доктор наук',
    'Машинное обучение', ['Программирование', 'Аналитика данных', 'Нейронные сети']
)
lecturer.print_object_info()

magistrant = Magistrant(
    'BSUIR', 'FKP', 'Belarus', 'Васильев Василий Васильевич', '1998', 'Бакалавр',
    'Радиотехника', ['Ротоботехника', 'Программировние эл. приборов'],
    '9 9 9 9 9', '1'
)
magistrant.print_object_info()
magistrant.print_magistrant()
magistrant.set_mark()
