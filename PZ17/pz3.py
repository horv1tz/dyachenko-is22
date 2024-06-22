"""
Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
оформленный согласно требованиям. Все задания выполняются c использованием модуля
OS:
•	перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена вложенных подкаталогов выводить не нужно.
•	перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
•	Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере файлов в папке test.
•	перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в консоль. Использовать функцию basename () (os.path.basename()).
•	перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в привязанной к нему программе. Использовать функцию os.startfile().
•	удалить файл test.txt
"""
import os
import shutil

try:
    # 1. Перейти в каталог PZ11 и вывести список всех файлов
    os.chdir('PZ11')
    files_in_pz11 = [f for f in os.listdir() if os.path.isfile(f)]
    print("Files in PZ11:", files_in_pz11)
    
    # 2. Перейти в корень проекта, создать папку test и test1
    os.chdir('..')  # Переход в корень проекта
    os.makedirs('test\\test1', exist_ok=True)
    
    # 3. Переместить файлы из ПЗ6 и ПЗ7
    pz6_files = ['PZ6\\1.py', 'PZ6\\2.py']
    pz7_file = 'PZ7\\1.py'
    
    for file in pz6_files:
        if os.path.exists(file):
            shutil.copy(file, 'test\\' + os.path.basename(file))
        else:
            print(f"File not found: {file}")

    if os.path.exists(pz7_file):
        shutil.copy(pz7_file, 'test\\test1\\test.txt')
    else:
        print(f"File not found: {pz7_file}")
    
    # 4. Вывести информацию о размере файлов в папке test
    test_files = [f for f in os.listdir('test') if os.path.isfile(os.path.join('test', f))]
    for file in test_files:
        file_size = os.path.getsize(os.path.join('test', file))
        print(f"Size of {file}: {file_size} bytes")
    
    # 5. Найти файл с самым коротким именем в PZ11
    os.chdir('PZ11')
    shortest_name_file = min(files_in_pz11, key=len)
    print("File with shortest name:", os.path.basename(shortest_name_file))
    
    # 6. Запустить отчет в формате .pdf
    os.chdir('..')
    pdf_path = 'reports\\report13.pdf'
    if os.path.exists(pdf_path):
        os.startfile(pdf_path)
    else:
        print(f"PDF report not found: {pdf_path}")
    
    # 7. Удалить файл test.txt
    test_txt_path = 'test\\test1\\test.txt'
    if os.path.exists(test_txt_path):
        os.remove(test_txt_path)
    else:
        print(f"File not found: {test_txt_path}")

except Exception as e:
    print(f"An error occurred: {e}")
