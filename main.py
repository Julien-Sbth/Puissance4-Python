import tkinter as tk
from Jeu import Puissance4
from IA import IA


class InterfaceGraphique:
    def __init__(self):
        self.fen = tk.Tk()
        self.cnv = tk.Canvas(self.fen, width=700, height=600, bg="white")
        self.cnv.grid()
        self.taille_carre = 100
        self.jeu = Puissance4()
        self.ia = IA()
        self.ia.charger_donnees()

        self.creer_carres()

    def creer_carres(self):
        for i in range(7):
            for j in range(6):
                id = self.cnv.create_rectangle(i * self.taille_carre, j * self.taille_carre,
                                               (i + 1) * self.taille_carre, (j + 1) * self.taille_carre, fill="white")
                self.cnv.tag_bind(id, "<Button-1>", lambda event, col=i: self.jouer_coup(event, col))

    def jouer_coup(self, event, colonne):
        if self.jeu.joueur == 1:
            self.jeu.jouer(colonne)
            self.cnv.itemconfig(self.cnv.find_closest(event.x, event.y), fill="red")

            if self.jeu.check_victoire():
                print("Vous avez gagné !")
                return

            # L'IA joue
            coup_ia = self.ia.choisir_coup(self.jeu.plateau)
            hauteur_colonne = next((i for i, row in enumerate(self.jeu.plateau) if row[coup_ia] == 0), None)
            if hauteur_colonne is not None:
                self.jeu.jouer(coup_ia)
                # Calcul de l'indice pour placer le carré jaune
                indice_canevas = coup_ia + (hauteur_colonne * 7)
                self.cnv.itemconfig(indice_canevas, fill="yellow")

            if self.jeu.check_victoire():
                print("L'IA a gagné !")
                return

            if self.jeu.joueur == 1:
                print("Attendez votre tour.")
        else:
            print("Attendez votre tour.")

    def run(self):
        self.fen.mainloop()


if __name__ == "__main__":
    interface = InterfaceGraphique()
    interface.run()
