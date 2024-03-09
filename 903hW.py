from tkinter import *
from tkinter import ttk

def convert_currency():
    global frCvar, toCvar, AmVar, exchange_rates

    from_currency = frCvar.get()
    to_currency = toCvar.get()
    amount = AmVar.get()

    rate = exchange_rates[from_currency][to_currency]
    converted_amount = amount * rate

    result = ttk.Label(root, text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    result.place(x=50, y=102)



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
root.configure(background='black')

frCvar = StringVar()
toCvar = StringVar()
AmVar = DoubleVar()

style = ttk.Style()
style.configure("TLabel", foreground="lime", background="black")
# style.configure("TButton", foreground="black", background="lime", font=("Arial", 10, "bold"))
style.configure("TEntry", foreground="lime", background="black")
style.configure("TCombobox", foreground="lime", background="black", selectforeground="lime", selectbackground="black")


frCurrencyL = ttk.Label(root, text="Валюта:", style='TLabel')
frCurrencyL.place(x=10, y=20)

frCurrencyC = ttk.Combobox(root, textvariable=frCvar, width=20, state='readonly', style='TCombobox')
frCurrencyC['values'] = ["USD", "UAH", "EUR", "PLN"]
frCurrencyC.place(x=100, y=20)
frCurrencyC.set("USD")

toCurrencyL = ttk.Label(root, text="Ваша валюта:", style='TLabel')
toCurrencyL.place(x=10, y=45)

toCurrencyC = ttk.Combobox(root, textvariable=toCvar, width=20, state='readonly', style='TCombobox')
toCurrencyC['values'] = ["USD", "UAH", "EUR", "PLN"]
toCurrencyC.place(x=100, y=45)
toCurrencyC.set("UAH")

amountLabel = ttk.Label(root, text="Сума:", style='TLabel')
amountLabel.place(x=50, y=75)
amountEntry = ttk.Entry(root, textvariable=AmVar, width=20, style='TEntry')
amountEntry.place(x=100, y=75)

convertBtn = Button(root, text="Конвертувати", command=convert_currency, foreground="black", background="lime")

convertBtn.place(x=90, y=125)

root.mainloop()
