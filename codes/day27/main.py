import tkinter as t

window = t.Tk()
window.title("Test")
window.minsize(500, 300)

label = t.Label(text = "Test!", font = ("Arial", 24, "bold"))  #text
label.pack()


def button_clicked():
    label.config(text=input.get())
    

button = t.Button(text="Click", command = button_clicked)
button.pack()



input = t.Entry(width=10)
input.pack()



window.mainloop()