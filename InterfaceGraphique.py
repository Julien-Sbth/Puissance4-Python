from tkinter import messagebox
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
        self.partie_terminee = False

        self.btn_rejouer = tk.Button(self.fen, text="Rejouer", command=self.rejouer_partie)
        self.btn_rejouer.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
        self.btn_rejouer.config(state="active")

        self.btn_joueur = tk.Button(self.fen, text="Jouer contre un joueur", command=self.player_against_player)
        self.btn_joueur.grid(row=0, column=1, padx=10, pady=10)

        self.btn_ia = tk.Button(self.fen, text="Jouer contre l'IA", command=self.PlayerAgainstIA)
        self.btn_ia.grid(row=0, column=2, padx=10, pady=10)

        self.btn_ia_vs_ia = tk.Button(self.fen, text="IA contre IA", command=self.IAvsIA)
        self.btn_ia_vs_ia.grid(row=0, column=3, padx=10, pady=10)

        self.creer_carres()

    def player_against_player(self):
        print("Jouer contre un joueur")
        self.mode = "joueur"

    def PlayerAgainstIA(self):
        print("Jouer contre l'IA")
        self.mode = "ia"
        self.tour = 1
        self.ia.entrainer_IA()

    def IAvsIA(self):
        print("IA contre IA")
        self.mode = "ia_vs_ia"
        self.tour = 1
        self.ia.entrainer_IA()
        self.IAversusIA()

    def rejouer_partie(self):
        self.jeu = Puissance4()
        self.creer_carres()
        self.tour = 1
        self.btn_rejouer.config(state="active")

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
                        messagebox.showinfo("You Win !", "Player 1 Win !")
                        self.btn_rejouer.config(state="active")
                        self.rejouer_partie()
                        return
                    self.tour = 2
                else:
                    self.jeu.jouer(colonne)
                    self.cnv.itemconfig(self.cnv.find_closest(colonne * self.taille_carre + self.taille_carre / 2,
                                                              ligne_vide * self.taille_carre + self.taille_carre / 2),
                                        fill="yellow")
                    if self.jeu.check_victoire():
                        messagebox.showinfo("You Lose !", "Player Two Win !")
                        self.rejouer_partie()
                        return
                    self.tour = 1
            else:
                messagebox.showinfo("Colonne pleine", "Veuillez choisir une autre colonne.")
        elif self.mode == "ia":
            ligne_vide = self.trouver_ligne_vide(colonne)
            if ligne_vide is not None:
                if self.tour == 1:
                    self.ia.charger_donnees()
                    self.jeu.jouer(colonne)
                    self.cnv.itemconfig(
                        self.cnv.find_closest(colonne * self.taille_carre + self.taille_carre / 2,
                                              ligne_vide * self.taille_carre + self.taille_carre / 2),
                        fill="red"
                    )
                    if self.jeu.check_victoire():
                        messagebox.showinfo("You Win !", "Player 1 Win !")
                        self.rejouer_partie()
                        return
                    self.tour = 2
                    self.ia_joue()
                else:
                    messagebox.showinfo("You Lose !", "IA Win !")
                    self.rejouer_partie()
                    return
        else:
            messagebox.showinfo("Colonne pleine", "Veuillez choisir une autre colonne.")

    def ia_joue(self):
        coup_ia = self.ia.prendre_decision_intelligente(self.jeu.plateau)
        ligne_vide = self.trouver_ligne_vide(colonne=coup_ia)
        if ligne_vide is not None:
            self.jeu.jouer(coup_ia)
            if self.jeu.check_victoire():
                print("IA a gagné !")
                return
            self.tour = 1

    def IAversusIA(self):
        if self.mode == "ia_vs_ia":
            if self.tour == 1:
                self.ia.charger_donnees()
                self.ia_joue()
                self.ia.enregistrer_resultat(self.jeu.plateau)
                self.ia.sauvegarder_donnees()
                self.tour = 2
            else:
                self.ia_joue()
                self.tour = 1
            if self.jeu.check_victoire():
                print("Partie terminée !")
                self.partie_terminee = True
                return
        if not self.partie_terminee:
            self.fen.after(1000, self.IAversusIA)

    def run(self):
        self.fen.mainloop()
