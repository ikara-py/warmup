#!/usr/bin/env python3

# _______________________ 1.1 __________________________
notes = [12, 18, 7, 15, 9, 20, 3, 14]

def max_min(notes):
    max = notes[0]
    min = notes[0]
    for i in notes:
        if i > max:
            max = i
        if i < min:
            min = i

    return f"Note max : {max} \nNote min : {min}"


# print(max_min(notes))

# _______________________ 1.2 __________________________


notes = [8, 14, 6, 17, 11, 20]
seuil = 12

def notes_au_dessus(notes, seuil):
    return [x for x in notes if x > seuil]

# print(notes_au_dessus(notes, seuil))



# _______________________ 1.3 __________________________


fruits = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]

def not_counter(fruits):
    dic = {}

    for i in fruits:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] = dic[i] + 1

    for n in dic:
        print(f"{n} : {dic[n]}")



# not_counter(fruits)


# _______________________ 1.4 __________________________

liste = [1, 2, 3, 4, 5]
# print(len(liste))

def inversion(liste):
    n = len(liste) + 1
    j = -1
    result = []
    while j != -n:
        result.append(liste[j])
        j -=1

    return result


# print(inversion(liste))


# _______________________ 1.5 __________________________ SKIPPED

liste_a = [1, 4, 7]
liste_b = [2, 3, 8, 9]
def merge(liste_a ,liste_b):
    merged = liste_a

    for i in liste_b:
        if i not in merged:
            merged.append(i)

    # print(merged)
    track = len(merged)

    for i in range(track -1):
        while track < len(merged):
            temp = 0
            if merged[track -1] > merged[track]:
                temp = merged[i]
                merged[i] = merged[track -1]
                merged[track -1] = temp
            track +=1

    return merged

# print(merge(liste_a ,liste_b))


# _______________________ 1.6 __________________________



nombres = [3, 12, 7, 25, 8, 19, 2]


def squares(nombres):
    sq = list(map(lambda x : x * x ,[x for x in nombres if x % 2 == 0]))
    print(sq)

squares(nombres)