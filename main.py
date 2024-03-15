import numpy as np
from Jeu import Puissance4
import tkinter as tk

fen = tk.Tk()
cnv = tk.Canvas(fen, width=700, height=600, bg="white")
cnv.grid()
for i in range(7):
    cnv.create_line(100*i, 0, 100*i, 600, fill="black")
for i in range(6):
    cnv.create_line(0, 100*i, 700, 100*i, fill="black")

fen.mainloop()

def main():
    jeu = Puissance4()
    print(jeu.plateau)
    while True:
        colonne = int(input("Choisissez une colonne:")) - 1
        jeu.jouer(colonne)
        if jeu.check_victoire():
            break

if __name__ == "__main__":
    main()