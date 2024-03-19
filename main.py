import tkinter as tk
from IA import IA
from Jeu import Puissance4


class InterfaceGraphique:
    def __init__(self):
        self.fen = tk.Tk()
        self.cnv = tk.Canvas(self.fen, width=700, height=600, bg="white")
        self.cnv.grid()
        self.taille_carre = 100
        self.jeu = Puissance4()
        self.ia = IA()
        self.ia.charger_donnees()

        self.tour = 1
        self.mode = None

        self.btn_joueur = tk.Button(self.fen, text="Jouer contre un joueur", command=self.jouer_contre_joueur_action)
        self.btn_joueur.grid(row=0, column=0, padx=10, pady=10)

        self.btn_ia = tk.Button(self.fen, text="Jouer contre l'IA", command=self.jouer_contre_ia_action)
        self.btn_ia.grid(row=0, column=1, padx=10, pady=10)

        self.creer_carres()

    def jouer_contre_joueur_action(self):
        print("Jouer contre un joueur")
        self.mode = "joueur"

    def jouer_contre_ia_action(self):
        print("Jouer contre l'IA")
        self.mode = "ia"
        self.tour = 1

    def creer_carres(self):
        for i in range(7):
            for j in range(6):
                id = self.cnv.create_rectangle(i * self.taille_carre, j * self.taille_carre,
                                               (i + 1) * self.taille_carre, (j + 1) * self.taille_carre, fill="white")
                self.cnv.tag_bind(id, "<Button-1>", lambda event, col=i: self.jouer_coup(event, col))

    def jouer_coup(self, event, colonne):
        if self.mode == "joueur":
            if self.tour == 1:
                self.jeu.jouer(colonne)
                self.cnv.itemconfig(self.cnv.find_closest(event.x, event.y), fill="red")
                if self.jeu.check_victoire():
                    print("Joueur 1 a gagné !")
                    return
                self.tour = 2
            else:
                self.jeu.jouer(colonne)
                self.cnv.itemconfig(self.cnv.find_closest(event.x, event.y), fill="yellow")
                if self.jeu.check_victoire():
                    print("Joueur 2 a gagné !")
                    return
                self.tour = 1
        elif self.mode == "ia":
            if self.tour == 1:
                self.jeu.jouer(colonne)
                self.cnv.itemconfig(self.cnv.find_closest(event.x, event.y), fill="red")
                if self.jeu.check_victoire():
                    print("Vous avez gagné !")
                    return
                self.tour = 2
                self.ia_joue()
            else:
                print("Attendez votre tour.")

    def ia_joue(self):
        coup_ia = self.ia.choisir_coup(self.jeu.plateau)
        hauteur_colonne = next((i for i, row in enumerate(self.jeu.plateau) if row[coup_ia] == 0), None)
        if hauteur_colonne is not None:
            self.jeu.jouer(coup_ia)
            indice_canevas = coup_ia + (hauteur_colonne * 7)
            self.cnv.itemconfig(indice_canevas, fill="yellow")
            if self.jeu.check_victoire():
                print("L'IA a gagné !")
                return
            self.tour = 1

    def run(self):
        self.fen.mainloop()


if __name__ == "__main__":
    interface = InterfaceGraphique()
    interface.run()
