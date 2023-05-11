import tkinter as t
from tkinter import messagebox
import random as rd
import pyperclip 
GREY = '#6c707a'

def gen_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters = [rd.choice(letters) for i in range (rd.randint(8, 10))]
    numbers = [rd.choice(numbers) for i in range (rd.randint(2, 4))]
    symbols = [rd.choice(symbols) for i in range (rd.randint(2, 4))]

    password_list = letters + numbers + symbols
    rd.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)

def append():
    site = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    if len(site) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title='Warning!', message="Don't leave the fields empty!")

    else:
        ok_cancel = messagebox.askokcancel(title='Confirm', message=f"These are the informations entered:\nPassword: {password}\nSite: {site}\nDo you really want to save?")

    if ok_cancel == True:
        f = open('data.txt', 'a')
        f.write(f'{site}  |  {email}  |  {password}\n')
        f.close()
        website_entry.delete(0, len(site))
        password_entry.delete(0, len(password))



window = t.Tk()
window.title("Password Manager.")
window.config(bg=GREY, padx=40, pady=40)


canvas = t.Canvas(width=200, height=200)
canvas.config(bg=GREY, highlightthickness=0)
locker_png = t.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = locker_png)
canvas.grid(row=0, column=1)


website_label = t.Label()
website_label.config(bg = GREY, text = 'Website:')
email_label = t.Label()
email_label.config(bg=GREY, text='Email/Username:')
password_label = t.Label()
password_label.config(bg= GREY, text='Password:')
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)


website_entry = t.Entry()
website_entry.config(bg=GREY, width=57)
website_entry.focus()
email_entry = t.Entry()
email_entry.config(bg=GREY, width=57)
email_entry.insert(0, 'davi.nasiamorim366@gmail.com')
password_entry = t.Entry()
password_entry.config(bg=GREY, width=38)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)


add_button = t.Button()
add_button.config(bg=GREY, text='Add', width= 49, command=append)
password_button = t.Button()
password_button.config(bg=GREY, width=15, text = 'Generate Password', command=gen_password)
add_button.grid(row=4, column=1, columnspan=2)
password_button.grid(row=3, column=2)


window.mainloop()