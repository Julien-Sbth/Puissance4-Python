import pandas as pd
import numpy as np


class IA:
    def __init__(self):
        self.data = pd.DataFrame(columns=['board', 'action', 'result', 'victoires'])
        self.victoires = 0

    def choisir_coup(self, plateau):
        colonnes_disponibles = [col for col in range(len(plateau[0])) if plateau[0][col] == 0]
        return np.random.choice(colonnes_disponibles)

    def enregistrer_resultat(self, plateau):
        flatten_board = [item for sublist in plateau for item in sublist]
        new_data = pd.DataFrame({'board': [flatten_board], 'action': [self.choisir_coup(plateau)]})
        self.data = pd.concat([self.data, new_data], ignore_index=True)

    def charger_donnees(self, file_path='data.xlsx'):
        try:
            self.data = pd.read_excel(file_path, engine='openpyxl')
        except FileNotFoundError:
            print("Le fichier Excel n'existe pas encore.")

    def incrementer_victoires(self):
        self.victoires += 1
        self.data.at[len(self.data) - 1, 'victoires'] = self.victoires

    def sauvegarder_donnees(self, file_path='data.xlsx'):
        self.data.to_excel(file_path, index=False)
