from random import randint

# Функция для замены элементов последней строки на 0
def replace_last_row(matrix):
    matrix[-1] = [0] * len(matrix[-1])
    return matrix

# Пример использования
rows, cols = map(int, input("Введите количество строк и столбцов матрицы через пробел: ").split())

# Создаем матрицу с размерами rows x cols
matrix = [[randint(1, 10) for _ in range(cols)] for _ in range(rows)]
print("Исходная матрица:")
for row in matrix:
    print(row)

# Вызываем функцию
result_matrix = replace_last_row(matrix)
print("Матрица после замены элементов последней строки на 0:")
for row in result_matrix:
    print(row)
