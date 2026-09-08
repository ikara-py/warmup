#!/usr/bin/env python3


import numpy as np


# ____________________________ 0 ____________________________


# print("Version de NumPy :", np.__version__)



# ____________________________ 1 ____________________________

# 1.1 Crée un tableau 1D à partir de la liste [1, 2, 3, 4, 5]
a = np.array([1, 2, 3, 4, 5])
# print(a)


# 1.2 Crée un tableau 2D (3x3) à partir d'une liste de listes
b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
# print(b.shape)


# 1.3 Crée un tableau rempli de zéros de forme (2, 4)
zeros_arr = np.zeros((2, 4))
# print(zeros_arr)

# 1.4 Crée un tableau rempli de uns de forme (3, 3)
ones_arr = np.ones((3,3))
# print(ones_arr)


# 1.5 Crée un tableau contenant les entiers de 0 à 19 (inclus) avec arange

range_arr = np.arange(0, 20)

# print(range_arr)

# 1.6 Crée un tableau de 10 valeurs régulièrement espacées entre 0 et 1 (inclus) avec linspace
lin_arr = np.linspace(0.0 ,1.0, 10)
# print(lin_arr)


# 1.7 Crée une matrice identité 4x4
identity = np.eye(4)
# print(identity)

# 1.8 Crée un tableau 3x3 de nombres aléatoires entre 0 et 1 (utilise np.random)
# random_arr = np.random.rand(0, 1)

# print(random_arr)
# print(a, b, zeros_arr, ones_arr, range_arr, lin_arr, identity, random_arr, sep="\n\n")
