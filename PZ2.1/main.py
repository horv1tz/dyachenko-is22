# Дан размер файла в байтах.
# Используя операцию деления нацело, найти количество полных килобайтов, которые занимает данный файл.
try:
    input_weight_b = float(input("Введите размер файла в байтах >> "))
    weight_kb = int(input_weight_b // 1024)
    print(f'Размер файла в килобайтах << {weight_kb}KB')
    
except ValueError:
    print("Ошибка: Введено некорректное значение. Введите целое число.")