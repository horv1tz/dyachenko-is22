"""
Дан список размера N. Найти количество участков, на которых его элементы
монотонно возрастают.
"""

from random import sample

def count_increasing_segments(lst):
    count = 0
    i = 0
    while i < len(lst) - 1:
        if lst[i] < lst[i + 1]:
            # Начало нового возрастающего участка
            while i < len(lst) - 1 and lst[i] < lst[i + 1]:
                i += 1
            count += 1
        i += 1
    return count

try:
    list = sample(range(10), 10)
    print("Исходный список: ", list)
    print("Количество возрастающих участков:", count_increasing_segments(list))
          
except Exception as exc:
    print(exc)