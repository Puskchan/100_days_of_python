from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pswd():
    pass_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letter = [password_list.append(random.choice(letters)) for _ in range(nr_letters)]

    symbol = [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]

    number = [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password1 = ""
    for char in password_list:
        password1 += char

    pass_entry.insert(0, password1)
    pyperclip.copy(password1)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web_name = web_entry.get()
    uname = email_entry.get()
    pass_w = pass_entry.get()

    if pass_w != "" and web_name != "":
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Email: {web_name}\n"
                                                                     f"Password: {pass_w}\n"
                                                                     f"Is it okay to save?")

        if is_ok:
            with open('data.txt', "a") as dat:
                dat.write(f"{web_name}: {uname} | {pass_w}\n")

            web_entry.delete(0, END)
            pass_entry.delete(0, END)
    else:
        messagebox.showinfo(title="OOPS", message="Please don't leave any entry empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website = Label(text="Website:", font=("Courier", 10, "bold"))
website.grid(column=0, row=1)

email_username = Label(text="Email/Username:", font=("Courier", 10, "bold"))
email_username.grid(column=0, row=2)

password = Label(text="Password:", font=("Courier", 10, "bold"))
password.grid(column=0, row=3)

web_entry = Entry(width=54)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=54)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "adipusk@gmail.com")

pass_entry = Entry(width=35)
pass_entry.grid(column=1, row=3)

pass_gen = Button(text="Generate Password", command=pswd)
pass_gen.grid(column=2, row=3)

add_entry = Button(text="Add", width=46, command=save)
add_entry.grid(column=1, row=4, columnspan=2)

window.mainloop()
