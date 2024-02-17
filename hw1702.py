from tkinter import *


if __name__ == "__main__":
    click = 0
    labelT = "Початковий напис"

    root = Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.resizable(width=False, height=False)
    root.geometry(f'300x300+{int(w / 2 - 150)}+{int(h / 2 - 150)}')

    label = Label(root, text=labelT,
                        fg='magenta')
    label.pack(pady=20)

    btnChange = Button(root,
                       text="Натисни",
                       bg='pink',
                       font=(None, 30),
                       fg='cyan',
                       padx=20, pady=10
                       # command=change_label
                       )
    btnChange.pack()

    clickLabel = Label(root,
                        text=f"Кількість клацань: {click}",
                        fg='magenta')
    clickLabel.pack(pady=10)

    root.mainloop()
