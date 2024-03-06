import numpy as np

# Функция для замены элементов последней строки на 0
def replace_last_row(matrix):
    matrix[-1, :] = 0
    return matrix

# Пример использования
rows, cols = map(int, input("Введите количество строк и столбцов матрицы через пробел: ").split())

# Создаем матрицу с размерами rows x cols
matrix = np.random.randint(1, 10, size=(rows, cols))
print("Исходная матрица:")
print(matrix)

# Вызываем функцию
result_matrix = replace_last_row(matrix)
print("Матрица после замены элементов последней строки на 0:")
print(result_matrix)
