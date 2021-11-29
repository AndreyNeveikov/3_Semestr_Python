"""
8. Написать функцию-шаблон,
вычисляющую максимальное значение в массиве.

10. Написать функцию-шаблон,
переставляющую элементы в массиве.
"""

import random
from abc import ABC, abstractmethod


class FunctionTemplate(ABC):
    """Шаблон класса для работы с массивами"""

    @abstractmethod
    def find_max(self):
        """Вычисляет максимальное значение"""

    @abstractmethod
    def rearranging_elements(self, size):
        """Переставляет элементы в массиве"""


class ArrayFunctions(FunctionTemplate):
    """Класс для работы с массивами"""

    def __init__(self, array=None):
        """Инициализация массива"""
        self.array = array

    def find_max(self):
        max_element = self.array[0]
        for element in self.array:
            if element > max_element:
                max_element = element
        return max_element

    def rearranging_elements(self, size):
        i = 0

        while i < size:
            rand_result_start = random.randint(0, size)
            rand_result_swapped = random.randint(0, size)
            tmp = self.array[rand_result_start]
            self.array[rand_result_start] = self.array[rand_result_swapped]
            self.array[rand_result_swapped] = tmp
            i += 1
        return self.array


array_test = ArrayFunctions(
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
)

print(array_test.find_max())
print(array_test.rearranging_elements(8))
