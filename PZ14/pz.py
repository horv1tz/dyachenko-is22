"""
В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
Посчитать количество полученных элементов.
"""
# Путь к файлу с текстом
file_path = 'Dostoevsky.txt'

# Импорт необходимых библиотек
import re

# Функция для поиска произведений в тексте
def find_works_in_text(file_path):
    # Открытие файла и чтение его содержимого
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Регулярное выражение для поиска названий произведений в кавычках
    pattern = r'«(.*?)»'
    
    # Поиск всех совпадений в тексте
    works = re.findall(pattern, text)
    
    # Удаление "делу Петрашевского" из списка
    works_filtered = [work for work in works if work.lower() != 'делу петрашевского' and work.lower() != 'время' and work.lower() != 'эпоха']
    
    # Возврат списка уникальных названий произведений и их количества
    return set(works_filtered), len(set(works_filtered))

# Поиск произведений в тексте и их количества
works_found, total_unique_works = find_works_in_text(file_path)
print(works_found, total_unique_works)