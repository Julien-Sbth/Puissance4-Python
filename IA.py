import csv
import random as rand

import numpy as np


class IA:
    def __init__(self, exploration_rate=0.2):
        self.coups_joues = []
        self.joueur = 1
        self.nb_colonnes = 7
        self.strategies = np.zeros(self.nb_colonnes)
        self.exploration_rate = exploration_rate

    def charger_donnees(self):
        with open('resultats.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                for i, resultat in enumerate(row[:self.nb_colonnes]):
                    if resultat:
                        self.strategies[i] += int(resultat)

    def enregistrer_resultat(self, resultats):
        # Concaténer les résultats en une seule chaîne de caractères
        resultats_str = ','.join(map(str, resultats))
        with open('resultats.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(resultats_str.split(','))  # Écrire chaque élément comme une colonne distincte

    def choisir_coup(self, plateau):
        if rand.random() < self.exploration_rate:
            coups_valides = [colonne for colonne in range(7) if plateau[0][colonne] == 0]
            if coups_valides:
                return rand.choice(coups_valides)
            else:
                return None
        else:
            coups_valides = [colonne for colonne in range(7) if plateau[0][colonne] == 0]
            if coups_valides:
                scores_coups = [self.strategies[colonne] for colonne in coups_valides]
                meilleur_coup = coups_valides[np.argmax(scores_coups)]
                return meilleur_coup
            else:
                return None
