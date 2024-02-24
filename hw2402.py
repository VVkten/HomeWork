import random
from tkinter import *
from tkinter import messagebox

root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'400x400+{int(w/2-200)}+{int(h/2-200)}')
root.title('Вгадай число')

min_value = StringVar()
max_value = StringVar()

maxSpr = 5
spr = 0
numb = None

def generate_number():
    # global generated_number, attempts_remaining
    global numb
    try:
        min = int(entryMin.get())
        max = int(entryMax.get())
        if min >= max:
            messagebox.showwarning('Зауваження', 'Перше число має бути меншим за друге!')
        else:
            numb = random.randint(min, max)
            print(f'Загадане число: {numb}')
            entryMax.config(state='disabled')
            entryMin.config(state='disabled')
            btn1.config(state='disabled')
            check_guess()
    except ValueError:
        messagebox.showerror('Помилка', 'Потрібно вводити цілі числа')

def check_guess():
    global numb
    global spr
    if spr < maxSpr:
        try:
            numberQ = int(entryWin.get())
            spr += 1
            if numberQ == numb:
                messagebox.showinfo('Результат', f'Ви вгадали число {numb}!')
            elif numberQ > numb:
                messagebox.showinfo('Результат', 'Загадане число менше!')
            else:
                messagebox.showinfo('Результат', 'Загадане число більше!')
        except:
            print('Не знаю чому Т-Т')
            # messagebox.showerror('Помилка', 'Потрібно вводити цілі числа')
    else:
        messagebox.showinfo('Кінець гри', f'Ви не вгадали число. Загадане число було: {numb}')

    labelSoW.place(x=10, y=150)
    entryWin.place(x=130, y=150)
    btn2.place(x=150, y=180)


labelMin = Label(root, text='Мінімальне число:')
labelMin.place(x=10, y=50)
entryMin = Entry(root, textvariable=min_value)
entryMin.place(x=135, y=50)

labelMax = Label(root, text='Максимальне число:')
labelMax.place(x=10, y=80)
entryMax = Entry(root, textvariable=max_value)
entryMax.place(x=135, y=80)

btn1 = Button(root, text='Генерувати', command=generate_number)
btn1.place(x=150, y=120)

btn2 = Button(root, text='Вгадати', command=check_guess)
btn2.place_forget()

entryWin = Entry(root)
entryWin.place_forget()

labelSoW = Label(root, text='Введіть число:')
labelSoW.place_forget()


root.mainloop()
