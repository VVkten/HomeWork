from tkinter import *


if __name__ == "__main__":
    click = 0
    labelT = "Початковий напис"

    root = Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.resizable(width=False, height=False)
    root.geometry(f'300x300+{int(w / 2 - 150)}+{int(h / 2 - 150)}')

    label = Label(root, text=labelT)
    label.pack(pady=20)

    root.mainloop()
