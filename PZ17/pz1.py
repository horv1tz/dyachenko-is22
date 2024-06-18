"""
В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
приближенный к оригиналу 
https://i.pinimg.com/originals/73/c6/0d/73c60def8c55043f9fd27b370530a9cf.jpg
"""

import tkinter as tk
from tkinter import ttk

def submit():
    print("Form Submitted")

def cancel():
    root.destroy()

# Создание главного окна
root = tk.Tk()
root.title("Sign Up")
# root.geometry("560x656")
root.resizable(width=False, height=False)
root.configure(bg='#e28406')

# Frame 1: Title
frame1 = tk.Frame(root, bg='#e28406', height=41)
frame1.grid(row=0, column=0, columnspan=2, sticky='ew')
label_title = tk.Label(frame1, text="Sign Up", fg='#ebd216', bg='#e28406', font=('Arial', 16), anchor='w')
label_title.pack(fill="both", padx=10, pady=10)

# Frame 2: Form Fields
frame2 = tk.Frame(root, bg='#242446')
frame2.grid(row=1, column=0, columnspan=2, padx=0, pady=0, sticky='nsew')

# First Name
label_first_name = tk.Label(frame2, text="First Name", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_first_name.grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_first_name = tk.Entry(frame2, width=30, font=('Arial', 12))
entry_first_name.insert(0, "Enter First Name...")
entry_first_name.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Last Name
label_last_name = tk.Label(frame2, text="Last Name", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_last_name.grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_last_name = tk.Entry(frame2, width=30, font=('Arial', 12))
entry_last_name.insert(0, "Enter Last Name...")
entry_last_name.grid(row=1, column=1, padx=10, pady=5, sticky='w')

# Screen Name
label_screen_name = tk.Label(frame2, text="Screen Name", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_screen_name.grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_screen_name = tk.Entry(frame2, width=30, font=('Arial', 12))
entry_screen_name.insert(0, "Enter Screen Name...")
entry_screen_name.grid(row=2, column=1, padx=10, pady=5, sticky='w')

# Date of Birth
label_dob = tk.Label(frame2, text="Date of Birth", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_dob.grid(row=3, column=0, padx=10, pady=5, sticky='e')

# Создание фрейма для выпадающих списков даты рождения
dob_frame = tk.Frame(frame2, bg='#242446')
dob_frame.grid(row=3, column=1, padx=10, pady=5, sticky='w')

months = ttk.Combobox(dob_frame, values=["January", "February", "March", "April", "May", "June", 
                                      "July", "August", "September", "October", "November", "December"], width=7)
months.current(4)
months.grid(row=0, column=0, padx=0, pady=5)

days = ttk.Combobox(dob_frame, values=list(range(1, 32)), width=3)
days.current(4)
days.grid(row=0, column=1, padx=0, pady=5)

years = ttk.Combobox(dob_frame, values=list(range(1900, 2024)), width=5)
years.current(85)
years.grid(row=0, column=2, padx=0, pady=5)

# Gender
label_gender = tk.Label(frame2, text="Gender", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_gender.grid(row=4, column=0, padx=10, pady=5, sticky='e')
gender_frame = tk.Frame(frame2, bg='#242446')
gender_frame.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky='w')
male_rb = tk.Radiobutton(gender_frame, text="Male", variable=tk.IntVar(), value=1, bg='#242446', fg='#e9e59b', font=('Arial', 12))
male_rb.pack(side='left')
female_rb = tk.Radiobutton(gender_frame, text="Female", variable=tk.IntVar(), value=2, bg='#242446', fg='#e9e59b', font=('Arial', 12))
female_rb.pack(side='left')

# Country
label_country = tk.Label(frame2, text="Country", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_country.grid(row=5, column=0, padx=10, pady=5, sticky='e')
country = ttk.Combobox(frame2, values=["USA", "Canada", "UK", "Australia"], width=20)
country.current(0)
country.grid(row=5, column=1, columnspan=3, padx=10, pady=5, sticky='w')

# E-mail
label_email = tk.Label(frame2, text="E-mail", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_email.grid(row=6, column=0, padx=10, pady=5, sticky='e')
entry_email = tk.Entry(frame2, width=30, font=('Arial', 12))
entry_email.insert(0, "Enter E-mail...")
entry_email.grid(row=6, column=1, columnspan=3, padx=10, pady=5, sticky='w')

# Phone
label_phone = tk.Label(frame2, text="Phone", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_phone.grid(row=7, column=0, padx=10, pady=5, sticky='e')
entry_phone = tk.Entry(frame2, width=30, font=('Arial', 12))
entry_phone.insert(0, "Enter Phone...")
entry_phone.grid(row=7, column=1, columnspan=3, padx=10, pady=5, sticky='w')

# Password
label_password = tk.Label(frame2, text="Password", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_password.grid(row=8, column=0, padx=10, pady=5, sticky='e')
entry_password = tk.Entry(frame2, width=30, font=('Arial', 12), show="*")
entry_password.grid(row=8, column=1, columnspan=3, padx=10, pady=5, sticky='w')

# Confirm Password
label_confirm_password = tk.Label(frame2, text="Confirm Password", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_confirm_password.grid(row=9, column=0, padx=10, pady=5, sticky='e')
entry_confirm_password = tk.Entry(frame2, width=30, font=('Arial', 12), show="*")
entry_confirm_password.grid(row=9, column=1, columnspan=3, padx=10, pady=5, sticky='w')

# Agreement Checkbutton
# Creating a separate frame for the label and checkbutton
frame_agree = tk.Frame(frame2, bg='#242446')
frame_agree.grid(row=10, column=1, columnspan=4, padx=10, pady=5, sticky='e')

# Agreement Label
label_agree = tk.Label(frame_agree, text="I agree to the Terms of Use", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_agree.grid(row=0, column=1, padx=10, pady=5, sticky='w')

# Agreement Checkbutton
agree_var = tk.IntVar()
check_agree = tk.Checkbutton(frame_agree, variable=agree_var, bg='#242446')
check_agree.grid(row=0, column=0, padx=5, pady=5, sticky='w')


# Frame 3: Buttons
frame3 = tk.Frame(root, bg='#e28406')
frame3.grid(row=2, column=0, columnspan=2, sticky='ew')
cancel_button = tk.Button(frame3, text="Cancel", command=cancel, fg="#ffffff", bg='#fc4c4c', font=('Arial', 14), width=10)
cancel_button.pack(side='right', padx=10, pady=10)
submit_button = tk.Button(frame3, text="Submit", command=submit, fg="#ffffff", bg='#55d237', font=('Arial', 14), width=10)
submit_button.pack(side='right', padx=5, pady=10)

root.mainloop()
