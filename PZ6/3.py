"""
Дан список размера N. Заменить каждый элемент списка на среднее арифметическое
этого элемента и его соседей.
"""
import random 

try:
    list = random.sample(range(10), 10)
    print("Исходный список: ", list)

    for i in range(len(list)):
        if i == 0:
            list[i] = (list[i] + list[i + 1]) / 2
        elif i == len(list) - 1:
            list[i] = (list[i] + list[i - 1]) / 2
        else:
            list[i] = (list[i - 1] + list[i] + list[i + 1]) / 3

    print("Измененный список: ", list)

except Exception as exc:
    print(exc)