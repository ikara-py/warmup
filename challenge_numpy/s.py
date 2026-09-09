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
random_arr = np.random.rand(3, 3)
# print(random_arr)

# print(a, b, zeros_arr, ones_arr, range_arr, lin_arr, identity, random_arr, sep="\n\n")



# ____________________________ 2 ____________________________



# m = np.array([[1, 2, 3], [4, 5, 6]])

# 2.1 Affiche la forme (shape) de m
# print("shape :", np.shape(m))

# 2.2 Affiche le nombre de dimensions de m
# print("ndim :", np.ndim(m))

# 2.3 Affiche le nombre total d'éléments de m
# print("size :", np.size(m))

# 2.4 Affiche le type des éléments de m
# print("dtype :", m.dtype)

# 2.5 Crée un nouveau tableau identique à m mais avec des éléments en float64
# m_float = m.astype(np.float64)
# print(m_float.dtype)


# ____________________________ 3 ____________________________



arr = np.arange(1, 26).reshape(5, 5)
# print(arr)

# 3.1 Récupère l'élément à la ligne 2, colonne 3 (index 0-based)
elem = arr[:,3]
# print(elem)

# 3.2 Récupère la première ligne entière
first_row = arr[0]
# print(first_row)


# 3.3 Récupère la dernière colonne entière
last_col = arr[-1]
# print(last_col)

# 3.4 Récupère la sous-matrice des 2 premières lignes et 3 premières colonnes
sub_matrix = arr[:3, :3]
# print(sub_matrix)

# 3.5 Récupère une ligne sur deux (lignes 0, 2, 4)
every_other_row = arr[0:5:2]
# print(every_other_row)

#!! 3.6 Inverse l'ordre des colonnes de arr
reversed_cols = arr[:, ::-1]
# print(reversed_cols)

# print(elem, first_row, last_col, sub_matrix, every_other_row, reversed_cols, sep="\n\n")


# ____________________________ 4 ____________________________

v1 = np.array([1, 2, 3])
v2 = np.array([10, 20, 30])

# 4.1 Additionne v1 et v2 élément par élément
sum_v = np.dstack([v1, v2])
x = sum_v.reshape((1, sum_v.size))[0]
# print(x)
# print(sum_v.size)

# 4.2 Multiplie v1 et v2 élément par élément
mult_v = np.multiply(v1, v2)
# print(mult_v)



# 4.3 Calcule le produit scalaire (dot product) de v1 et v2
dot_v = sum(mult_v)
# print(dot_v)


# 4.4 Ajoute le scalaire 5 à tous les éléments de v1 (broadcasting scalaire)
plus_five = v1 + 5
# print(plus_five)


# 4.5 Soit la matrice M (3x3) et le vecteur row (taille 3).

# Ajoute row à chaque ligne de M grâce au broadcasting (sans boucle !)
M = np.ones((3, 3))
row = np.array([1, 2, 3])
M_plus_row = M + row

# print(M_plus_row)

# 4.6 Calcule la racine carrée de chaque élément de v2
sqrt_v2 = np.sqrt(v2)
# print(sqrt_v2)

# print(sum_v, mult_v, dot_v, plus_five, M_plus_row, sqrt_v2, sep="\n\n")


# ____________________________ 5 ____________________________



data = np.array([[4, 9, 2],
                  [1, 7, 5],
                  [8, 3, 6]])

# 5.1 Calcule la somme de tous les éléments
total = np.sum(data)
# print(total)


# 5.2 Calcule la moyenne de chaque colonne (axis=0)
mean_cols = np.mean(data, axis=0)
# print(mean_cols)

# 5.3 Calcule le maximum de chaque ligne (axis=1)
max_rows = np.max(data, axis=1)
# print(max_rows)


# 5.4 Trouve l'indice (position) de la valeur minimale globale (argmin)
idx_min = np.argmin(data)
# print(idx_min)


# 5.5 Calcule l'écart-type (std) de tout le tableau
std_all = np.std(data)
# print(std_all)

# 5.6 Trouve la valeur maximale de chaque colonne, ET son indice de ligne
max_col_values = np.max(data, axis= 0)
max_col_indices = np.argmax(data == max_col_values, axis=0)
# print(max_col_values)
# print(max_col_indices)


print(total, mean_cols, max_rows, idx_min, std_all, max_col_values, max_col_indices, sep="\n\n")

