import tkinter as tk
from tkinter import messagebox

class Puissance4GUI:

    def __init__(self, puissance4):
        self.puissance4 = puissance4
        self.window = tk.Tk()
        self.ia = None
        self.window.title("Puissance 4")
        self.buttons = []

        for i in range(6):
            row = []
            for j in range(7):
                button = tk.Button(self.window, width=5, height=2, bg="white", command=lambda i=i, j=j: self.jouer(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def jouer(self, i, j):
        if self.puissance4.plateau[0][j] != 0:
            messagebox.showerror("Erreur", "Cette colonne est pleine !")
            return
        ligne = self.puissance4.jouer_coup(j)
        if ligne == -1:
            return
        self.buttons[ligne][j].config(bg="yellow" if self.puissance4.joueur == 1 else "red")
        if self.puissance4.verifier_victoire():
            messagebox.showinfo("Victoire", f"Le joueur {self.puissance4.joueur} a gagné !")
            self.window.quit()
            return
        self.puissance4.joueur = 3 - self.puissance4.joueur

        def jouer(self, i, j):
            ligne = self.puissance4.jouer_coup(j)
            if ligne < 0:
                messagebox.showerror("Erreur", "Cette colonne est pleine !")
                return
            self.buttons[ligne][j].config(bg="yellow" if self.puissance4.joueur == 1 else "red")

            if self.puissance4.verifier_victoire():
                messagebox.showinfo("Victoire", f"Le joueur {self.puissance4.joueur} a gagné !")
                self.window.quit()
                return

            self.puissance4.joueur = 3 - self.puissance4.joueur

    def run(self):
        self.window.mainloop()
