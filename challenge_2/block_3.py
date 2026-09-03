#!/usr/bin/env python3


# _______________________ 3.1 __________________________

atelier_python = ["Ali", "Sara", "Lina", "Karim"]
atelier_java = ["Sara", "Omar", "Lina", "Yasmine"]

def Inscrits_aux_deux_ateliers(atelier_1,atelier_2):
    dub = set()
    merged = set(atelier_1).union(set(atelier_2))
    unique = set()

    for i in atelier_1:
        if i in atelier_2:
            dub.add(i)

        if i not in atelier_2:
            unique.add(i)

    print(f"Inscrits aux deux ateliers : {dub}")
    print(f"Inscrits a au moins un atelier : {merged}")
    print(f"Uniquement Python :  {unique}")

# Inscrits_aux_deux_ateliers(atelier_python,atelier_java)



# _______________________ 3.2 __________________________

liste_1 = ["Ali", "Sara", "Lina"]
liste_2 = ["Ali", "Sara", "Ali"]

def a_des_doublons(list):
    j = set(list)
    if len(j) != len(list):
        return True
    return False

# print(a_des_doublons(liste_2))


# _______________________ 3.3 __________________________


tags_articles = [
["python", "web", "api"],
["python", "data"],
["web", "css"],
]

def unique(tags_articles):
    result = set()

    for i in tags_articles:
        result = result.union(set(i))

    return result

# print(unique(tags_articles))


# _______________________ 3.4 __________________________

