#!/usr/bin/env python3


# first_name = input("enter your first name : ")
# last_name = input("enter your last name : ")

# grades = []

# MAX_NUM = 3
# num= 1

# while num <= MAX_NUM:


#     note = input(f"enter grade number {num} : ")
#     grades.append(note)
#     num += 1

# for g in grades:
#     try:
#         float(g)
#         print(f"Note acceptee : {g}")
#     except:
#         print("it is not a number try again.")

        
# summ = 0

# try:

#     for grade in grades:
#         summ += float(grade)
#     print(f" : {summ/ len(grades):.2f}")
# except ValueError as err:
#     print(f"there is err {err}")

# # print(f"{first_name} {last_name} : {sum(grades)/ len(grades):.2f}")

# print(grades)


grades = [12, 13.22, 15]



def calculer_moyenne(grades):
    summ = 0

    try:
        for grade in grades:
            summ += float(grade)
        
        return round(summ / len(grades), 2)
    except ValueError as err:
        return err


valeurs_test = [9.9, 10.0, 11.9, 12.0, 15.9, 16.0, 20.0]

def appreciation(grades_list):
    for i in grades_list:
        if i >= 16 and i <= 20:
            print( "Tres bien")
        elif i >= 12 :
            print( "bien")
        elif i >= 10:
            print( "Passable")
        elif i < 10:
            print( "Insuffisant")


def appreciation2(note):
    
    if note >= 16 and note <= 20:
        return( "Tres bien")
    elif note >= 12 :
        return( "bien")
    elif note >= 10:
        return( "Passable")
    elif note < 10:
        return( "Insuffisant")

# print(appreciation2(12))

# print(calculer_moyenne(grades))

etudiants = [
    {"nom": "Karim", "notes": [12, 15, 9]},
    {"nom": "Sara", "notes": [18, 17, 16]},
    {"nom": "Lina", "notes": [6, 8, 5]},
]

def moyenne_groupe(etudiants):
    summ = 0
    temp = 0
    for student in etudiants :
        temp = sum(student["notes"])
        summ += temp / len(student["notes"])

    return round(summ / len(etudiants), 2)
# print(moyenne_groupe(etudiants))


notes = [14, 10, 18] # Maths, Francais, Sport
coefficients = [3, 2, 1]

def somme_recursive(notes):
    return round(sum(notes), 2)

# print(somme_recursive(notes))

def calculer_moyenne_ponderee(notes, coefficients):
    if len(notes) != len(coefficients):
        return "err the two lists has different lengths"
    
    start = 0
    notes_after_coefficients = []
    try:
        while start < len(notes):
            res = notes[start] * coefficients[start]
            notes_after_coefficients.append(res)
            start += 1
        return round(sum(notes_after_coefficients) / somme_recursive(coefficients), 2)
    except ZeroDivisionError as err:
        return f"there is err : {err}"

# print(calculer_moyenne_ponderee(notes, coefficients))


def dictionnaire_resultats(etudiants):
    dic = {}
    for i in etudiants:
        moyenn = calculer_moyenne(i["notes"])
        dic[i["nom"]] = {"moyenne":moyenn, "mention": appreciation2(moyenn)} 

    return dic


# print(dictionnaire_resultats(etudiants))
def classer_par_moyenne(resultats):

    return sorted(resultats.items(), key=lambda x: x[1]["moyenne"], reverse=True)

# print(classer_par_moyenne(dictionnaire_resultats(etudiants)))
# print(dictionnaire_resultats(etudiants).items())

def classement(sorted):
    order = 1
    for key, value in sorted:
        print(f"{order}. {key} - {value["moyenne"]}")
        order +=1

# classement(classer_par_moyenne(dictionnaire_resultats(etudiants)))

def echec_attendu(sorted):
    failed = []
    for key, value in sorted:
        if appreciation2(value["moyenne"]) == "Insuffisant":
            failed.append({key : value})

    return failed



# print(echec_attendu(classer_par_moyenne(dictionnaire_resultats(etudiants))))

def regrouper_par_mention(data):
    regroup = {}
    for key, value in data:
        if appreciation2(value["moyenne"]) not in regroup :
            regroup[appreciation2(value["moyenne"])] = [key]
        else:
            regroup[appreciation2(value["moyenne"])].append({key })

    return regroup

# print(regrouper_par_mention(classer_par_moyenne(dictionnaire_resultats(etudiants))))



noms = ["Karim", "Sara", "Lina", "Karim"]

def detection_de_doublon(data):
    dublicates = []
    for i in data:
        if data.count(i) > 1:
            dublicates.append(i)
    if dublicates:
        return "Attention, il y a des doublons !"
    else:
        return "c bon" 

# print(detection_de_doublon(noms))

groupe_a = {
"Karim": {"moyenne": 12.0, "mention": "Bien"},
}
groupe_b = {
"Karim": {"moyenne": 15.0, "mention": "Bien"},
"Sara": {"moyenne": 17.0, "mention": "Tres bien"},
}

def merge_groups(group_1, group_2):
    merged = group_1
    for key, value in group_2.items():
        if key in merged:
            merged[key] = [merged[key], value]
        else:
            merged[key] = value
    return merged

print(merge_groups(groupe_a, groupe_b))