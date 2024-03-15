import tkinter as tk


class Interface:
    def __init__(self):
        self.fen = tk.Tk()
        self.fen.title("Puissance 4")
        self.cnv = tk.Canvas(self.fen, width=700, height=600, bg="blue")  # Changer la couleur de fond
        self.cnv.grid()
        self.taille_carre = 100
        self.ids = []
        self.colors = ["yellow", "red"]  # Couleurs pour les joueurs 1 et 2
        self.current_player = 1  # Joueur 1 commence

        self.creer_carres()
        self.lier_evenements()

    def creer_carres(self):
        for i in range(7):
            for j in range(6):
                id = self.cnv.create_rectangle(i * self.taille_carre, j * self.taille_carre,
                                               (i + 1) * self.taille_carre, (j + 1) * self.taille_carre, fill="white")
                self.ids.append(id)

    def change_color(self, event):
        id = self.cnv.find_withtag("current")[0]
        if self.current_player == 1:
            self.cnv.itemconfig(id, fill=self.colors[0])
            self.current_player = 2  # Passage au joueur 2
        else:
            self.cnv.itemconfig(id, fill=self.colors[1])
            self.current_player = 1  # Passage au joueur 1

    def lier_evenements(self):
        for id in self.ids:
            self.cnv.tag_bind(id, "<Button-1>", self.change_color)

    def run(self):
        self.fen.mainloop()

if __name__ == "__main__":
    interface = Interface()
    interface.run()
