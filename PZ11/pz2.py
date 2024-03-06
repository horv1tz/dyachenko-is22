"""
Из предложенного текстового файла (text18-8.txt) вывести на экран его содержимое,
количество символов, принадлежащих к группе букв. Сформировать новый файл, в
который поместить текст в стихотворной форме предварительно удалив букву «с» из
текста
"""

# Путь к исходному файлу
source_file_path = 'text18-8.txt'
# Путь к новому файлу
new_file_path = 'return.txt'

# Чтение исходного файла 
with open(source_file_path, 'r', encoding='utf-16') as file:
    text = file.read()
    print('Содержимое: ' + text)

# Подсчет количества буквенных символов
letter_count = sum(c.isalpha() for c in text)
print(f'Количество буквенных символов: {letter_count}')

# Удаление буквы "с" из текста и форматирование в стихотворную форму
formatted_text = '\n'.join(line.replace('с', '') for line in text.split('\n'))

# Сохранение отформатированного текста в новый файл
with open(new_file_path, 'w', encoding='utf-8') as new_file:  
    new_file.write(formatted_text)

print('Обработка завершена, файл сохранен.')

