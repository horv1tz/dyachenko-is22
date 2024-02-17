'''
В последовательности на n целых элементов найти количество пар, для которых
произведение элементов делится на 3 (элементы пары в последовательности являются
соседними).
'''

def count_pairs_divisible_by_3(sequence):
    count = 0
    for i in range(len(sequence) - 1):
        if (sequence[i] * sequence[i+1]) % 3 == 0:
            count += 1
    return count

# Пример использования функции
sequence = [1, 2, 3, 4, 5, 6]  # Пример последовательности
result = count_pairs_divisible_by_3(sequence)
print(f"Количество пар, произведение которых делится на 3: {result}")
