import os
from tkinter import messagebox
from karakter_creatie import compleet_gekozen_karakter_opslaan
karakter_lijst = []

def karakter_opslaan(karakter):
    cwd = os.getcwd()
    path = cwd + "/karakter/opgeslagen_karakters.txt"
    with open(path, "a") as bestand:
        bestand.write(karakter + "\n")
        messagebox.showinfo(f"Het karakter '{karakter}' is opgeslagen.")



