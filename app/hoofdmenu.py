import os
from tkinter import Label, Frame, Button, Canvas

from app.achtergrond import maak_achtergrond
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

    canvas = maak_achtergrond(venster, "/images/real_rivendell.jpg")

    content_frame = Frame(canvas, bg="#444444")

    hoofdmenu_titel = Label(content_frame, text="Welkom, Avonturier!", font=("Helvetica", 36), bg="#444444", fg="white")
    hoofdmenu_titel.pack(pady=20, padx=20)

    karakter_button = Button(content_frame, text="Karakter Menu", width=40, height=2, bg="#333333", fg="white", command=lambda: ga_naar_karakter_menu_scherm(canvas))
    karakter_button.pack(pady=20, padx=20)

    avontuur_kiezen = Button(content_frame, text="Avontuur Kiezen", width=40, height=2, bg="#333333", fg="white", command=lambda: ga_naar_avontuurmenu(canvas))
    avontuur_kiezen.pack(pady=20, padx=20)

    admin_button = Button(content_frame, text="Admin login", width=40, height=2, bg="#333333", fg="white", command=lambda: ga_naar_admin_scherm(canvas))
    admin_button.pack(pady=20, padx=20)

    content_frame.pack(expand=True, anchor="center")
