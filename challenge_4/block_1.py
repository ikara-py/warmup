#!/usr/bin/env python3


# _______________________ 1.1 __________________________



class Livre():
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.disponible = True

    def __str__(self):
        return f"{self.name} de {self.author} -- {'disponible' if self.disponible else 'pas disponible'}"


# livre = Livre("Dune", "Frank Herbert")
# print(livre)




# _______________________ 1.2 __________________________

class Adherent():
    def __init__(self, name):
        self.name = name
        self.book_list = []


    def emprunter_livre(self, livre):
        if not livre.disponible:
            print(f"Erreur : le livre {livre.name} n'est pas disponible.")
        else:
            livre.disponible = False
            self.book_list.append(livre)

    def rendre_livre(self, livre):
        try:
            livre.disponible = True
            self.book_list.remove(livre)
        except ValueError:
            print("book not in books list")

    def nombre_livres_empruntes(self):
        return len(self.book_list)


# livre = Livre("Dune", "Frank Herbert")
# ali = Adherent("Ali")

# ali.emprunter_livre(livre)
# ali.rendre_livre(livre)



# print(livre)
# print(ali.nombre_livres_empruntes())

# print(livre.disponible)

# _______________________ 1.3 __________________________


# livre = Livre("Dune", "Frank Herbert")
# ali = Adherent("Ali")
# sara = Adherent("Sara")
# ali.emprunter_livre(livre)
# sara.emprunter_livre(livre)


# _______________________ 1.4 __________________________


livre = Livre("Dune", "Frank Herbert")
ali = Adherent("Ali")
ali.emprunter_livre(livre)
ali.rendre_livre(livre)
print(livre)
print(ali.nombre_livres_empruntes())