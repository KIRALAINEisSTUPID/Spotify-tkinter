import webbrowser

from tkinter import (Tk, Frame, LabelFrame, Label, Entry, Spinbox, Button, messagebox,StringVar,
                     DISABLED, Menu, Menubutton)
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os
import subprocess
root= Tk()
root.attributes('-fullscreen', False)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
center_x = int(width / 2 - 580 / 2)
center_y = int(height / 2 - 500 / 2)
root.geometry(f"580x500+{center_x}+{center_y}")
root.configure(bg="#121212")
logo = ImageTk.PhotoImage(Image.open("pictures/icon.png"))
root.iconphoto(False, logo)
root.title("♬Spotify-SONGS ♪ LIST♩")
def exit(event=None):
    root.destroy()
    os.system("python Nazorat.py")



root.bind('<Escape>',exit)



import os
def finder(path):
    direct=os.getcwd()
    k =os.path.join(direct, path)
    return k




megalovania = Button(root,text="Megalovania",bg="#121212",width=29,fg="white",font=("Impact", 30),command=lambda:(os.system(finder("songs")+"\Megalovania.mp3")))
megalovania.grid()

shino = Button(root,text="Shinogowa E-wa",bg="#121212",width=29,fg="white",font=("Impact", 30),command=lambda:(os.system(finder("songs")+ "\shino.mp3")))
shino.grid()

depressed= Button(root,text="Cute Depressed",bg="#121212",width=29,fg="white",font=("Impact", 30),command=lambda:(os.system(finder("songs")+ "\cute.m4a")))
depressed.grid()


psycho= Button(root,text="Psycho dreams",bg="#121212",width=29,fg="white",font=("Impact", 30),command=lambda:(os.system(finder("songs")+ "\psycho.mp3")))
psycho.grid()


WTF= Button(root,text="WTF 2",bg="#121212",width=29,fg="white",font=("Impact", 30),command=lambda:(os.system(finder("songs")+ "\wtf.mp3")))
WTF.grid()

spit= Button(root,text="Spit in my face",bg="#121212",width=29,fg="white",font=("Impact", 30),command=lambda:(os.system(finder("songs")+ "\spit.m4a")))
spit.grid()











root.mainloop()




