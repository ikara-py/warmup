#!/usr/bin/env python3

# _______________________ 1.2 __________________________


def division_securisee(a, b):
    try:
        calc = a / b
        return calc
    except ZeroDivisionError:
        return "Erreur : division par zero impossible."

# print(division_securisee(10, 2))
# print(division_securisee(10, 0))


# _______________________ 1.3 __________________________

def convertir_entier(value):
    try:

        int(value)
        return value
    except ValueError:
        return f"Erreur : {value} n'est pas un entier valide."


# print(convertir_entier(22))
# print(convertir_entier("yyyyyyy"))

# _______________________ 1.4 __________________________

notes = [12, 15, 9]

def acceder_element(list, index):
    try:
        return list[index]
    except IndexError:
        return f"Erreur : index {index} hors limites (taille de la liste : {len(list)})."

# print(acceder_element(notes, 10))
# print(acceder_element(notes, 1))


# _______________________ 1.5 __________________________

eleve = {"nom": "Sara", "age": 20}

def acceder_cle(dictionnaire, cle):
    try:
        return dictionnaire[cle]
    except KeyError:
        return f"Erreur : la cle '{cle}' n'existe pas."
    
# print(acceder_cle(eleve, "nom"))
# print(acceder_cle(eleve, "email"))


# _______________________ 1.6 __________________________

def traiter_valeur(value):

    try:
        return int(value)
    except ValueError:
        return f"Erreur : '{value}' n'est pas convertible."
    finally:
        print("Traitement termine.")

print(traiter_valeur(8))
print(traiter_valeur("x"))

