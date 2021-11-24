# 1. Разработать класс Fakultet, порождающим класс Student.
# Класс Fakultet включает компоненты данные: наименование ВУЗа и факультета.
# Класс Student, включает компоненты данные:
# Ф.И.О. студента, год рождения, результаты сдачи последней сессии.


class Fakultet():

    def __init__(self, university, fakultet, country):
        # Инициализация атрибутов
        self.university = university
        self.fakultet = fakultet
        self.country = country

    def print_fakultet(self, university, fakultet, country):
        print('\nСтуден университета: ' + university + ' факультета: ' + fakultet + '\nСтраны ' + country)


class Student(Fakultet):

    def __init__(self, university, fakultet, country, FIO, year, results):
        super().__init__(university, fakultet, country)
        self.FIO = FIO
        self.year = year
        self.results = results

    def print_stud(self, university, fakultet, country, FIO, year, results):
        print('\nСтуден университета: ' + university + ' факультета: ' + fakultet + '\nСтраны ' + country +
              '\nФИО ' + FIO + ' ' + year + ' года рождения' + '\nРезультаты сессии' + results)

    def set_mark(self, FIO):
        print('ВВедите отметку за сессию')
        mark = input()
        print('\nУ ' + FIO + ' за сессию ' + mark)


class Groupmate(Student):

    def __init__(self, university, fakultet, country, FIO, year, results, group):
        super().__init__(university, fakultet, country, FIO, year, results)
        self.group = group

    def print_groupmate(self, university, fakultet, country, FIO, year, results, group):
        print('\nСтуден университета: ' + university + ' факультета: ' + fakultet + '\nСтраны ' + country +
              '\nФИО ' + FIO + ' ' + year + ' года рождения' + '\nРезультаты сессии' + results + '\nНомер группы ' + group)

    def print_stud(self, FIO, year, results, group):
        print('\nФИО ' + FIO + ' ' + year + ' года рождения' + '\nРезультаты сессии' + results + '\nНомер группы ' + group)


std = Student('BSUIR', 'FKP', 'Belarus', 'Neveikov Andrey Sergeevich', '200', '10 10 10 10 10')
std.print_stud('BSUIR', 'FKP', 'Belarus', 'Neveikov Andrey Sergeevich', '200', '10 10 10 10 10')
std.print_fakultet('BSUIR', 'FKP', 'Belarus')

stud1 = Groupmate('BSUIR', 'FKP', 'Belarus', 'Васильев Василий Васильевич', '200', '9 9 9 9 9', '014301')
stud1.print_groupmate('BSUIR', 'FKP', 'Belarus', 'Васильев Василий Васильевич', '200', '9 9 9 9 9', '014301')
stud1.print_stud('Васильев Василий Васильевич', '200', '9 9 9 9 9', '014301')
stud1.set_mark('Васильев Василий Васильевич')