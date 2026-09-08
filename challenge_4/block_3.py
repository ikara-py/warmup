#!/usr/bin/env python3


# _______________________ 3.1 __________________________


class Vehicule():

    base = 20
    def __init__(self, marque, immatriculation, nombre_places=5):
        self.marque = marque
        self.immatriculation = immatriculation
        self.nombre_places = nombre_places

    def tarif_journalier():
        pass

class Voiture(Vehicule):

    def __init__(self, marque, immatriculation, nombre_places=5):
        super().__init__(marque, immatriculation, nombre_places)

    @property
    def tarif_journalier(self):
            return super().base + (5 * self.nombre_places)

    def __str__(self):
            return f"Marque : {self.marque}\nImmatriculation : {self.immatriculation}\nNombre places : {self.nombre_places}\nTarif_journalier : {self.tarif_journalier}"
    

class Moto(Vehicule):
    def __init__(self, marque, immatriculation, nombre_places=5, cylindree = 600):
        super().__init__(marque, immatriculation, nombre_places)
        self.cylindree = cylindree 

    def __str__(self):
        return f"Marque : {self.marque}\nImmatriculation : {self.immatriculation}\nCylindree : {self.cylindree}"
        

    def tarif_journalier(self):
        return super().base + (5 * self.cylindree)


class Camion(Vehicule):
    def __init__(self, marque, immatriculation, nombre_places=5, charge_utile = 3000):
        super().__init__(marque, immatriculation, nombre_places)
        self.charge_utile = charge_utile

    def __str__(self):
        return f"Marque : {self.marque}\nImmatriculation : {self.immatriculation}\nCharge utile : {self.charge_utile}"
    
    def tarif_journalier(self):
        return super().base + (5 * self.charge_utile)

# voiture = Voiture("Renault", "123-A-45", nombre_places=5)
# print(voiture.marque)
# print(voiture.tarif_journalier())
# print(voiture)


# _______________________ 3.2 __________________________


# moto = Moto("Yamaha", "987-B-65", cylindree=600)
# camion = Camion("Volvo", "456-C-78", charge_utile=3000)
# print(moto.tarif_journalier())
# print(camion.tarif_journalier())



# _______________________ 3.3 __________________________


# flotte = [
#     Voiture("Renault", "123-A-45", nombre_places=5),
#     Moto("Yamaha", "987-B-65", cylindree=600),
#     Camion("Volvo", "456-C-78", charge_utile=3000),
#     ]
# for v in flotte:
#     print(v.marque, "->", v.tarif_journalier())


# _______________________ 3.4 __________________________

# voiture = Voiture("Renault", "123-A-45", nombre_places=5)
# print(voiture)


