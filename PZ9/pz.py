# Исходная строка
data_str = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'

# Преобразование строки в словарь
data_list = data_str.split()  # Разделение строки на элементы
data_dict = {}
key = ''

for item in data_list:
    if item.isalpha():  # Если элемент - слово, используем его как ключ
        key = item
        data_dict[key] = []
    else:  # Иначе, добавляем элемент (преобразованный в число) в список текущего ключа
        data_dict[key].append(int(item))

# Функция для расчёта среднего значения
def calculate_average(sales_list):
    return sum(sales_list) / len(sales_list)

# Расчёт средних значений и вывод результатов
average_sales = {product: calculate_average(sales) for product, sales in data_dict.items()}

# Вывод результатов
for product, average in average_sales.items():
    print(f'Среднее количество проданных {product}: {average} кг')
