import tkinter as tk
from tkinter import colorchooser, messagebox, Menu
from puissance4 import Puissance4

class Interface:
    def __init__(self):
        self.fen = tk.Tk()
        self.fen.title("Puissance 4")
        self.fen.geometry("600x500")  # Redimensionner la fenêtre
        self.cnv = tk.Canvas(self.fen, width=600, height=600, bg="blue")  # Changer la couleur de fond
        self.cnv.grid(row=0, column=0, padx=10, pady=10)  # Utiliser grid pour positionner le canvas
        self.taille_carre = 100
        self.ids = []
        self.colors = []  # Couleurs pour les joueurs 1 et 2
        self.current_player = 1  # Joueur 1 commence
        self.puissance4 = Puissance4()

        self.ask_colors()
        self.creer_carres()
        self.lier_evenements()
        self.creer_menu()  # Créer le menu de la partie

    def ask_colors(self):
        color1 = colorchooser.askcolor()[1]  # Demander au joueur 1 de choisir une couleur
        self.colors.append(color1)
        color2 = colorchooser.askcolor()[1]  # Demander au joueur 2 de choisir une couleur
        self.colors.append(color2)

    def creer_carres(self):
        for i in range(7):
            for j in range(6):
                id = self.cnv.create_rectangle(i * self.taille_carre, j * self.taille_carre,
                                               (i + 1) * self.taille_carre, (j + 1) * self.taille_carre, fill="white")
                self.ids.append(id)

    def change_color(self, event):
        color = self.colors[self.current_player - 1]
        id = self.cnv.find_withtag("current")[0]
        colonne = self.ids.index(id) % 7
        self.puissance4.jouer(colonne)
        self.cnv.itemconfig(id, fill=color)
        if self.puissance4.check_victoire():
            messagebox.showinfo("Fin de partie", f"Joueur {self.puissance4.joueur} a gagné !")
            self.rejouer()  # Proposer une nouvelle partie après la victoire
        else:
            self.current_player = 2 if self.current_player == 1 else 1  # Changer de joueur

    def lier_evenements(self):
        for id in self.ids:
            self.cnv.tag_bind(id, "<Button-1>", self.change_color)

    def creer_menu(self):
        menubar = Menu(self.fen)
        self.fen.config(menu=menubar)
        menu_partie = Menu(menubar, tearoff=0)
        menu_partie.add_command(label="Jouer contre un autre joueur", command=self.rejouer)
        menu_partie.add_command(label="Jouer contre l'IA", command=self.rejouer_ia)
        menu_partie.add_separator()
        menu_partie.add_command(label="Quitter", command=self.fen.quit)
        menubar.add_cascade(label="Partie", menu=menu_partie)

    def rejouer(self):
        if messagebox.askyesno("Rejouer ?", "Voulez-vous rejouer ?"):
            self.puissance4 = Puissance4()  # Réinitialiser le jeu
            self.colors.clear()  # Réinitialiser les couleurs
            self.cnv.delete("all")  # Effacer le canvas
            self.ask_colors()  # Redemander les couleurs
            self.creer_carres()  # Recréer les carrés
            self.current_player = 1  # Joueur 1 commence
        else:
            self.fen.quit()  # Quitter le jeu si le joueur ne veut pas rejouer

    def rejouer_ia(self):
        # Code pour jouer contre l'IA
        pass

    def run(self):
        self.fen.mainloop()

if __name__ == "__main__":
    interface = Interface()
    interface.run()
