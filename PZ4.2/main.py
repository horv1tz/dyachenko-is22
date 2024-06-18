# Начальный вклад в банке равен 1000 руб.
# Через каждый месяц размер вклада увеличивается на Р процентов от имеющейся суммы (Р - вещественное число, 0< Р <25). 
# По данному Р определить, через сколько месяцев размер вклада превысит 1100руб.,
# и вывести найденное количество месяцев К (целое число) и итоговый размервклада S (вещественное число).
from colorama import Fore

def get_months_and_total(procent: float):
        total = 1000
        months = 0
        
        if (procent < 0) or (procent > 25):
            print(Fore.RED + 'Процент должен быть больше 0 и меньше 25')
            
        else:
            while total < 1100:
                total += total * (procent  / 100)
                months += 1

        return total, months

while True:
    try:
        procent = float(input(Fore.WHITE + "Введите месячный процент >> "))
        total, months = get_months_and_total(procent)
        
        print(Fore.GREEN + f"Месяцы: {months}")
        print(Fore.GREEN + f"Итоговая сумма вклада: {total}")

    except ValueError:
        print(Fore.RED + "Error: Введите правильные значения")

    except Exception as ex:
        print(Fore.RED + f"Error: {ex}")
