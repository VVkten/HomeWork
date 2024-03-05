from tkinter import *
import math

# Функція для очищення поля введення
def clear():
    entry.delete(0, END)

# Функція для введення числа та оператора
def button_click(symbol):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + symbol)

# Функція для обчислення sin
def calculate_sin():
    try:
        num = float(entry.get())
        result = math.sin(num)
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Помилка")

# Функція для обчислення виразу
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Помилка")

# Створення головного вікна
root = Tk()
root.title("Калькулятор")

# Створення поля введення
entry = Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Створення кнопок для калькулятора
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', 'sin', 'Вихід'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        Button(root, text=button, padx=30, pady=20, command=calculate).grid(row=row, column=col)
    elif button == 'C':
        Button(root, text=button, padx=30, pady=20, command=clear).grid(row=row, column=col)
    elif button == 'sin':
        Button(root, text=button, padx=30, pady=20, command=calculate_sin).grid(row=row, column=col)
    elif button == 'Вихід':
        Button(root, text=button, padx=30, pady=20, command=root.destroy).grid(row=row, column=col)
    else:
        Button(root, text=button, padx=30, pady=20, command=lambda b=button: button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
