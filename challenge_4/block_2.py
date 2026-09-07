#!/usr/bin/env python3


# _______________________ 2.1 __________________________

class CompteBancaire():
    def __init__(self, name, solde_initial = 100):
        self.__name = name
        self.__solde = solde_initial

    @property
    def solde(self):
        return self.__solde



compte = CompteBancaire("Ali", solde_initial=100)
compte.solde
compte.solde = 5000


# _______________________ 2.2 __________________________
