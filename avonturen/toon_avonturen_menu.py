import os
from tkinter import Button, Label, Frame, Canvas
from PIL import Image, ImageTk

from app.achtergrond import maak_achtergrond
from app.splash_scherm import ga_naar_hoofdmenu_scherm
from avonturen.avontuur_spelen import maak_avontuur_scherm_aan

def ga_naar_avontuur(venster, avontuur):
    maak_avontuur_scherm_aan(venster, str(avontuur))
def ga_naar_avontuur_1(venster):
    maak_avontuur_scherm_aan(venster, "1")


def ga_naar_avontuur_2(venster):
    maak_avontuur_scherm_aan(venster, "2")


def ga_naar_avontuur_3(venster):
    maak_avontuur_scherm_aan(venster, "3")


def toon_avonturen_menu(venster):
    cwd = os.getcwd()
    for widget in venster.winfo_children():
        widget.destroy()

    canvas = maak_achtergrond(venster, "/images/real_rivendell.jpg")

    avontuur_image_path = cwd + "/images/Crown_pic_two-2939004554.png"
    original_image = Image.open(avontuur_image_path)
    resized_image = original_image.resize((100, 100), Image.LANCZOS)
    avontuur_image = ImageTk.PhotoImage(resized_image)

    # Boven frame
    boven_frame = Frame(canvas)
    button_terug_naar_hoofd_menu = Button(boven_frame, text="Terug naar hoofdmenu", width=30, height=2,
                                          command=lambda: ga_naar_hoofdmenu_scherm(venster))
    button_terug_naar_hoofd_menu.pack(side="left")
    boven_frame.pack(side="top", anchor="nw")

    # Content frame
    content_frame = Frame(canvas)
    titel_frame = Frame(content_frame)

    titel_label = Label(titel_frame, text="Kies een avontuur", font=("Helvetica", 36))
    titel_label.pack()

    titel_frame.pack(fill="both", expand=True)

    avonturen_lijst = ["Reis In De Gouw", "Zoektocht zwaard Elendil", "Queeste Erebor"]
    frame_avonturen = Frame(content_frame)
    for teller in range(len(avonturen_lijst)):
        frame_avontuur = Frame(frame_avonturen)

        avontuur_label = Label(frame_avontuur, image=avontuur_image)
        avontuur_label.image = avontuur_image
        avontuur_label.pack()

        button_avontuur = Button(frame_avontuur, text=avonturen_lijst[teller],
                                 command=lambda teller=teller: ga_naar_avontuur(venster, teller + 1))
        button_avontuur.pack()

        frame_avontuur.grid(row=2, column=teller, padx=100, pady=100)

    frame_avonturen.pack(fill="both", expand=True)
    content_frame.pack(expand=True)

    # Onder frame
    onder_frame = Frame(canvas)
    onder_frame.pack()

    # Linker frame
    # linker_frame = Frame(canvas, borderwidth=10, relief="solid")
    # frame_terug_naar_hoofdmenu = Frame(linker_frame)

    # button_terug_naar_hoofd_menu = Button(linker_frame, text="Terug naar hoofdmenu", width=30, height=2,
    #                                       command=lambda: ga_naar_hoofdmenu_scherm(venster))
    # button_terug_naar_hoofd_menu.pack(side="left", anchor="nw")

    # frame_terug_naar_hoofdmenu.pack()
    # linker_frame.pack(side="left", expand=True)

    # Midden frame
    midden_frame = Frame(canvas, borderwidth=10, relief="solid")
    # titel_frame = Frame(midden_frame)
    #
    # titel_label = Label(titel_frame, text="Kies een avontuur", font=("Helvetica", 36))
    # titel_label.pack()
    #
    # titel_frame.pack(fill="both", expand=True)
    #
    # avonturen_lijst = ["Reis In De Gouw", "Zoektocht zwaard Elendil", "Queeste Erebor"]
    # frame_avonturen = Frame(midden_frame)
    # for teller in range(len(avonturen_lijst)):
    #     frame_avontuur = Frame(frame_avonturen)
    #
    #     avontuur_label = Label(frame_avontuur, image=avontuur_image)
    #     avontuur_label.image = avontuur_image
    #     avontuur_label.pack()
    #
    #     button_avontuur = Button(frame_avontuur, text=avonturen_lijst[teller],
    #                              command=lambda teller=teller: ga_naar_avontuur(venster, teller + 1))
    #     button_avontuur.pack()
    #
    #     frame_avontuur.grid(row=2, column=teller, padx=100, pady=100)
    #
    # frame_avonturen.pack(fill="both", expand=True)
    midden_frame.pack(expand=True, side="left")

    # Rechter frame
    rechter_frame = Frame(canvas)

    rechter_frame.pack(side="right", expand=True)

    # titel_frame = Frame(canvas)
    #
    # titel_label = Label(titel_frame, text="Kies een avontuur", font=("Helvetica", 36))
    # titel_label.grid(row=0, column=1, padx=360, pady=30)
    #
    # titel_frame.grid(row=0, column=1, pady=50)
    #
    # avonturen_lijst = ["Reis In De Gouw", "Zoektocht zwaard Elendil", "Queeste Erebor"]
    # frame_avonturen = Frame(canvas)
    # for teller in range(len(avonturen_lijst)):
    #
    #     frame_avontuur = Frame(frame_avonturen)
    #
    #     avontuur_label = Label(frame_avontuur, image=avontuur_image)
    #     avontuur_label.image = avontuur_image
    #     avontuur_label.pack()
    #
    #     button_avontuur = Button(frame_avontuur, text=avonturen_lijst[teller], command=lambda: ga_naar_avontuur(venster, teller + 1))
    #     button_avontuur.pack()
    #
    #     frame_avontuur.grid(row=2, column=teller, padx=100, pady=100)
    # frame_avonturen.pack()
    # frame_avontuur_1 = Frame(canvas)
    #
    # avontuur_1_label = Label(frame_avontuur_1, image=avontuur_image)
    # avontuur_1_label.image = avontuur_image
    # avontuur_1_label.pack()
    #
    # button_avontuur_1 = Button(frame_avontuur_1, text="Reis In De Gouw", command=lambda: ga_naar_avontuur_1(venster))
    # button_avontuur_1.pack()
    #
    # frame_avontuur_1.grid(row=2, column=0, padx=100, pady=100)

    # frame_avontuur_2 = Frame(canvas)
    #
    # avontuur_2_label = Label(frame_avontuur_2, image=avontuur_image)
    # avontuur_2_label.image = avontuur_image
    # avontuur_2_label.pack()
    #
    # button_avontuur_2 = Button(frame_avontuur_2, text="Zoektocht zwaard Elendil", command=lambda: ga_naar_avontuur_2(venster))
    # button_avontuur_2.pack()
    #
    # frame_avontuur_2.grid(row=2, column=1, padx=100)
    #
    # frame_avontuur_3 = Frame(canvas)
    #
    # avontuur_3_label = Label(frame_avontuur_3, image=avontuur_image)
    # avontuur_3_label.image = avontuur_image
    # avontuur_3_label.pack()
    #
    # button_avontuur_3 = Button(frame_avontuur_3, text="Queeste Erebor", command=lambda: ga_naar_avontuur_3(venster))
    # button_avontuur_3.pack()
    #
    # frame_avontuur_3.grid(row=2, column=2, padx=100)

    # frame_terug_naar_hoofdmenu = Frame(canvas)
    #
    # button_terug_naar_hoofd_menu = Button(frame_terug_naar_hoofdmenu, text="Terug naar hoofdmenu", width=30, height=2, command=lambda: ga_naar_hoofdmenu_scherm(venster))
    # button_terug_naar_hoofd_menu.pack(pady=450)
    #
    # frame_terug_naar_hoofdmenu.pack()

