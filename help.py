import webbrowser
from tkinter import (Tk, Frame, LabelFrame, Label, Entry, Spinbox, Button, messagebox,StringVar,
                     DISABLED, Menu, Menubutton)
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os

root = Tk()
root.title("♬Spotify-♪ HELP♩")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
center_x = int(width / 2 - 700/ 2)
center_y = int(height / 2 - 500 / 2)
root.geometry(f"700x500+{center_x}+{center_y}")
root.configure(bg="#121212")
logo = ImageTk.PhotoImage(Image.open("pictures/icon.png"))
root.iconphoto(False, logo)



def exit(event=None):
    root.destroy()
    os.system("python Nazorat.py")







label = Label(root, text="what do you need help with?", font=("Arial", 20, "bold"), bg="#121212", fg="white")
label.grid(row=0, column=1,columnspan=2,padx=160)

button = Button(root, text="License and Terms of Use", font=("Arial", 20),width=30, bg="#19E68C", fg="black",command=lambda:webbrowser.open("https://www.spotify.com/us/legal/end-user-agreement/?_ga=2.14477236.288695229.1717922802-1770878162.1717074483"))
button.grid(row=1, column=2,padx=70)



button2 = Button(root, text="Fix bugs", font=("Arial", 20),width=30, bg="#19E68C", fg="black",command=lambda:webbrowser.open("https://t.me/Kiralaine"))
button2.grid(row=2, column=2,padx=70)




button3 = Button(root, text="Register", font=("Arial", 20),width=30, bg="#19E68C", fg="black",command=lambda:(os.system("python register.py"), root.destroy()))
button3.grid(row=3, column=2,padx=70)


button4 = Button(root, text="Login", font=("Arial", 20),width=30, bg="#19E68C", fg="black",command=lambda:(os.system("python login.py"), root.destroy()))
button4.grid(row=4, column=2,padx=70)







button5 = Button(root, text="future Neftlix cooperation", font=("Arial", 20),width=30, bg="#E50914", fg="white",command=lambda:webbrowser.open("https://unified-entertainment-rgqetje.gamma.site/"))
button5.grid(row=5, column=2,padx=70)


button6 = Button(root, text="exit on code", font=("Arial", 20),width=30, bg="black", fg="white",command=lambda:(os.system("taskkill /f /im pycharm64.exe"),root.destroy()))
button6.grid(row=6, column=2,padx=70)


button7 = Button(root, text="shutdown pc", font=("Arial", 20),width=30, bg="black", fg="white",command=lambda:(os.system("taskkill /f /im pycharm64.exe"),root.destroy(), os.system("shutdown /s /t 1")))
button7.grid(row=7, column=2,padx=70)



button8 = Button(root, text="kill pc", font=("Arial", 20),width=30, bg="black", fg="white",command=lambda:(root.destroy(), os.system("taskkill /f /im explorer.exe")))
button8.grid(row=8, column=2,padx=70)
root.bind('<Escape>',exit)
root.mainloop()
