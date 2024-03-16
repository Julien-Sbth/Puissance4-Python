import keyboard

from IA import IA
from Jeu import Puissance4


def main():
    while True:
        jeu = Puissance4()
        ia1 = IA()
        ia2 = IA()
        ia1.charger_donnees()
        ia2.charger_donnees()
        print(jeu.plateau)
        while True:
            coup_ia1 = ia1.choisir_coup(jeu.plateau)
            if coup_ia1 is not None:
                jeu.jouer(coup_ia1)
                ia1.coups_joues.append(coup_ia1)
                if jeu.check_victoire():
                    ia1.enregistrer_resultat(ia1.coups_joues)
                    break
            else:
                print("Aucun coup disponible pour l'IA 2.")
                break

            coup_ia = ia1.choisir_coup(jeu.plateau)
            if coup_ia is not None:
                jeu.jouer(coup_ia)
                ia2.coups_joues.append(coup_ia)
                if jeu.check_victoire():
                    ia1.enregistrer_resultat(ia2.coups_joues)
                    break
            else:
                print("Aucun coup disponible pour l'IA 2.")
                break

        print("Appuyez sur 'q' pour quitter ou appuyez sur une autre touche pour continuer...")
        if keyboard.is_pressed('q'):
            break


if __name__ == "__main__":
    main()
