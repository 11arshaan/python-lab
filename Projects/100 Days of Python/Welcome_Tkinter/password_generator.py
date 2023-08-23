import tkinter
from tkinter import messagebox
from handle_password import random_password
import json


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

# add 20 padding to canvas

canvas = tkinter.Canvas(width=200, height=200)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = tkinter.Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)
search_button = tkinter.Button(text="Search", width=13)
search_button.grid(row=1, column=2)

# ---------------------------- SAVE PASSWORD ------------------------------- #


# Add password function
def add_password(event):
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        # Error Messagebox
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return

    # Confirm Messagebox
    is_ok = messagebox.askokcancel(title=website,
                                   message=f"These are the details entered: \nEmail: {email} \nPassword: {password} "
                                           f"\nIs it ok to save?")
    if is_ok:
        try:
            with open("data.json", "r") as json_file:
                # Reading old data
                data = json.load(json_file)
        except FileNotFoundError:
            with open("data.json", "w") as json_file:
                json.dump(new_data, json_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            # Saving updated data
            with open("data.json", "w") as json_file:
                json.dump(data, json_file, indent=4)
        finally:
            website_entry.delete(0, tkinter.END)
            email_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


add_button.bind("<Button-1>", add_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def search_password(event):
    website = website_entry.get()
    try:
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Password: {password}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No passwords stored.")
    except KeyError:
        messagebox.showinfo(title="Error", message="No details for the website exists.")
    finally:
        website_entry.delete(0, tkinter.END)


search_button.bind("<Button-1>", search_password)


# Generate password function
def generate_password(event):
    password_entry.delete(0, tkinter.END)
    password = random_password()
    password_entry.insert(0, "".join(password))


generate_password_button.bind("<Button-1>", generate_password)


window.mainloop()
