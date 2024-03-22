from tkinter import messagebox
import time
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
        self.tour = 1
        self.mode = None

        self.btn_rejouer = tk.Button(self.fen, text="Rejouer", command=self.rejouer_partie)
        self.btn_rejouer.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
        self.btn_rejouer.config(state="disabled")

        self.btn_joueur = tk.Button(self.fen, text="Jouer contre un joueur", command=self.jouer_contre_joueur_action)
        self.btn_joueur.grid(row=0, column=1, padx=10, pady=10)

        self.btn_ia = tk.Button(self.fen, text="Jouer contre l'IA", command=self.jouer_contre_ia_action)
        self.btn_ia.grid(row=0, column=2, padx=10, pady=10)

        self.btn_ia_vs_ia = tk.Button(self.fen, text="IA contre IA", command=self.ia_vs_ia_action)
        self.btn_ia_vs_ia.grid(row=0, column=3, padx=10, pady=10)

        self.creer_carres()

    def jouer_contre_joueur_action(self):
        print("Jouer contre un joueur")
        self.mode = "joueur"

    def jouer_contre_ia_action(self):
        print("Jouer contre l'IA")
        self.mode = "ia"
        self.tour = 1
        self.ia.entrainer_IA()

    def ia_vs_ia_action(self):
        print("IA contre IA")
        self.mode = "ia_vs_ia"
        self.tour = 1
        self.ia.entrainer_IA()
        self.boucle_principale()

    def rejouer_partie(self):
        self.jeu = Puissance4()
        self.creer_carres()
        self.tour = 1
        self.btn_rejouer.config(state="normal")

    def creer_carres(self):
        self.cnv.delete("all")
        for i in range(7):
            for j in range(6):
                id = self.cnv.create_rectangle(i * self.taille_carre, j * self.taille_carre,
                                               (i + 1) * self.taille_carre, (j + 1) * self.taille_carre, fill="white")
                self.cnv.tag_bind(id, "<Button-1>", lambda event, col=i: self.jouer_coup(event, col))

    def trouver_ligne_vide(self, colonne):
        for ligne in range(5, -1, -1):
            if self.jeu.plateau[ligne][colonne] == 0:
                return ligne
        return None

    def jouer_coup(self, event, colonne):
        if self.mode == "joueur":
            ligne_vide = self.trouver_ligne_vide(colonne)
            if ligne_vide is not None:
                if self.tour == 1:
                    self.jeu.jouer(colonne)
                    self.cnv.itemconfig(self.cnv.find_closest(colonne * self.taille_carre + self.taille_carre / 2,
                                                              ligne_vide * self.taille_carre + self.taille_carre / 2),
                                        fill="red")
                    if self.jeu.check_victoire():
                        messagebox.showinfo("Fin de partie", "Vous avez gagné !")
                        self.btn_rejouer.config(state="normal")
                        return
                    self.tour = 2
                else:
                    self.jeu.jouer(colonne)
                    self.cnv.itemconfig(self.cnv.find_closest(colonne * self.taille_carre + self.taille_carre / 2,
                                                              ligne_vide * self.taille_carre + self.taille_carre / 2),
                                        fill="yellow")
                    if self.jeu.check_victoire():
                        print("Joueur 2 a gagné !")
                        messagebox.showinfo("You Win !", "Player Two Win !")
                        return
                    self.tour = 1
            else:
                print("Colonne pleine. Veuillez choisir une autre colonne.")
        elif self.mode == "ia":
            if self.tour == 1:
                self.jeu.jouer(colonne)
                self.cnv.itemconfig(self.cnv.find_closest(colonne * self.taille_carre + self.taille_carre / 2,
                                                          self.trouver_ligne_vide(
                                                              colonne) * self.taille_carre + self.taille_carre / 2),
                                    fill="red")
                if self.jeu.check_victoire():
                    print("Vous avez gagné !")
                    return
                self.tour = 2
                self.ia_joue()
            else:
                print("Attendez votre tour.")

    def ia_joue(self):
        coup_ia = self.ia.prendre_decision_intelligente(self.jeu.plateau)
        hauteur_colonne = next((i for i, row in enumerate(self.jeu.plateau) if row[coup_ia] == 0), None)
        if hauteur_colonne is not None:
            self.jeu.jouer(coup_ia)
            indice_canevas = coup_ia + (hauteur_colonne * 7)
            self.cnv.itemconfig(indice_canevas, fill="yellow")
            if self.jeu.check_victoire():
                print("IA a gagné !")
                return
            self.tour = 1

    def boucle_principale(self):
        while True:
            if self.mode == "ia_vs_ia":
                if self.tour == 1:
                    self.ia_joue()
                    self.ia.enregistrer_resultat(self.jeu.plateau)
                    self.ia.sauvegarder_donnees()
                    self.tour = 2
                else:
                    self.ia_joue()
                    self.tour = 1
                if self.jeu.check_victoire():
                    print("Partie terminée !")
                    return
            time.sleep(1)

    def run(self):
        self.fen.mainloop()
