#!/usr/bin/env python3

from statistics import mean
from abc import ABC, abstractmethod
# _______________________ 4.1 __________________________



class Modele(ABC):
    @abstractmethod
    def entrainer(self, donnees):
        pass

    @abstractmethod
    def predire(self ,entree):
        pass

class ModeleMoyenne(Modele):

    def entrainer(self, donnees):
        
        self.moyenne = mean(donnees)
        

    def predire(self, entree):
        return self.moyenne
    
class ModeleLineaireSimple(Modele):
    def __init__(self, poids=2, biais=1):
        self.poids = poids
        self.biais = biais


    def entrainer(self, donnees):
        if donnees:
            return sum(donnees) / len(donnees)
        else:
            return None
        
    def predire(self ,entree):
        return self.poids * entree + self.biais
    

def normaliser(donnees):
    maximum = max(donnees)
    return [d / maximum for d in donnees]

class Pipeline:
    def __init__(self, pretraitement=normaliser, modele=ModeleMoyenne()):
        self.pretraitement = pretraitement
        self.modele = modele

    def executer(self, donnees, entree=5):
        self.modele.entrainer(self.pretraitement(donnees))
        print(self.modele.entrainer(self.pretraitement(donnees)))
        return self.modele.predire(entree)




# modele = Modele()

# _______________________ 4.2 __________________________

# donnees = [5, 8, 11]
# modele = ModeleMoyenne()
# print(modele.entrainer(donnees))
# modele.predire(999)



# _______________________ 4.3 __________________________

# modele = ModeleLineaireSimple(poids=2, biais=1)
# modele.entrainer(donnees=None)
# print(modele.predire(5))


# _______________________ 4.4 __________________________

# donnees = [5, 8, 11]

# pipeline_moyenne = Pipeline(pretraitement=normaliser, modele = ModeleMoyenne())
# pipeline_lineaire = Pipeline(pretraitement=normaliser, modele = ModeleLineaireSimple(2, 1))

# for pipeline in [pipeline_moyenne, pipeline_lineaire]:
#     resultat = pipeline.executer(donnees, entree=5)
#     print(type(pipeline.modele).__name__, "->", resultat)
