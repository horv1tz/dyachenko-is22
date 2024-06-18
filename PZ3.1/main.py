# Даны 2 целых числа: A, B. Проверить истиность высказывания:
# "Каждое из чисел A и B нечётное."
from colorama import Fore

try:
    a = float(input("Введите первое число >> "))
    b = float(input("Введите второе число >> "))

    if (a % 2 == 1) and (b % 2 == 1):
        print("Оба числа нечётные")
    else:
        print("Нечётные не оба числа")

except ValueError:
    print(Fore.RED + "Введите число") 