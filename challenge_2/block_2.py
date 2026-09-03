#!/usr/bin/env python3



# _______________________ 2.1 __________________________

stock = {"pommes": 50, "bananes": 30, "oranges": 0}

def vendre(stock, product, quantity):
    if product not in stock:
        print("product is not in stock")
        return

    for key, value in stock.items():
        if key == product:
            if quantity > value:
                return f"Stock insuffisant pour {key} (disponible : {value})."
            else:
                stock[key] -= quantity
                return f"Vente enregistree : {quantity} {product}."

# print(stock)

vendre(stock, "pommes", 20)
vendre(stock, "oranges", 5)


# print(stock)


# _______________________ 2.2 __________________________


stock = {"pommes": 30, "bananes": 0, "oranges": 0, "kiwis": 12}

def produits_epuises(stock):
    out_of_stock = []
    for key, value in stock.items():
        if value == 0:
            out_of_stock.append(key)

    return out_of_stock

# print(produits_epuises(stock))



# _______________________ 2.3 __________________________


commandes = [
{"client": "Ali", "produit": "pommes", "quantite": 5},
{"client": "Sara", "produit": "bananes", "quantite": 10},
{"client": "Ali", "produit": "oranges", "quantite": 2},
]


def total_par_client(commandes):
    track = {}

    for i in commandes:
        if i["client"] not in track :
            track[i["client"]] = i["quantite"]
        else:
            track[i["client"]] += i["quantite"]

    return track


# print(total_par_client(commandes))


# _______________________ 2.4 __________________________


d = {"a": 1, "b": 2, "c": 3}

def inversion_dictionnaire(d):
    dic = {}

    for key, value in d.items():
        if value not in dic:
            dic[value] = key

    return dic
    # return {v:k for k,v in d.items()}


# print(inversion_dictionnaire(d))



# _______________________ 2.5 __________________________


mots = ["chat", "elephant", "abeille", "riz"]

def comprehension(mots):
    return {k: len(k) for k in mots}

# print(comprehension(mots))


# _______________________ 2.5 __________________________


entreprise = {
"IT": ["Ali", "Sara", "Omar"],
"RH": ["Lina"],
"Ventes": ["Karim", "Yasmine", "Nadia", "Hicham"],
}


def imbriques(entreprise):
    for key, value in entreprise.items():
        print(f"{key} : {len(value)} employe(s)")


imbriques(entreprise)