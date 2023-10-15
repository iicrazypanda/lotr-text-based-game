import os
from tkinter import Frame, Label
from PIL import ImageTk, Image
from app.hoofdmenu import maak_hoofdmenu_scherm_aan
from muziek import achtergrond_muziek


def ga_naar_hoofdmenu_scherm(venster):
    achtergrond_muziek.speel_achtergrond_muziek()
    maak_hoofdmenu_scherm_aan(venster)


def maak_splash_scherm_aan(venster):
    cwd = os.getcwd()
    for widget in venster.winfo_children():
        widget.destroy()

    frame = Frame(venster, height=venster.winfo_screenheight(), width=venster.winfo_screenwidth())

    splash_scherm_titel = Label(venster, text="Splash menu", font=("Helvetica", 36))
    splash_scherm_titel.tkraise()
    splash_scherm_titel.grid(row=0, column=0)

    image_path = cwd + "/images/schippi.png"
    original_image = Image.open(image_path)
    resized_image = original_image.resize((400, 400), Image.LANCZOS)
    voorbeeld_image = ImageTk.PhotoImage(resized_image)

    label_image = Label(venster, image=voorbeeld_image)
    label_image.image = voorbeeld_image
    label_image.tkraise()
    label_image.grid(row=0, column=0)

    frame.grid(row=0, column=0)

    venster.after(3000, lambda: ga_naar_hoofdmenu_scherm(venster))
