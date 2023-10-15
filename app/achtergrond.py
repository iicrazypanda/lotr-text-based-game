import os
from tkinter import Canvas
from PIL import ImageTk, Image


def maak_achtergrond(venster, image):
    cwd = os.getcwd()

    # Make background image
    background_image_path = cwd + image
    original_image = Image.open(background_image_path)
    resized_image = original_image.resize((venster.winfo_screenwidth(), venster.winfo_screenheight()), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(resized_image)

    canvas = Canvas(venster, width=venster.winfo_screenwidth(), height=venster.winfo_screenheight())

    canvas.create_image(0, 0, image=background_image, anchor="nw")
    canvas.image = background_image

    canvas.pack(fill="both", expand=True)

    return canvas
