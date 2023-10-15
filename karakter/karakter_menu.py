from tkinter import Label, Button, Frame
from PIL import ImageTk, Image
from karakter.karakter_creatie import maak_karakter_creatie_scherm_aan
from karakter.karakter_selectie import maak_karakter_selectie_scherm_aan


def ga_naar_karakter_selectie_scherm(venster):
    maak_karakter_selectie_scherm_aan(venster)


def ga_naar_hoofdmenu(venster):
    from app.hoofdmenu import maak_hoofdmenu_scherm_aan
    maak_hoofdmenu_scherm_aan(venster)


def ga_naar_karakter_creatie_scherm(venster):
    maak_karakter_creatie_scherm_aan(venster)


def maak_karakter_menu_scherm_aan(venster):
    for widget in venster.winfo_children():
        widget.destroy()

    # Boven frame
    boven_frame = Frame(venster)
    terug_button = Button(boven_frame, text="Terug naar hoofdmenu", command=lambda: ga_naar_hoofdmenu(venster),
                          width=20,
                          height=2)
    terug_button.pack()
    boven_frame.pack(side="top", anchor="nw")

    # Content frame
    content_frame = Frame(venster)
    karakter_menu_titel = Label(content_frame, text="Karakter Menu", font=("Helvetica", 36))
    karakter_menu_titel.pack(padx=20, pady=20)

    karakter_selectie_button = Button(content_frame, text="Karakter Selectie", width=20,
                                      height=2, command=lambda: ga_naar_karakter_selectie_scherm(venster))
    karakter_selectie_button.pack(expand=True, side="left", padx=20, pady=20)

    karakter_creatie_button = Button(content_frame, text="Karakter Creëren", width=20,
                                     height=2, command=lambda: ga_naar_karakter_creatie_scherm(venster))
    karakter_creatie_button.pack(expand=True, side="right", padx=20, pady=20)
    content_frame.pack(expand=True)

    onder_frame = Frame(venster)
    onder_frame.pack(side="bottom")

    # karakter_menu_titel = Label(venster, text="Karakter Menu", font=("Helvetica", 36))
    # karakter_menu_titel.pack()
    #
    # karakter_selectie_button = Button(text="Karakter Selectie", width=20,
    #                                   height=2, command=lambda: ga_naar_karakter_selectie_scherm(venster))
    # karakter_selectie_button.pack(expand=True, side="left")
    #
    # karakter_creatie_button = Button(text="Karakter Creëren", width=20,
    #                                  height=2, command=lambda: ga_naar_karakter_creatie_scherm(venster))
    # karakter_creatie_button.pack(expand=True, side="right")

    # terug_button = Button(venster, text="Terug naar hoofdmenu", command=lambda: ga_naar_hoofdmenu(venster),
    #                       width=20,
    #                       height=2)
    # terug_button.pack()

