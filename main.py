import tkinter as tk
from puissance4 import Puissance4
from puissance4gui import Puissance4GUI

class InterfaceGraphique:
    def __init__(self):
        self.fen = tk.Tk()
        self.fen.title("Puissance 4")

        self.btn_joueur = tk.Button(self.fen, text="Jouer contre un joueur", command=self.jouer_contre_joueur_action)
        self.btn_joueur.pack()


    def jouer_contre_joueur_action(self):
        puissance4 = Puissance4()
        interface = Puissance4GUI(puissance4)
        interface.run()

    def run(self):
        self.fen.mainloop()

if __name__ == "__main__":
    interface = InterfaceGraphique()
    interface.run()
