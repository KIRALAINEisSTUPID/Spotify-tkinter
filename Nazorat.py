import webbrowser
from tkinter import (Tk, Frame, LabelFrame, Label, Entry, Spinbox, Button, messagebox,StringVar,
                     DISABLED, Menu, Menubutton)
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os


def exit(event=None):
    root.destroy()


def resize(event=None):
    root.attributes('-fullscreen', False)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    center_x = int(width / 2 - 580 / 2)
    center_y = int(height / 2 - 500 / 2)
    root.geometry(f"580x500+{center_x}+{center_y}")











def finder(path):
    direct=os.getcwd()
    k =os.path.join(direct, path)
    return k







root = Tk()
root.title("♬Spotify-SONGS ♪ SEARCH♩")
root.attributes('-fullscreen', True)

root.configure(bg="#121212")
root.bind('<Escape>',resize)
root.bind('<F11>',exit)
logo = ImageTk.PhotoImage(Image.open("pictures/icon.png"))
root.iconphoto(False, logo)




def search():
    webbrowser.open(f"https://open.spotify.com/search/{entry.get()}")




entr = StringVar(root)

entry = Entry(root,textvariable=entr, bg="white", fg="black", justify="center", font=("Arial", 20),background="#121212",foreground="white")
entry.grid(row=0, column=3, columnspan=2,ipadx=200, padx=400,ipady=5)
entr.set("Search songs")

searchphoto= Image.open("pictures/search.png")
searchphoto = searchphoto.resize((45,45))
searchphoto= ImageTk.PhotoImage(searchphoto)
search = Button(root,image=searchphoto,bg="#121212",fg="green",command=search)
search.grid(row=0,column=4)




premiumphoto = Image.open("pictures/premium.png")
premiumphoto = premiumphoto.resize((45,45))
premiumphoto= ImageTk.PhotoImage(premiumphoto)
premium = Button(root,image=premiumphoto,bg="#1ED760",fg="green",command=lambda:(messagebox.showinfo(title="Premium",message="Add card to remove ads" ), webbrowser.open("https://www.spotify.com/uz/premium/")))
premium.place(x=1140)



homephoto= Image.open("pictures/home.png")
homephoto = homephoto.resize((45,45))
homephoto= ImageTk.PhotoImage(homephoto)
home = Menubutton(root,image=homephoto,bg="#121212",fg="green",bd=0)
home.place(x=349)
buttonlist = Menu(home, tearoff=0,bg="#00D25C",fg="#121212")
home.configure(menu=buttonlist)
buttonlist.add_command(label="List",command=lambda:(root.destroy(),os.system("python list.py")))
buttonlist.add_command(label="Rock",command=lambda:(webbrowser.open("https://open.spotify.com/genre/0JQ5DAqbMKFDXXwE9BDJAr")))
buttonlist.add_command(label="POP",command=lambda:(webbrowser.open("https://open.spotify.com/genre/0JQ5DAqbMKFEC4WFtoNRpw")))
buttonlist.add_command(label="Classic",command=lambda:(webbrowser.open("https://open.spotify.com/genre/0JQ5DAqbMKFPrEiAOxgac3")))
buttonlist.add_command(label="Help",command=lambda:(root.destroy(),os.system("python help.py")))
# buttonlist.add_command(label="Close", command=)








frame = Frame(root)
label_frame = LabelFrame(frame, bg="#121212")

frame.place(x=0, y=102)
label_frame.grid(row=0, column=0)


megalovania = Image.open("pictures/megalovania.png")
megalovania = megalovania.resize((225,225))
megalovania = ImageTk.PhotoImage(megalovania)
megalovaniaButton = Button(label_frame,image=megalovania,bg="#314486",command=lambda:(os.system(finder("songs")+"\Megalovania.mp3")))
megalovaniaButton.grid(row=0, column=0)
megalovania_label = Label(label_frame, text="Megalovania", bg="#121212", fg="white", font=("Sans", 15))
megalovania_label.grid(row=1, column=0)


bastards = Image.open("pictures/LOVELYBastards.jpg.")
bastards = bastards.resize((225,225))
bastards= ImageTk.PhotoImage(bastards)
bastardsbutton = Button(label_frame,image=bastards,bg="#314486",command=lambda:(os.system(finder("songs")+"\lovelybastards.mp3")))
bastardsbutton.grid(row=0, column=1)
bastards_label = Label(label_frame, text="Lovely bastards \n"
                                         "X \n"
                                         "Meet the frownies", bg="#121212", fg="white", font=("Sans", 15))
bastards_label.grid(row=1, column=1)







cute = Image.open("pictures/cute.jpg")
cute = cute.resize((225,225))
cute= ImageTk.PhotoImage(cute)
cutebutton = Button(label_frame,image=cute,bg="#314486",command=lambda:(os.system(finder("songs")+"\cute.m4a")))
cutebutton.grid(row=0, column=2)
cute_label = Label(label_frame, text="Cute Depressed", bg="#121212", fg="white", font=("Sans", 15))
cute_label.grid(row=1, column=2)

pscho = Image.open("pictures/psycho.jpg")
pscho = pscho.resize((225,225))
pscho= ImageTk.PhotoImage(pscho)
pschobutton = Button(label_frame,image=pscho,bg="#314486",command=lambda:(os.system(finder("songs")+"\psycho.m4a")))
pschobutton.grid(row=0, column=3)
psycho_label = Label(label_frame, text="Psycho dreams", bg="#121212", fg="white", font=("Sans", 15))
psycho_label.grid(row=1, column=3)

mentalite = Image.open("pictures/mentalite.jpg")
mentalite = mentalite.resize((250,225))
mentalite= ImageTk.PhotoImage(mentalite)
mentalitebutton = Button(label_frame,image=mentalite,bg="#314486",command=lambda:(os.system(finder("songs")+"\mentalite.mp3")))
mentalitebutton.grid(row=2, column=0)
mentalite_label = Label(label_frame, text="Mentalite", bg="#121212", fg="white", font=("Sans", 15))
mentalite_label.grid(row=3, column=0)







black = Image.open("pictures/black.jpg")
black = black.resize((250,225))
black= ImageTk.PhotoImage(black)
blackbutton = Button(label_frame,image=black,bg="#314486",command=lambda:(os.system(finder("songs")+"\Loser.mp3")))
blackbutton.grid(row=2, column=1)
black_label = Label(label_frame, text="Чёрный диплом!", bg="#121212", fg="white", font=("Sans", 15))
black_label.grid(row=3, column=1)



nejnovye = Image.open("pictures/nejno.jpg")
nejnovye = nejnovye.resize((250,225))
nejnovye= ImageTk.PhotoImage(nejnovye)
nejnovyebutton = Button(label_frame,image=nejnovye,bg="#314486",command=lambda:(os.system(finder("songs")+"\Нежно.mp3")))
nejnovyebutton.grid(row=2, column=2)
nejnovye_label = Label(label_frame, text="Паша Изотов – Нежно", bg="#121212", fg="white", font=("Sans", 15))
nejnovye_label.grid(row=3, column=2)


michael = Image.open("pictures/muzan (1).jpg")
michael = michael.resize((208,225))
michael= ImageTk.PhotoImage(michael)
michaelbutton = Button(label_frame,image=michael,bg="#314486",command=lambda:(os.system(finder("songs")+"\sss.mp3")))
michaelbutton.grid(row=2, column=3)
michael_label = Label(label_frame, text="Smooth criminal", bg="#121212", fg="white", font=("Sans", 15))
michael_label.grid(row=3, column=3)


frame2 = Frame(root)
frame2.place(x=1000, y=102)
label_frame2 = LabelFrame(frame2, bg="#121212")
label_frame2.grid(row=0, column=0)





photo = Image.open("pictures/rek1.jpg")
photo2 = Image.open("pictures/rek2.jpg")
photo3 = Image.open("pictures/rek3.jpg")
photo4 = Image.open("pictures/rek4.jpg")

photos = [photo, photo2, photo3, photo4]
photos_list = []
for p in photos:
    size = p.resize((500,500))
    photo = ImageTk.PhotoImage(size)
    photos_list.append(photo)

current_photo_index = 0
photo_label = Label(label_frame2, image=photos_list[current_photo_index],bg="#121212")
photo_label.grid()


def change_photo(photo):
    global current_photo_index
    new_index = current_photo_index + photo
    if 0 <= new_index < len(photos_list):
        current_photo_index = new_index
        photo_label.config(image=photos_list[current_photo_index])

    if current_photo_index > 0:
        back_button['state'] = "normal"
    else:
        back_button['state'] = "disabled"

    if current_photo_index < len(photos_list) - 1:
        next_button['state'] = "normal"
    else:
        next_button['state'] = "disabled"


def back_photo():
    change_photo(-1)


def next_photo():
    change_photo(1)

up = Image.open("pictures/UP.png")
up = up.resize((50, 50))
up = ImageTk.PhotoImage(up)


down = Image.open("pictures/down2.png")
down = down.resize((50, 50))
down = ImageTk.PhotoImage(down)
back_button = Button(label_frame2, image=up,bg="#121212",
                     font=("Impact", 15),
                     command=back_photo)

next_button = Button(label_frame2, image=down,bg="#121212",
                     font=("Impact", 15),
                     command=next_photo)
back_button.grid(row=1)

next_button.grid(row=2)


spotify_premium_photo = Image.open("pictures/premium_spotify.png")
spotify_premium_photo = spotify_premium_photo.resize((900, 200))
spotify_premium_photo = ImageTk.PhotoImage(spotify_premium_photo)
spotify_premium = Label(root,image=spotify_premium_photo,bg="#121212")
spotify_premium.place(x=50,y=670)
root.mainloop()