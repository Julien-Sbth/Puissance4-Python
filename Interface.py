import tkinter as tk
import Jeu

class Interface:
    def __init__(self):
        self.fen = tk.Tk()
        self.cnv = tk.Canvas(self.fen, width=700, height=600, bg="white")
        self.cnv.grid()
        self.taille_carre = 100

        self.creer_carres()

    def creer_carres(self):
        for i in range(7):
            for j in range(6):
                id = self.cnv.create_rectangle(i * self.taille_carre, j * self.taille_carre,
                                               (i + 1) * self.taille_carre, (j + 1) * self.taille_carre, fill="white")
                self.cnv.tag_bind(id, "<Button-1>", self.change_color)

    def change_color(self, event):
        id = self.cnv.find_withtag("current")[0]
        self.cnv.itemconfig(id, fill="red")

    def run(self):
        self.fen.mainloop()


if __name__ == "__main__":
    app = Interface()
    app.run()