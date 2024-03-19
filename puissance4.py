import numpy as np

class Puissance4:
    def __init__(self):
        self.plateau = np.zeros((6, 7))
        self.joueur = 1

    def jouer_coup(self, colonne):
        for i in reversed(range(len(self.plateau))):
            if self.plateau[i][colonne] == 0:
                self.plateau[i][colonne] = self.joueur
                return i
        return -1

    def verifier_victoire(self):
        return (self.verifier_horizontal() or
                self.verifier_vertical() or
                self.verifier_diagonale_desc() or
                self.verifier_diagonale_asc())

    def verifier_horizontal(self):
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i]) - 3):
                if all(self.plateau[i][j + k] == self.joueur for k in range(4)):
                    return True
        return False

    def verifier_vertical(self):
        for i in range(len(self.plateau) - 3):
            for j in range(len(self.plateau[i])):
                if all(self.plateau[i + k][j] == self.joueur for k in range(4)):
                    return True
        return False

    def verifier_diagonale_desc(self):
        for i in range(len(self.plateau) - 3):
            for j in range(len(self.plateau[i]) - 3):
                if all(self.plateau[i + k][j + k] == self.joueur for k in range(4)):
                    return True
        return False

    def verifier_diagonale_asc(self):
        for i in range(3, len(self.plateau)):
            for j in range(len(self.plateau[i]) - 3):
                if all(self.plateau[i - k][j + k] == self.joueur for k in range(4)):
                    return True
        return False
