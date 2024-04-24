import random

def multiply_column(matrix, N):
    if not matrix or N >= len(matrix[0]):
        print("Неверный номер столбца или матрица пуста")
        return matrix
    for row in matrix:
        row[N] *= 2
    return matrix

rows, cols = map(int, input("Введите количество строк и столбцов матрицы через пробел: ").split())
N = int(input("Введите номер столбца N для увеличения (отсчет с 0): "))

matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
print("Исходная матрица:", *matrix, sep='\n')

result_matrix = multiply_column(matrix, N)
print("Матрица после увеличения элементов столбца N:", *result_matrix, sep='\n')
