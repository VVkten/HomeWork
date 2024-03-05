from tkinter import *
import math
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
        Button(root, text=button, padx=30, pady=20).grid(row=row, column=col)
    elif button == 'C':
        Button(root, text=button, padx=30, pady=20).grid(row=row, column=col)
    elif button == 'sin':
        Button(root, text=button, padx=30, pady=20).grid(row=row, column=col)
    elif button == 'Вихід':
        Button(root, text=button, padx=30, pady=20).grid(row=row, column=col)
    else:
        Button(root, text=button, padx=30, pady=20).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()