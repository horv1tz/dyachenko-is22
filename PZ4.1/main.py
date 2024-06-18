# Даны два целых числа A и B (A < B). 
# Найти сумму квадратов всех целых чисел от A до B включительно.

from colorama import Fore

def sum_squares(a: int, b: int):
    return sum(i**2 for i in range(a, b+1))

while True:
    try:
        a, b = map(int, input(Fore.WHITE + "Введите числа через пробел, пример (1 2) >> ").split())
        if a > b:
            print(Fore.RED + "Error: Первое число должно быть меньше второго")
        else:
            print(Fore.GREEN + f"Сумма квадратов чисел последовательности >> {sum_squares(a, b)}")

    except ValueError:
        print(Fore.RED + "Error: Введите правильные значения")

    except Exception as ex:
        print(Fore.RED + f"Error: {ex}")

        