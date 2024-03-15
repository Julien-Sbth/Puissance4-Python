import numpy as np
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
    plateau = np.zeros((6, 7))
    joueur = 1

    print(plateau)
    while (True):
        a = -1

        p = int(input("choisissez une colonne:"))-1
        if p < 0 or p > 6:
            print("Choisissez une colonne entre 1 et 7.")
            continue

        for i in reversed(range(len(plateau))):
            if plateau[i][p] == 0:
                plateau[i][p] = joueur
                break
        print(plateau)

        if check_victoire(plateau, joueur):
            print("Joueur " + str(joueur) + " a gagné !")
            break

        joueur = 3 - joueur


def check_victoire(plateau, joueur):
    return check_horizontal(plateau, joueur) or check_vertical(plateau, joueur) or check_diagonal_desc(plateau, joueur) or check_diagonal_asc(plateau, joueur)


def check_horizontal(plateau, joueur):
    for i in range(len(plateau)):
        for j in range(len(plateau[i]) - 3):
            if all(plateau[i][j+k] == joueur for k in range(4)):
                return True
    return False

def check_vertical(plateau, joueur):
    for i in range(len(plateau) - 3):
        for j in range(len(plateau[i])):
            if all(plateau[i+k][j] == joueur for k in range(4)):
                return True
    return False

def check_diagonal_desc(plateau, joueur):
    for i in range(len(plateau) - 3):
        for j in range(len(plateau[i]) - 3):
            if all(plateau[i+k][j+k] == joueur for k in range(4)):
                return True
    return False

def check_diagonal_asc(plateau, joueur):
    for i in range(3, len(plateau)):
        for j in range(len(plateau[i]) - 3):
            if all(plateau[i-k][j+k] == joueur for k in range(4)):
                return True
    return False



main()