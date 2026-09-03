#!/usr/bin/env python3

# _______________________ 4.1 __________________________


ventes = [
{"produit": "pommes", "montant": 120},
{"produit": "bananes", "montant": 80},
{"produit": "pommes", "montant": 45},
{"produit": "oranges", "montant": 60},
{"produit": "bananes", "montant": 30},
]

def analyse(ventes):
    total_product = {}
    distincts = set()
    meilleur = {"name": "placeholder", "mount": 0}
    for i in ventes:
        if i["produit"] not in total_product:
            total_product[i["produit"]] = i["montant"]
            distincts.add(i["produit"])
        else:
            total_product[i["produit"]] += i["montant"]
            if total_product[i["produit"]] > meilleur["mount"]:
                meilleur = {"name": i["produit"], "mount": total_product[i["produit"]]}

    print(f"Total par produit : {total_product}")
    print(f"Meilleur produit : {meilleur}")
    print(f"Produits distincts : {distincts}")


# analyse(ventes)


# _______________________ 4.2 __________________________

inv1 = {"pommes": 20, "bananes": 15}
inv2 = {"bananes": 10, "kiwis": 5}

def fusion(inv1, inv2):

    fus = inv1
    # print(fus)
    for k, v in inv2.items():
        if k not in fus:
            fus[k] = v
        else:
            fus[k] += v

    return fus

# print(fusion(inv1, inv2))


# _______________________ 4.3 __________________________

etudiants = [
{"nom": "Ali", "matieres": {"maths": 14, "physique": 12}},
{"nom": "Sara", "matieres": {"maths": 18, "physique": 16, "svt": 15}},
{"nom": "Lina", "matieres": {"maths": 9, "physique": 11}},
]


def mini_challenge(etudiants):

    enseignees = set()
    matiere = {}
    meilleure = {"name":"placeholder", "note": 0}

    for i in etudiants:
        total= 0
        for b , n in i["matieres"].items():
            
            if b not in matiere:
                matiere[b] = [n]
            elif b in matiere:
                matiere[b].append(n)
            enseignees.add(b)
            total += n

            
        print(f"{i["nom"]} : {round(total / len(i["matieres"]), 2)}")

    print(f"Matieres enseignees (set) : {enseignees}")

    for k, v in matiere.items():
        print(f"{k} : {v}")

        calc = sum(v) / len(v)
        if calc > meilleure["note"]:
            meilleure["name"] = k
            meilleure["note"] = calc


    print(f"Meilleure matiere (moyenne globale) : {meilleure["name"]} {meilleure["note"]}")

# mini_challenge(etudiants)