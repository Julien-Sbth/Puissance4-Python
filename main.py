import csv
import random as rand

import numpy as np
import keyboard

from IA import IA
from Jeu import Puissance4
from Interface import Interface


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
