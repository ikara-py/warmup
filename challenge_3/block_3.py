#!/usr/bin/env python3
import os

# _______________________ 3.1 __________________________
articles = ["pommes", "lait", "pain"]

def ecrire_liste_courses(chemin, articles):
    with open(chemin, 'w') as f:
        for art in articles:
            f.write(f"{art} \n")


# ecrire_liste_courses("courses.txt", articles)


# _______________________ 3.2 __________________________


def ajouter_article(chemin, item):
    
    with open(chemin, 'a') as f:
        f.write(f"{item} \n")

# ajouter_article("courses.txt", "oeufs")


# _______________________ 3.3 __________________________
def lire_fichier(file):
    try:
        with open(file, "r") as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError as err:
        print(f"Err : {err}")

# print(lire_fichier("courses.txt"))


# _______________________ 3.4 __________________________


def compter_lignes(file):
    with open(file, "r") as f:
        count = 0
        for i in f:
            if i.strip():
                count +=1

        return count

print(compter_lignes("courses.txt"))