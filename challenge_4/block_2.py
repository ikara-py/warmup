#!/usr/bin/env python3


# _______________________ 2.1 __________________________

class CompteBancaire():

    nom_banque = "BanquePyDiag"
    nombre_total = 0


    def __init__(self, name, solde_initial = 100):
        self.__name = name
        self.__solde = solde_initial
        CompteBancaire.nombre_total += 1


    def deposer(self, amount):
        if amount <= 0:
            raise ValueError(f"le montant du depot doit etre positif {amount}")
        else:
            self.__solde += amount

    def retirer(self, amount):
        if amount > self.__solde :
            raise ValueError(f"fonds insuffisants (solde : {self.__solde}, retrait demande : {amount}")
        else:
            self.__solde -= amount

    @property
    def solde(self):
        return self.__solde

    @classmethod
    def nombre_comptes(cls):
        print(cls.nombre_total)

    @staticmethod
    def convertir_devise(montant, taux = 10.5):
        return montant * taux



# compte = CompteBancaire("Ali", solde_initial=100)
# print(compte.solde)
# compte.solde = 5000


# _______________________ 2.2 __________________________


# compte = CompteBancaire("Ali", solde_initial=100)
# compte.deposer(50)
# compte.retirer(30)
# print(compte.solde)


# _______________________ 2.3 __________________________

# compte = CompteBancaire("Ali", solde_initial=100)
# compte.deposer(-20)
# compte.retirer(500)


# _______________________ 2.4 __________________________


# c1 = CompteBancaire("Ali", 100)
# c2 = CompteBancaire("Sara", 200)
# print(c1.nom_banque, c2.nom_banque)
# print(c1.solde, c2.solde)


# _______________________ 2.5 __________________________

c1 = CompteBancaire("Ali", 100)
c2 = CompteBancaire("Sara", 200)
c3 = CompteBancaire("Lina", 0)
CompteBancaire.nombre_comptes()
print(CompteBancaire.convertir_devise(100, taux=10.5))