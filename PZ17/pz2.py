"""
Разработать программу с применением пакета tk, взяв в качестве условия одну
любую задачу из ПЗ №№ 2 – 9
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def generate_string():
    try:
        n = int(entry_n.get())
        if n <= 0:
            raise Exception("N должно быть больше 0")
        show_result('Результат задачи 1', 'C' * n)
    except Exception as exc:
        messagebox.showerror("Ошибка", str(exc))

def normalize_spaces():
    try:
        string = entry_string.get()
        show_result('Результат задачи 2', ' '.join(string.split()))
    except Exception as exc:
        messagebox.showerror("Ошибка", str(exc))

def show_result(title, result):
    result_window = tk.Toplevel(root)
    result_window.title(title)
    result_label = tk.Label(result_window, text=result, padx=20, pady=20)
    result_label.pack()

# Создание главного окна
root = tk.Tk()
root.title("Tkinter Задачи")

# Создание вкладок
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Вкладка для задачи 1
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text='Задача 1')

label_n = tk.Label(frame1, text="Введите целое число N (>0):")
label_n.pack(side=tk.LEFT, padx=10, pady=10)

entry_n = tk.Entry(frame1)
entry_n.pack(side=tk.LEFT, padx=10, pady=10)

button_generate = tk.Button(frame1, text="Создать строку", command=generate_string)
button_generate.pack(side=tk.LEFT, padx=10, pady=10)

# Вкладка для задачи 2
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text='Задача 2')

label_string = tk.Label(frame2, text="Введите строку:")
label_string.pack(side=tk.LEFT, padx=10, pady=10)

entry_string = tk.Entry(frame2)
entry_string.pack(side=tk.LEFT, padx=10, pady=10)

button_normalize = tk.Button(frame2, text="Нормализовать пробелы", command=normalize_spaces)
button_normalize.pack(side=tk.LEFT, padx=10, pady=10)

# Запуск главного цикла приложения
root.mainloop()
