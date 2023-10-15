import os
from tkinter import Tk
from app.splash_scherm import maak_splash_scherm_aan


def main():
    cwd = os.getcwd()
    print(cwd)
    os.chdir("../")

    # Maak root aan
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.title("Lord of the Rings Game")
    root.geometry("%dx%d" % (width, height))
    root.resizable(False, False)

    # Adding transparent background property
    root.wm_attributes('-transparentcolor', '#ab23ff')

    # Begin met splash scherm
    maak_splash_scherm_aan(root)

    root.mainloop()


if __name__ == '__main__':
    main()


