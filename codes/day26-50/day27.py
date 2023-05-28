import tkinter as t

window = t.Tk()
window.title("Mile to Km Converter!")
window.minsize(200, 100)
window.config(padx= 35, pady=20)  #distance from the axes.


entry = t.Entry(width=10)
entry.grid(column=1, row = 0)


miles_label = t.Label(text="Miles")
is_equal_label = t.Label(text="Is iqual to: ")
km_label = t.Label(text="Km")
km_value = t.Label(text="0")
miles_label.grid(column=2, row=0)
is_equal_label.grid(column=0, row=1)
km_value.grid(column=1, row=1)
km_label.grid(column=2, row=1)


def calculate():
    km_value.config(text = f"{float(entry.get()) * 1.609}")

button = t.Button(text="Calculate.", command= calculate, width=8)
button.grid(column=1, row=2)



window.mainloop()