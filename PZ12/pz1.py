'''
В последовательности на n целых элементов найти количество пар, для которых
произведение элементов делится на 3 (элементы пары в последовательности являются
соседними).
'''

def count_pairs_divisible_by_three(sequence):
    # Создаем пары соседних элементов
    pairs = zip(sequence, sequence[1:])
    # Фильтруем те пары, произведение которых делится на 3
    divisible_pairs = filter(lambda pair: (pair[0] * pair[1]) % 3 == 0, pairs)
    # Возвращаем количество таких пар
    return len(list(divisible_pairs))

<<<<<<< HEAD
sequence = [1, 3, 6, 4, 9, 8]
=======
sequence = [1, 3, 5, 4, 9, 8]
>>>>>>> 347fb23cc562486b01bafd48880c188e972dafbd
print(f"Количество пар, произведение которых делится на 3: {count_pairs_divisible_by_three(sequence)}")
