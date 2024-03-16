from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox

def save_selection(selected_car):
    selected_items = []

    # Додавання обраних елементів у список
    selected_items.append(f"Попередні дані про автомобіль: {var1.get()}")
    selected_items.append(f"Марка автомобіля: {lis1.get()}")
    selected_items.append(f"Об'єм двигуна: {lis2.get()}")
    selected_items.append(f"Континент виробника: {lis3.get()}")
    selected_items.append(f"Вид двигуна: {dv.get()}")
    selected_items.append(f"Колір: {color_var.get()}")
    selected_items.append(f"Стаж використання: {lis4.get()}")

    # Отримання тексту з обраними елементами
    result_text = "\n".join(selected_items)

    # Запис до файлу
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            file.write(result_text)
        print("Дані збережено у файл", filename)

def NewCAr():
    print('New')

def Car():
    print('Old')


root = Tk()
root.title("Вибір автомобіля")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'600x400+{int(w / 2 - 300)}+{int(h / 2 - 200)}')
root.resizable(width=False, height=False)

var1 = IntVar()

fr1 = LabelFrame(root, text="Виберіть попередні дані про автомобіть")
ch1 = Radiobutton(fr1, value='Нова машина', text='Нова машина' , variable=var1)
ch2 = Radiobutton(fr1, value='Іноземного виробництва', text='Іноземного виробництва', variable=var1)
ch1.pack()
ch2.pack()
fr1.place(x=100, y=15)

btnStart = Button(root, text='Основні питання', command=Car, relief='groove')
btnStart.place(x=380, y=39)

model = ['BMW', 'Mercedes', 'VOLKSWAGEN', 'Mazda', 'TOYOTA', 'SKODA', 'RENAULT', 'NISSAN']
selectCar = StringVar(root)

fr2 = LabelFrame(root, text='Марка автомобілів')
lis1 = Combobox(fr2, values=model, state='readonly')
lis1.set('Mercedes')
lis1.pack()
fr2.place(x=10, y=90)

litr = ['менше 1200', '1200-1500', '1501-2200', 'більше 2200']
fr3 = LabelFrame(root, text="Об'єм двигуна")
lis2 = Combobox(fr3, values=litr, state='readonly')
lis2.set('1200-1500')
lis2.pack()
fr3.place(x=220, y=90)

hm = ['Західна Європа', 'Східна Європа', 'Азія', 'Америка']
fr4 = LabelFrame(root, text="Континент виробник")
lis3 = Combobox(fr4, values=hm, state='readonly')
lis3.set('Азія')
lis3.pack()
fr4.place(x=430, y=90)

fr5 = LabelFrame(root, text="Вид двигуна")
dv = IntVar()
d1 = Radiobutton(fr5, text='Дизель', value='Дизель', variable=dv, indicator=1)
d2 = Radiobutton(fr5, text='Бензин', value='Бензин', variable=dv, indicator=1)
d1.pack()
d2.pack()
fr5.place(x=10, y=140, width=146, height=80)

def update_color(*args):
    color = color_var.get()
    tx['background'] = color

lb = Label(root, text='Колір')

colo = ['red', 'blue', 'pink', 'green', 'purple', 'yellow', 'black', 'white']
color_var = StringVar(root)
color_var.set(colo[0])  # Встановлюємо початкове значення
color_var.trace_add('write', update_color)  # Пов'язуємо зміну значення з функцією

tx = Text(root, background=color_var.get(), width=16, height=2)
spinbox = Spinbox(root, values=colo,textvariable=color_var, wrap=True, command=update_color)
# cl = spinbox.get()
lb.place(x=220, y=135)
spinbox.place(x=220, y=155)
tx.place(x=220, y=175)

old = ['до 5 років', '6-10 років', '11-15 років', 'більше 15 років']
fr6 = LabelFrame(root, text="Скільки років")
lis4 = Combobox(fr6, values=old, state='readonly')
lis4.set('до 5 років')
lis4.pack()
fr6.place(x=430, y=140)

lb2 = Label(root, text="Результат вибору")
tx2 = Text(root, width=70, height=4)
lb2.place(x=10, y=230)
tx2.place(x=10, y=250)

btnFinish = Button(root, text="Результат вибору", relief='groove')
btnNew = Button(root, text='Нове опитування', relief='groove')
btnFinish.place(x=160, y=330)
btnNew.place(x=300, y=330)

btnSaved = Button(root, text="Зберегти результат", width=34, height=1, relief='groove', command=save_selection)
btnSaved.place(x=159, y=360)


root.mainloop()
