import csv
import random as rand
import numpy as np


class IA:
    def __init__(self, exploration_rate=0.2, learning_rate=0.1):
        self.coups_joues = []
        self.joueur = 1
        self.nb_colonnes = 7
        self.strategies = np.zeros(self.nb_colonnes)
        self.exploration_rate = exploration_rate
        self.learning_rate = learning_rate

    def charger_donnees(self):
        with open('resultats.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                for i, resultat in enumerate(row[:self.nb_colonnes]):
                    if resultat:
                        self.strategies[i] += int(resultat)

    def enregistrer_resultat(self, resultats):
        resultats_str = ','.join(map(str, resultats))
        with open('resultats.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(resultats_str.split(','))

    def choisir_coup(self, plateau):
        if rand.random() < self.exploration_rate:
            coups_valides = [colonne for colonne in range(self.nb_colonnes) if plateau[0][colonne] == 0]
            if coups_valides:
                coup_choisi = rand.choice(coups_valides)
                self.coups_joues.append(coup_choisi)
                return coup_choisi
            else:
                return None
        else:
            coups_valides = [colonne for colonne in range(self.nb_colonnes) if plateau[0][colonne] == 0]
            if coups_valides:
                scores_coups = [self.strategies[colonne] for colonne in coups_valides]
                meilleur_coup = coups_valides[np.argmax(scores_coups)]
                self.coups_joues.append(meilleur_coup)
                return meilleur_coup
            else:
                return None

    def mettre_a_jour_strategies(self, coup_gagnant):
        if coup_gagnant is not None:
            self.strategies[coup_gagnant] += self.learning_rate
