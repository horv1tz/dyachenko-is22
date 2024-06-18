"""
Дан целочисленный список размера 10. Вывести все содержащиеся в данном списе
четные числа в порядке убывания их индексов, а также их количество K.
"""
from random import sample

try:
    list = sample(range(10), 10)

    print("Исходный список: ", list)

    for i in range(len(list)-1, -1, -1):
        print("Четное число: ", list[i], "Индекс: ", i)

except Exception as exc:
    print(exc) 


    