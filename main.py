from tkinter import *
import pandas as pd
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = 8
    nr_symbols = 4
    nr_numbers = 8

    pass_entry.delete(0, END)

    pass_letters = [random.choice(letters) for _ in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password = pass_numbers + pass_letters + pass_symbols

    random.shuffle(password)
    new_gen_password = ''.join(password)
    pass_entry.insert(0, new_gen_password)
    pyperclip.copy(new_gen_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
df = pd.DataFrame()


def save():
    website = website_entry.get()
    email = user_entry.get()
    password = pass_entry.get()

    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showwarning(title='warning', message="Do Not let empty fields!")
    else:
        is_ok = messagebox.askokcancel(title="password confirmation",
                                       message=f"Website:  {website}\nEmail:  {email}\nPassword:  "
                                               f"{password}\n\nDo you want to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website}|{email}|{password}\n")
            website_entry.delete(0, END)
            pass_entry.delete(0, END)

            global df
            data_dic = {"website": [website], "email": [email], "password": [password]}
            new_data = pd.DataFrame(data_dic)
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_excel("passwords_data.xlsx")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="website:")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/User Name:")
user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
user_entry = Entry(width=52)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, 'xyz@gmail.com')

pass_entry = Entry(width=33)
pass_entry.grid(row=3, column=1)

pass_gen_BT = Button(text="Generate Password", command=generate_password)
pass_gen_BT.grid(row=3, column=2)

Add_BT = Button(text="ADD", width=44, command=save)
Add_BT.grid(row=4, column=1, columnspan=2)

window.mainloop()
