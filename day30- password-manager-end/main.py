from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def search_website():
    website = entry_website.get()
    try:
        with open("my_passowrd.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Data not found", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showwarning(title="Website not found", message=f"No details for the {website} exists.")


def generate_password():
    entry_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    entry_password.insert(0, f"{password}")
    pyperclip.copy(password)
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {website: {"email": email,
                          "password": password}}
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please do not leave any field empty!")
    else:
        try:
            with open("my_passowrd.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("my_passowrd.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("my_passowrd.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
entry_website = Entry()
entry_website.grid(row=1, column=1, sticky="ew")
entry_website.focus()
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)
entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2, sticky="ew")
entry_email.insert(0, "quans1991@gmail.com")

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)
entry_password = Entry(width=21)
entry_password.grid(row=3, column=1, sticky="ew")

button_gen_passwod = Button(text="Generate Password", command=generate_password)
button_gen_passwod.grid(row=3, column=2, sticky="ew")

button_add = Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2, sticky="ew")

button_search = Button(text="Search", command=search_website, highlightthickness=0)
button_search.grid(row=1, column=2, sticky="ew")
window.mainloop()
