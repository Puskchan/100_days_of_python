from tkinter import *


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)


# Label

my_label = Label(text="Miles", font=("Arial", 10, "bold"))
my_label.grid(column=3, row=0)

# Label

my_label = Label(text="is equal to", font=("Arial", 10, "bold"))
my_label.grid(column=0, row=2)

# Label

my_label = Label(text="Km", font=("Arial", 10, "bold"))
my_label.grid(column=3, row=2)

# Entry

in_put = Entry(width=10)
in_put.grid(column=2, row=0)


# Button


def button():
    print("I got clicked")
    my_label.config(text=convert(in_put.get()))
    # or you can write my_label["text"] = "text"


button = Button(text="Calculate", command=button)
button.grid(column=2, row=3)


def convert(n=0):
    return str(round(int(n) * 1.6, 2))


# Label

my_label = Label(text="0", font=("Arial", 10, "bold"))
my_label.grid(column=2, row=2)


window.mainloop()