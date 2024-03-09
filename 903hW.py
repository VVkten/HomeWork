from tkinter import *
from tkinter import ttk

# Курси обміну валют
exchange_rates = {
    'USD': {'UAH': 27.5, 'EUR': 0.85, 'PLN': 3.75},
    'UAH': {'USD': 0.036, 'EUR': 0.031, 'PLN': 0.14},
    'EUR': {'USD': 1.18, 'UAH': 32.5, 'PLN': 4.5},
    'PLN': {'USD': 0.27, 'UAH': 7.1, 'EUR': 0.22}
}

root = Tk()
root.title("Currency Converter")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'250x250+{int(w/2-125)}+{int(h/2-125)}')

frCvar = StringVar()
toCvar = StringVar()
AmVar = DoubleVar()

frCurrencyL = ttk.Label(root, text="Валюта:")
frCurrencyL.place(x=10, y=20)

frCurrencyC = ttk.Combobox(root, textvariable=frCvar, width=20)
frCurrencyC['values'] = ["USD", "UAH", "EUR", "PLN"]
frCurrencyC.place(x=100, y=20)
frCurrencyC.set("USD")

toCurrencyL = ttk.Label(root, text="Ваша валюта:")
toCurrencyL.place(x=10, y=45)

toCurrencyC = ttk.Combobox(root, textvariable=toCvar, width=20)
toCurrencyC['values'] = ["USD", "UAH", "EUR", "PLN"]
toCurrencyC.place(x=100, y=45)
toCurrencyC.set("UAN")

amountLabel = ttk.Label(root, text="Сума:")
amountLabel.place(x=50, y=85)
amountEntry = ttk.Entry(root, textvariable=AmVar, width=20)
amountEntry.place(x=100, y=85)

convertBtn = ttk.Button(root, text="Конвертувати")
convertBtn.place(x=90, y=125)

result = ttk.Label(root, text="")
result.place(x=10, y=150)

root.mainloop()
