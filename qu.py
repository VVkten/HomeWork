from tkinter import *
from tkinter import ttk
from tkinter import filedialog


root = Tk()
root.title("Currency Converter")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'550x450+{int(w/2-275)}+{int(h/2-225)}')

def TruFal():
    t = 0
    if qu1.get() == 3:
        t += 1
    if qu2.get() == 1:
        t += 1
    if qu3.get() == 2:
        t += 1
    if qu4.get() == 2:
        t += 1
    if qu5.get() == 2:
        t += 1
    if qu6.get() == 2:
        t += 1

    lb7 = Label(fr7, text=f"Ваша оцінка {t * 2}", font=(None, 12))
    lb7.pack()

    btnSav = Button(fr7, text='Зберегти оцінку', command=Sav)
    btnSav.pack(padx=20, pady=20)

def Sav():
    global t
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f'Оцінка: {t*2}')
        print("Дані збережено у файл", filename)


note = ttk.Notebook(root)
note.pack(fill=BOTH, expand=True)

fr0 = ttk.Frame(note)
fr1 = ttk.Frame(note)
fr2 = ttk.Frame(note)
fr3 = ttk.Frame(note)
fr4 = ttk.Frame(note)
fr5 = ttk.Frame(note)
fr6 = ttk.Frame(note)

fr7 = ttk.Frame(note)

fr6.pack(fill=BOTH, expand=True)
fr5.pack(fill=BOTH, expand=True)
fr4.pack(fill=BOTH, expand=True)
fr3.pack(fill=BOTH, expand=True)
fr2.pack(fill=BOTH, expand=True)
fr0.pack(fill=BOTH, expand=True)
fr1.pack(fill=BOTH, expand=True)
fr7.pack(fill=BOTH, expand=True)

# додаємо фрейми в якості закладок
note.add(fr0, text="Вступ")
note.add(fr1, text="1")
note.add(fr2, text="2")
note.add(fr3, text="3")
note.add(fr4, text="4")
note.add(fr5, text="5")
note.add(fr6, text="6")
note.add(fr7, text="Результат")

lb0 = Label(fr0, text="Вітаю вас на короткому опитувані Python", font=(None,13))
lb0.pack(padx=20, pady=20)



lb1 = Label(fr1, text="Що таке коментарі в Python та як їх додавати до коду?", font=(None, 12))
lb1.pack()
qu1 = IntVar()
a1 = Radiobutton(fr1, text='a) Коментарі - це фрагменти коду, які виконуються програмою', value=1, variable=qu1)
a1.pack(padx=20, pady=20)
b1 = Radiobutton(fr1, text='b) Коментарі - це інструкції, які пропускаються під час виконання програми.', value=2, variable=qu1)
b1.pack(padx=20, pady=20)
c1 = Radiobutton(fr1, text='c) Коментарі - це текстові пояснення у коді, які ігноруються інтерпретатором Python.', value=3, variable=qu1)
c1.pack(padx=20, pady=20)

lb2 = Label(fr2, text="Як вивести текст на консоль у Python?", font=(None, 12))
lb2.pack()
qu2 = IntVar()
a2 = Radiobutton(fr2, text='a) print("Текст, який потрібно вивести")', value=1, variable=qu2)
a2.pack(padx=20, pady=20)
b2 = Radiobutton(fr2, text='b) display("Текст, який потрібно вивести")', value=2, variable=qu2)
b2.pack(padx=20, pady=20)
c2 = Radiobutton(fr2, text='c) show("Текст, який потрібно вивести")', value=3, variable=qu2)
c2.pack(padx=20, pady=20)

lb3 = Label(fr3, text="Як визначити довжину списку у Python?", font=(None, 12))
lb3.pack()
qu3 = IntVar()
a3 = Radiobutton(fr3, text='a) length(list)', value=1, variable=qu3)
a3.pack(padx=20, pady=20)
b3 = Radiobutton(fr3, text='b) len(list)', value=2, variable=qu3)
b3.pack(padx=20, pady=20)
c3 = Radiobutton(fr3, text='c) size(list)', value=3, variable=qu3)
c3.pack(padx=20, pady=20)

lb4 = Label(fr4, text="Як використовувати умовні конструкції (if-else) в Python?", font=(None, 12))
lb4.pack()
qu4 = IntVar()
a4 = Radiobutton(fr4, text='a) if condition { } else { }', value=1, variable=qu4)
a4.pack(padx=20, pady=20)
b4 = Radiobutton(fr4, text='b) if condition: ... else: ...', value=2, variable=qu4)
b4.pack(padx=20, pady=20)
c4 = Radiobutton(fr4, text='c) if condition then { } else { }', value=3, variable=qu4)
c4.pack(padx=20, pady=20)

lb5 = Label(fr5, text="Що таке оператори 'and', 'or' та 'not' у Python та як вони працюють?", font=(None, 12))
lb5.pack()
qu5 = IntVar()
a5 = Radiobutton(fr5, text='a) "and" - логічне НЕ, "or" - логічне АБО, "not" - логічне І', value=1, variable=qu5)
a5.pack(padx=20, pady=20)
b5 = Radiobutton(fr5, text='b)  "and" - логічне І, "or" - логічне АБО, "not" - логічне НЕ', value=2, variable=qu5)
b5.pack(padx=20, pady=20)
c5 = Radiobutton(fr5, text='c) "and" - логічне АБО, "or" - логічне І, "not" - логічне НЕ', value=3, variable=qu5)
c5.pack(padx=20, pady=20)

lb6 = Label(fr6, text="Як встановити значення змінної в Python?", font=(None, 12))
lb6.pack()
qu6 = IntVar()
a6 = Radiobutton(fr6, text='a) var x = 5', value=1, variable=qu6, command=TruFal)
a6.pack(padx=20, pady=20)
b6 = Radiobutton(fr6, text='b) x = 5', value=2, variable=qu6, command=TruFal)
b6.pack(padx=20, pady=20)
c6 = Radiobutton(fr6, text='c) set x = 5', value=3, variable=qu6, command=TruFal)
c6.pack(padx=20, pady=20)



root.mainloop()
