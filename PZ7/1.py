"""
Дано целое число N (>0) и символ C. Вывести строку длины N, которая состоит из
символов C.
"""
try:
    n = int(input("Введите целое число N (>0): "))
    if n <= 0:
        raise Exception("N должно быть больше 0")
    print('C' * n)

except Exception as exc:
    print(exc)