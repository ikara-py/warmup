#!/usr/bin/env python3

# _______________________ 2.1 __________________________

def verifier_age(value):
    if value < 0:
        raise Exception(f"ValueError: l’age ne peut pas etre negatif {value}.")
    else:
        return f"Age valide : {value}"


#print(verifier_age(-3))

# _______________________ 2.2 __________________________


def traiter_liste_de_valeurs(values):
    for i in values:
        try:
            int(i)
        except ValueError as e:
            print(f"valeur '{i}' invalide, exception relancee.")
            raise




# traiter_liste_de_valeurs(["3", "9", "x", "5"])

# _______________________ 2.3 __________________________

class StockInsuffisantError(Exception):
    def __init__(self, product, demand, disponible):
        message = f"stock insuffisant pour '{product}' (demande : {demand}, disponible : {disponible})"
        super().__init__(message)


# _______________________ 2.4 __________________________


stock = {"pommes": 20, "bananes": 4}

def retirer_stock(stock, item, quantity):
    if item not in stock:
        print("product is not in stock")
        return

    disponible = stock[item]

    if quantity <= disponible:
        print(f"Retrait effectue: {quantity} {item}.")
        stock[item] -= quantity
    else:
        raise StockInsuffisantError(item, quantity, disponible)

retirer_stock(stock, "pommes", 5)
retirer_stock(stock, "bananes", 10)


