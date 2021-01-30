from tkinter import *
from tkinter import messagebox
from password_generator import RandomPassword
import pyperclip
import json

BG_IMG = "lock_logo.png"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pw = RandomPassword()
    new_password = pw.generate_password()
    password_entry.delete(0, END)
    password_entry.insert(END, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = (website_entry.get()).lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any empty fields")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Confirm details:\n\n "
                                                              f"Email - {email}\n"
                                                              f"Password- {password}\n\nis it okay to save?")

        if is_ok:
            try:
                with open("password_data.json", "r") as data_file:

                    # read old data
                    data = json.load(data_file)
                    # print(data)

                    # update data
                    data.update(new_data)

                with open("password_data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            except FileNotFoundError:
                with open("password_data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD------------------------------- #
def search():
    website = (website_entry.get()).lower()
    website = website.lower()
    try:
        with open("password_data.json", "r") as data_file:
            # read old data
            data = json.load(data_file)
        email = data[website]["email"]
        password = data[website]["password"]
    except FileNotFoundError:
        messagebox.showerror(title="Error!", message="No passwords saved.")
    except KeyError:
        messagebox.showerror(title="Error!", message="Password does not exist.")
    else:
        messagebox.askokcancel(title=website, message=f"email: {email}\n\npassword: {password}")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.minsize(width=300, height=300)

canvas = Canvas(width=200, height=200)
bg_img = PhotoImage(file=BG_IMG)
canvas.create_image(110, 100, image=bg_img)
canvas.grid(column=2, row=1)

# LABELS
website_label = Label(text="Website:")
website_label.grid(column=1, row=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=1, row=3)

password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

# ENTRIES
website_entry = Entry(width=32)
website_entry.grid(column=2, row=2, columnspan=1)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.insert(END, "bethpritchard97@gmail.com")
email_entry.grid(column=2, row=3, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(column=2, row=4)

# BUTTONS
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=3, row=4)

add_button = Button(width=42, text="Add", command=save)
add_button.grid(column=2, row=5, columnspan=2)

search_button = Button(text = "Search", width = 14, command=search)
search_button.grid(column=3, row=2)


window.mainloop()
