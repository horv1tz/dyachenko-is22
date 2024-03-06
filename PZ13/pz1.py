import numpy as np

# Функция для увеличения элементов столбца N в два раза
def multiply_column(matrix, N):
    # Проверяем, что N не выходит за границы матрицы
    if N < 0 or N >= matrix.shape[1]:
        print("Неверный номер столбца")
        return matrix
    # Умножаем элементы столбца N на 2
    matrix[:, N] *= 2
    return matrix

# Пример использования
rows, cols = map(int, input("Введите количество строк и столбцов матрицы через пробел: ").split())
N = int(input("Введите номер столбца N для увеличения (отсчет с 0): "))

# Создаем матрицу с размерами rows x cols
matrix = np.random.randint(1, 10, size=(rows, cols))
print("Исходная матрица:")
print(matrix)

# Вызываем функцию
result_matrix = multiply_column(matrix, N)
print("Матрица после увеличения элементов столбца N:")
print(result_matrix)
