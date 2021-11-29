"""
Напишите шаблон класса односвязного списка,
который принимает элементы любого типа.
В классе реализуйте функции для работы с односвязным списком.
"""

from abc import ABC, abstractmethod


class ListTemplate(ABC):

    @abstractmethod
    def append(self, *args):
        """
        Добавляет элемент в конец массива
        """

    @abstractmethod
    def insert(self, *args):
        """
        Добавляет элемент в середину массива
        """

    @abstractmethod
    def get_element(self, *args):
        """
        Выводит элемент с заданным индексом
        """

    @abstractmethod
    def delete_element(self, *args):
        """
        Удаляет элемент с заданным индексом из массива
        """

    @abstractmethod
    def out(self, *args):
        """
        Вывод массива
        """


class LinkedList(ListTemplate):
    """Односвязный список"""
    head = None    # Начало списка

    class Node:
        """"Запись в списке (принимает любой тип)"""

        def __init__(self, element=None, next_node=None):
            """Инициализация записи"""
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if not self.head:   # Если список еще пустой
            self.head = self.Node(element)   # Присваиваем значение в head
            return element

        # Если нет, добираемся до последнего элемента
        node = self.head

        while node.next_node:   # Пока есть следующий элемент
            node = node.next_node   # Присваиваем значение следующего

        node.next_node = self.Node(element)   # Когда закончились, присваиваем значение

    def insert(self, element, index):
        """
           ()             ()       Убираем старую связь между элементами
           V     -->     /  \
        ()---()        ()   ()     и добавляем две новых
        """
        i = 0
        node = self.head
        prev_node = self.head

        while i < index:   # Доходим до индекса элемента, который вставляем
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = self.Node(element, next_node=node)   # Новый узел (node - позиция)

        return element

    def get_element(self, index):
        i = 0
        node = self.head

        while i < index:   # Проходим до нужного элемента
            node = node.next_node
            i += 1

        return node.element

    def delete_element(self, index):
        """
           ()             ()       Убираем две старых связи между элементами
          /  \
        ()   ()        ()---()     и соединяем соседние элементы
        """
        if index == 0:   # Переназначаем голову в следующий узел
            self.head = self.head.next_node

        node = self.head
        i = 0
        prev_node = node

        while i < index:   # Проходим до нужного элемента
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = node.next_node   # Убираем связи с искомым элементом
        element = node.element
        del node   # Удаляем искомый элемент

        return element

    def out(self):
        node = self.head

        while node.next_node:   # Печать пока есть следующий
            print(node.element)
            node = node.next_node
        print(node.element)   # Печать последнего


linked_list = LinkedList()

linked_list.append(123)    # int
linked_list.append(456.00)    # float
linked_list.append('789')    # string
linked_list.append(['list element 1', 'list element 2'])    # list
linked_list.append((9, 8, 7))    # tuple
linked_list.append({654})    # set
linked_list.append({"one": 1, "two": 2, "three": 3})    # dict
linked_list.append(True)    # bool
linked_list.append(123)

linked_list.insert(999, 4)

print("\nПолучившийся список")
linked_list.out()

print(f'\nЭлемент с заданным индексом: {linked_list.get_element(4)}')
print(f'\nУдален элемент: {linked_list.delete_element(5)}')
linked_list.out()
