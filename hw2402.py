import random
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x250')
root.title('Вгадай число')

min_value = StringVar()
max_value = StringVar()

attempts_remaining = 5
current_attempt = 0
generated_number = None

min_label = Label(root, text='Мінімальне число:')
min_label.place(x=10, y=50)
min_entry = Entry(root, textvariable=min_value)
min_entry.place(x=135, y=50)

max_label = Label(root, text='Максимальне число:')
max_label.place(x=10, y=80)
max_entry = Entry(root, textvariable=max_value)
max_entry.place(x=135, y=80)

generate_button = Button(root, text='Генерувати')
generate_button.place(x=150, y=120)

root.mainloop()
