# Единицы длины пронумерованы следующим образом: 1 — дециметр, 2 — километр, 3 — метр, 4 — миллиметр, 5 — сантиметр. 
# Дан номер единицы длины (целое число в диапазоне 1-5) и длина отрезка в этих единицах (вещественное число). 
# Найти длину отрезка в метрах.
from colorama import Fore
                    
while True:
    try:
        unit = int(input("Введите номер единицы длины (1-5): "))
        length = float(input("Введите длину отрезка в выбранных единицах: "))
                        
        if unit == 1:
            length_m = length / 10
        elif unit == 2:
            length_m = length * 1000
        elif unit == 3:
            length_m = length
        elif unit == 4:
            length_m = length / 1000
        elif unit == 5:
            length_m = length / 100
        else:
            print("Вы ввели неправильное значение")
            break
                                      
        print(Fore.GREEN + f"Длина отрезка в метрах: {length_m}")
    except ValueError:
        print(Fore.RED + "Введите число")