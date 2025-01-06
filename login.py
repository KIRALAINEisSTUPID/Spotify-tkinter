import webbrowser
from tkinter import (Tk, Frame, LabelFrame, Label, Entry, Spinbox, Button, messagebox,StringVar,
                     DISABLED, Menu, Menubutton)
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os

from database import db




root = Tk()

logo = ImageTk.PhotoImage(Image.open("pictures/icon.png"))
root.iconphoto(False, logo)

root.configure(bg="#121212")
root.title("Login")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
center_x = int(width/2 - 525/2)
center_y = int(height/2 - 500/2)
root.geometry(f"525x500+{center_x}+{center_y}")

email_entry = Entry(root, font=("Arial", 35), bg="#121212", fg="white",justify="center")
email_entry.insert(0, "Email")
email_entry.place(y=100)

password_entry = Entry(root, font=("Arial", 35), bg="#121212", fg="white",justify="center")
password_entry.insert(0, "Password")
password_entry.place(y=200)

def login():
    email = email_entry.get()
    password = password_entry.get()
    user = db.get_user(email=email, password=password)
    if user:
        messagebox.showinfo(title="Success", message="Login successful")
        root.destroy()
        os.system("python Nazorat.py")
    else:
        messagebox.showerror(title="Error", message="Invalid email or password")

button = Button(root, text="Login", font=("Arial", 35), bg="#19E68C", fg="black",command=login)
button.place(x=150,y=300)
root.mainloop()