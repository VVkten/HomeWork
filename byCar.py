from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox

def changCar():
    if var1.get() == 1:
        NewCar()
    elif var1.get() == 2:
        Car()

def pr_selection():
    global tx2
    tx2.delete(1.0, END)
    result = f"Тип автомобіля: {'Нова машина' if var1.get() == 1 else 'Стара машина'}\n"
    result += f"Марка автомобіля: {lis1.get()}\n"
    result += f"Об'єм двигуна: {lis2.get()}\n"
    result += f"Континент виробник: {lis3.get()}\n"
    result += f"Вид двигуна: {'Дизель' if dv.get() == 'Дизель' else 'Бензин'}\n"
    result += f"Колір автомобіля: {color_var.get()}\n"
    if var1.get() == 2:
        result += f"Стаж використання автомобіля: {lis4.get()}"
    tx2.insert(END, result)


def clear_selection():
    lis1.set('')
    lis2.set('')
    lis3.set('')
    dv.set(0)
    color_var.set('')
    lis4.set('')
    tx2.delete(1.0, END)


def save_selection():
    selected_items = []

    # Додавання обраних елементів у список
    selected_items.append(f"Попередні дані про автомобіль: {var1.get()}")
    selected_items.append(f"Марка автомобіля: {lis1.get()}")
    selected_items.append(f"Об'єм двигуна: {lis2.get()}")
    selected_items.append(f"Континент виробника: {lis3.get()}")
    selected_items.append(f"Вид двигуна: {dv.get()}")
    selected_items.append(f"Колір: {color_var.get()}")
    if var1.get() == 2:
        selected_items.append(f"Стаж використання: {lis4.get()}")

    # Отримання тексту з обраними елементами
    result_text = "\n".join(selected_items)

    # Запис до файлу
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(result_text)
        print("Дані збережено у файл", filename)

def update_color(*args):
    color = color_var.get()
    tx['background'] = color

def NewCar():
    lis1.pack()
    fr2.place(x=10, y=90)
    lis2.pack()
    fr3.place(x=220, y=90)
    lis3.pack()
    fr4.place(x=430, y=90)
    d1.pack()
    d2.pack()
    fr5.place(x=10, y=140, width=146, height=80)
    lb.place(x=220, y=135)
    spinbox.place(x=220, y=155)
    tx.place(x=220, y=175)
    lb2.place(x=10, y=230)
    tx2.place(x=10, y=250)
    scrollbar.place(x=570, y=250, height=70)
    btnFinish.place(x=160, y=330)
    btnNew.place(x=300, y=330)
    btnSaved.place(x=159, y=360)

def Car():
    lis1.pack()
    fr2.place(x=10, y=90)
    lis2.pack()
    fr3.place(x=220, y=90)
    lis3.pack()
    fr4.place(x=430, y=90)
    d1.pack()
    d2.pack()
    fr5.place(x=10, y=140, width=146, height=80)
    lb.place(x=220, y=135)
    spinbox.place(x=220, y=155)
    tx.place(x=220, y=175)
    lis4.pack()
    fr6.place(x=430, y=140)

    lb2.place(x=10, y=230)
    tx2.place(x=10, y=250)
    scrollbar.place(x=570, y=250, height=70)
    btnFinish.place(x=160, y=330)
    btnNew.place(x=300, y=330)
    btnSaved.place(x=159, y=360)

root = Tk()
root.title("Вибір автомобіля")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'600x400+{int(w / 2 - 300)}+{int(h / 2 - 200)}')
root.resizable(width=False, height=False)

var1 = IntVar()

fr1 = LabelFrame(root, text="Виберіть попередні дані про автомобіть")
ch1 = Radiobutton(fr1, value=1, text='Нова машина', variable=var1)
ch2 = Radiobutton(fr1, value=2, text='Стара машина', variable=var1)
ch1.pack()
ch2.pack()
fr1.place(x=100, y=15)

btnStart = Button(root, text='Основні питання',
                  command=changCar,
                  relief='groove')
btnStart.place(x=380, y=39)

model = ['BMW', 'Mercedes', 'VOLKSWAGEN', 'Mazda', 'TOYOTA', 'SKODA', 'RENAULT', 'NISSAN']
selectCar = StringVar(root)

fr2 = LabelFrame(root, text='Марка автомобілів')
lis1 = Combobox(fr2, values=model, state='readonly')
lis1.set('Mercedes')
# lis1.pack()
# fr2.place(x=10, y=90)

litr = ['менше 1200', '1200-1500', '1501-2200', 'більше 2200']
fr3 = LabelFrame(root, text="Об'єм двигуна")
lis2 = Combobox(fr3, values=litr, state='readonly')
lis2.set('1200-1500')
# lis2.pack()
# fr3.place(x=220, y=90)

hm = ['Західна Європа', 'Східна Європа', 'Азія', 'Америка']
fr4 = LabelFrame(root, text="Континент виробник")
lis3 = Combobox(fr4, values=hm, state='readonly')
lis3.set('Азія')
# lis3.pack()
# fr4.place(x=430, y=90)

fr5 = LabelFrame(root, text="Вид двигуна")
dv = IntVar()
d1 = Radiobutton(fr5, text='Дизель', value=1, variable=dv)
d2 = Radiobutton(fr5, text='Бензин', value=2, variable=dv)
dv.set(1)
# d1.pack()
# d2.pack()
# fr5.place(x=10, y=140, width=146, height=80)

lb = Label(root, text='Колір')

colo = ['red', 'blue', 'pink', 'green', 'purple', 'yellow', 'black', 'white']
color_var = StringVar(root)
color_var.set(colo[0])  # Встановлюємо початкове значення
color_var.trace_add('write', update_color)  # Пов'язуємо зміну значення з функцією
tx = Text(root, background=color_var.get(), width=16, height=2)
spinbox = Spinbox(root, values=colo, textvariable=color_var, wrap=True, command=update_color)
# lb.place(x=220, y=135)
# spinbox.place(x=220, y=155)
# tx.place(x=220, y=175)

old = ['до 5 років', '6-10 років', '11-15 років', 'більше 15 років']
fr6 = LabelFrame(root, text="Скільки років")
lis4 = Combobox(fr6, values=old, state='readonly')
lis4.set('до 5 років')
# lis4.pack()
# fr6.place(x=430, y=140)

lb2 = Label(root, text="Результат вибору")
tx2 = Text(root, width=70, height=4)
# lb2.place(x=10, y=230)
# tx2.place(x=10, y=250)
scrollbar = Scrollbar(root, command=tx2.yview)
# scrollbar.place(x=560, y=250, height=70)
tx2.config(yscrollcommand=scrollbar.set)

btnFinish = Button(root, text="Результат вибору", relief='groove', command=pr_selection)
btnNew = Button(root, text='Нове опитування', relief='groove', command=clear_selection)
# btnFinish.place(x=160, y=330)
# btnNew.place(x=300, y=330)

btnSaved = Button(root, text="Зберегти результат", width=34, height=1, relief='groove', command=save_selection)
# btnSaved.place(x=159, y=360)

root.mainloop()
