import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

def submit():
    print("Form Submitted")

def cancel():
    root.destroy()

# Создание главного окна с использованием ttkbootstrap
root = tb.Window(themename="darkly")
root.title("Sign Up")
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
entry_first_name = ttk.Entry(frame2, width=30, font=('Arial', 12))
entry_first_name.insert(0, "Enter First Name...")
entry_first_name.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Last Name
label_last_name = tk.Label(frame2, text="Last Name", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_last_name.grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_last_name = ttk.Entry(frame2, width=30, font=('Arial', 12))
entry_last_name.insert(0, "Enter Last Name...")
entry_last_name.grid(row=1, column=1, padx=10, pady=5, sticky='w')

# Screen Name
label_screen_name = tk.Label(frame2, text="Screen Name", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_screen_name.grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_screen_name = ttk.Entry(frame2, width=30, font=('Arial', 12))
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
gender_var = tk.IntVar()
male_rb = ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value=1, style='TButton')
male_rb.pack(side='left')
female_rb = ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value=2, style='TButton')
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
entry_email = ttk.Entry(frame2, width=30, font=('Arial', 12))
entry_email.insert(0, "Enter E-mail...")
entry_email.grid(row=6, column=1, columnspan=3, padx=10, pady=5, sticky='w')

# Phone
label_phone = tk.Label(frame2, text="Phone", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_phone.grid(row=7, column=0, padx=10, pady=5, sticky='e')
entry_phone = ttk.Entry(frame2, width=30, font=('Arial', 12))
entry_phone.insert(0, "Enter Phone...")
entry_phone.grid(row=7, column=1, columnspan=3, padx=10, pady=5, sticky='w')

# Password
label_password = tk.Label(frame2, text="Password", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_password.grid(row=8, column=0, padx=10, pady=5, sticky='e')
entry_password = ttk.Entry(frame2, width=30, font=('Arial', 12), show="*")
entry_password.grid(row=8, column=1, columnspan=3, padx=10, pady=5, sticky='w')

# Confirm Password
label_confirm_password = tk.Label(frame2, text="Confirm Password", bg='#242446', fg='#e9e59b', font=('Arial', 12))
label_confirm_password.grid(row=9, column=0, padx=10, pady=5, sticky='e')
entry_confirm_password = ttk.Entry(frame2, width=30, font=('Arial', 12), show="*")
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
check_agree = ttk.Checkbutton(frame_agree, variable=agree_var)
check_agree.grid(row=0, column=0, padx=5, pady=5, sticky='w')

# Frame 3: Buttons
frame3 = tk.Frame(root, bg='#e28406')
frame3.grid(row=2, column=0, columnspan=2, sticky='ew')

# Настройка стилей для кнопок
style = ttk.Style()
style.configure('TButton', font=('Arial', 14), padding=10, relief="flat")
style.map('TButton', background=[('active', '#fc4c4c'), ('!active', '#55d237')],
                     foreground=[('active', '#ffffff'), ('!active', '#ffffff')])

cancel_button = ttk.Button(frame3, text="Cancel", command=cancel, style='TButton')
cancel_button.pack(side='right', padx=10, pady=10)
submit_button = ttk.Button(frame3, text="Submit", command=submit, style='TButton')
submit_button.pack(side='right', padx=5, pady=10)

root.mainloop()
