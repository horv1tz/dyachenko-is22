"""
Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Индекс последнего минимального элемента:
Сумма элементов больших 10 во второй половине: 
"""

import random

# Генерация случайной последовательности чисел
def generate_sequence(length):
    sequence = [random.randint(-100, 100) for _ in range(length)]
    return sequence

# Запись последовательности чисел в файл
def write_sequence_to_file(sequence, filename):
    with open(filename, 'w') as file:
        for number in sequence:
            file.write(str(number) + '\n')

# Обработка последовательности чисел
def process_sequence(sequence):
    num_elements = len(sequence)
    min_index = sequence.index(min(sequence))
    sum_gt_10 = sum(num for num in sequence[num_elements // 2:] if num > 10)
    return sequence, num_elements, min_index, sum_gt_10

# Запись обработанных данных в новый файл
def write_processed_data_to_file(data, filename):
    with open(filename, 'w') as file:
        data_list = ', '.join(str(item) for item in data[0])
        file.write("Исходные данные: {}\n".format(data_list))
        file.write("Количество элементов: {}\n".format(data[1]))
        file.write("Индекс последнего минимального элемента: {}\n".format(data[2]))
        file.write("Сумма элементов больших 10 во второй половине: {}\n".format(data[3]))

# Генерация и запись исходной последовательности чисел
sequence = generate_sequence(20)  # пример: 20 элементов
write_sequence_to_file(sequence, 'sequence.txt')

# Обработка последовательности и запись результатов в новый файл
processed_data = process_sequence(sequence)
write_processed_data_to_file(processed_data, 'processed_data.txt')
