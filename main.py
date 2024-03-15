import csv
import random as rand

import numpy as np
import keyboard

from IA import IA
from Jeu import Puissance4


def main():
    while True:  # Boucle infinie
        jeu = Puissance4()
        ia1 = IA()  # Première instance de l'IA
        ia2 = IA()  # Première instance de l'IA
        ia1.charger_donnees()  # Charger les données pour la première IA
        ia2.charger_donnees()
        print(jeu.plateau)
        while True:
            coup_ia1 = ia1.choisir_coup(jeu.plateau)
            if coup_ia1 is not None:  # Vérifier si un coup est disponible
                jeu.jouer(coup_ia1)
                ia1.coups_joues.append(coup_ia1)  # Ajouter le coup joué par l'IA 2 à ses coups joués
                if jeu.check_victoire():
                    ia1.enregistrer_resultat(ia1.coups_joues)  # Enregistrer les coups joués par l'IA 2
                    break
            else:
                print("Aucun coup disponible pour l'IA 2.")
                break

            coup_ia2 = ia2.choisir_coup(jeu.plateau)
            if coup_ia2 is not None:  # Vérifier si un coup est disponible
                jeu.jouer(coup_ia2)
                ia2.coups_joues.append(coup_ia2)  # Ajouter le coup joué par l'IA 2 à ses coups joués
                if jeu.check_victoire():
                    ia2.enregistrer_resultat(ia2.coups_joues)  # Enregistrer les coups joués par l'IA 2
                    break
            else:
                print("Aucun coup disponible pour l'IA 2.")
                break

        print("Appuyez sur 'q' pour quitter ou appuyez sur une autre touche pour continuer...")
        if keyboard.is_pressed('q'):
            break


if __name__ == "__main__":
    main()
