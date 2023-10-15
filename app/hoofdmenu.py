import tkinter as tk
from tkinter import Label, Button
from karakter.karakter_menu import maak_karakter_menu_scherm_aan
from PIL import ImageTk, Image

def ga_naar_admin_scherm(venster):
    from admin.admin_button import maak_admin_scherm
    maak_admin_scherm(venster)
def ga_naar_avontuurmenu(venster):
    from avonturen.toon_avonturen_menu import toon_avonturen_menu
    toon_avonturen_menu(venster)


def ga_naar_karakter_menu_scherm(venster):
    maak_karakter_menu_scherm_aan(venster)


def maak_hoofdmenu_scherm_aan(venster):
    for widget in venster.winfo_children():
        widget.destroy()

    hoofdmenu_titel = Label(venster, text="Welkom, avonturier!", font=("Helvetica", 36))

    karakter_button = Button(text="Karakter Menu",width=40, height=2, command=lambda : ga_naar_karakter_menu_scherm(venster))
    avontuur_kiezen = Button(text="Avontuur Kiezen", width=40, height=2,command=lambda : ga_naar_avontuurmenu(venster))
    admin_button = Button(text="Admin login", width= 40, height=2,command=lambda : ga_naar_admin_scherm(venster))


    # original background settings
    original_image = Image.open("../images/rivendell.png")
    resized_image = original_image.resize((1200, 700), Image.LANCZOS)
    voorbeeld_image = ImageTk.PhotoImage(resized_image)

    label_image = Label(venster, image=voorbeeld_image)
    label_image.image = voorbeeld_image
    label_image.tkraise()


    hoofdmenu_titel.pack()
    label_image.pack()
    karakter_button.pack()
    avontuur_kiezen.pack()
    admin_button.pack()

# venster = tk.Tk()
# venster.attributes("-fullscreen", True)  # Make the window fullscreen
#
# maak_hoofdmenu_scherm_aan(venster)
#
# venster.mainloop()