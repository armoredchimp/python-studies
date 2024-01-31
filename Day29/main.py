from tkinter import *
import random
import os
import pyperclip
from tkinter import messagebox
print(os.getcwd())

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    pass_entry.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list.extend(random.choice(letters) for _ in range(nr_letters))
    password_list.extend(random.choice(symbols) for _ in range(nr_symbols))
    password_list.extend(random.choice(numbers) for _ in range(nr_numbers))

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)


def save_output():
    web_output = website_entry.get()
    email_output = email_entry.get()
    pass_output = pass_entry.get()

    if len(web_output) == 0 or len(pass_output) == 0:
        no = messagebox.showinfo(
            title='Nice work, you fool!', message='Entries must have more than zero chars')
        return
    yes = messagebox.askokcancel(
        title=web_output, message=f'Details entered: \nEmail: {email_output}\nPassword: {pass_output}\nOk? You got problem with this? Cancel or accept.')

    if yes:
        with open('data.txt', 'a') as file:
            file.write(f'{web_output} | {email_output} | {pass_output}\n')

    website_entry.delete(0, END)
    # email_entry.delete(0, END)
    pass_entry.delete(0, END)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username')
email_label.grid(row=2, column=0)
pass_label = Label(text='Password')
pass_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "nope@fakemail.com")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text='Add', width=36, command=save_output)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
