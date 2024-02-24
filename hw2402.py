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
numb = None

def generate_number():
    # global generated_number, attempts_remaining
    try:
        min_val = int(labelMin.get())
        max_val = int(labelMax.get())
        if min_val >= max_val:
            messagebox.showwarning('Зауваження', 'Перше число має бути меншим за друге!')
        else:
            numb = random.randint(min_val, max_val)
            labelMin.config(state='disabled')
            labelMax.config(state='disabled')
            btn1.config(state='disabled')
    except ValueError:
        messagebox.showerror('Помилка', 'Потрібно вводити цілі числа')



labelMin = Label(root, text='Мінімальне число:')
labelMin.place(x=10, y=50)
entryMin = Entry(root, textvariable=min_value)
entryMin.place(x=135, y=50)

labelMax = Label(root, text='Максимальне число:')
labelMax.place(x=10, y=80)
entryMax = Entry(root, textvariable=max_value)
entryMax.place(x=135, y=80)

btn1 = Button(root, text='Генерувати')
btn1.place(x=150, y=120)

btn2 = Button(root, text='Вгадати',
                      # command=check_guess
                      )
btn2.place_forget()

entryWin = Entry(root)
entryWin.place_forget()

labelSoW = Label(root, text='Введіть число:')
labelSoW.place_forget()


root.mainloop()
