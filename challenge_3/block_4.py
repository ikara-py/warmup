#!/usr/bin/env python3

import csv
from block_2 import StockInsuffisantError, retirer_stock

# _______________________ 4.1 __________________________


def lire_fichier_securise(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()
            return lignes

    except FileNotFoundError:
        print(f'Err : "{chemin}" doesnt exist')
        return []

    except PermissionError:
        print(f'Err : you dont have permission to this file "{chemin}".')
        return []


print(lire_fichier_securise("courses.txt"))
print(lire_fichier_securise("inexistant.txt"))



# _______________________ 4.2 __________________________



def calculer_moyenne_csv(chemin):
    notes = []

    try:
        with open(chemin, "r", encoding="utf-8") as f:
            lecteur = csv.DictReader(f)

            for ligne in lecteur:
                nom = ligne["nom"]
                note = ligne["note"]

                try:
                    note = float(note)
                    notes.append(note)

                except ValueError:
                    print(f'Attention : note invalide pour "{nom}" ("{ligne["note"]}"), ligne ignorée.')

        if notes:
            moyenne = sum(notes) / len(notes)
            print(f"Moyenne calculée ({len(notes)} notes valides) : {moyenne:.2f}")
            return moyenne
        else:
            print("Aucune note valide.")
            return None

    except FileNotFoundError:
        print(f'Err : "{chemin}" doesnt exist.')
        return None

    except PermissionError:
        print(f'Err : you dont have permission to this file "{chemin}".')
        return None



# calculer_moyenne_csv("notes.csv")


# _______________________ 4.3 __________________________


